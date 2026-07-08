import re
from typing import Any

from placementiq.common.clean_text import (
    clean_text,
    clean_text_list,
)

BASE_EXPERIENCE_URL = "https://internito.csesnitw.in/experiences/"


def parse_batch(batch: str | None) -> tuple[int | None, int | None]:
    """
    Convert '2019-2023' into (2019, 2023).
    """

    if not batch:
        return None, None

    try:
        start_year, end_year = batch.split("-")
        return int(start_year), int(end_year)

    except (ValueError, AttributeError):
        return None, None


def normalize_company(company: str | None) -> str:
    """
    Normalize company name.
    """

    if not company:
        return ""

    return clean_text(company).title()


def normalize_branches(
    branches: list[str] | None,
) -> list[str]:
    """
    Normalize branch names.
    """

    if not branches:
        return []

    return sorted(
        {clean_text(branch).upper() for branch in branches if clean_text(branch)}
    )


def extract_duration(description: str) -> str | None:
    """
    Extract duration like '50 mins'
    from interview description.
    """

    if not description:
        return None

    match = re.search(
        r"(\d+\s*mins?)",
        description,
        flags=re.IGNORECASE,
    )

    if match:
        return match.group(1)

    return None


def infer_round_type(description: str) -> str:
    """
    Infer interview round type.
    """

    if not description:
        return "Unknown"

    text = description.lower()

    if "hr interview" in text:
        return "HR"

    if "technical interview" in text:
        return "Technical"

    if "managerial" in text:
        return "Managerial"

    if "system design" in text:
        return "System Design"

    if "coding" in text:
        return "Coding"

    if "online test" in text:
        return "Online Test"

    return "Mixed"


def extract_round_title(
    title: str | None,
    description: str | None,
) -> str:
    """
    Fix incorrect round titles using
    the description if possible.
    """

    if description:
        match = re.search(
            r"(Round\s+\d+)",
            description,
            flags=re.IGNORECASE,
        )

        if match:
            return match.group(1)

    return clean_text(title)


def normalize_online_test(
    raw: dict[str, Any],
) -> dict[str, Any]:
    """
    Normalize online test section.
    """

    return {
        "description": clean_text(raw.get("OT_description")),
        "duration": clean_text(raw.get("OT_duration")),
        "questions": clean_text_list(raw.get("OT_questions")),
    }


def normalize_round(
    round_data: dict[str, Any],
) -> dict[str, Any]:
    """
    Normalize one interview round.
    """

    description = clean_text(round_data.get("description"))

    return {
        "title": extract_round_title(
            round_data.get("title"),
            description,
        ),
        "type": infer_round_type(
            description,
        ),
        "description": description,
        "duration": extract_duration(
            description,
        ),
    }


def normalize_rounds(
    rounds: list[dict[str, Any]] | None,
) -> list[dict[str, Any]]:
    """
    Normalize all interview rounds.
    """

    if not rounds:
        return []

    return [normalize_round(round_data) for round_data in rounds]


def normalize_interview(
    raw_interview: dict[str, Any],
) -> dict[str, Any]:
    """
    Convert one raw API interview into
    the PlacementIQ schema.
    """

    start_year, end_year = parse_batch(raw_interview.get("batch"))

    interview_id = raw_interview.get("_id")

    interview = {
        # ---------- Basic ----------
        "id": interview_id,
        "company": normalize_company(raw_interview.get("company")),
        "experience_type": clean_text(raw_interview.get("experienceType")),
        "batch": clean_text(raw_interview.get("batch")),
        "start_year": start_year,
        "end_year": end_year,
        "cgpa_cutoff": raw_interview.get("cgpaCutoff"),
        "eligible_branches": normalize_branches(raw_interview.get("eligibleBranches")),
        "number_of_selections": raw_interview.get(
            "numberOfSelections",
            0,
        ),
        # ---------- Online Test ----------
        "online_test": normalize_online_test(raw_interview),
        # ---------- Interview ----------
        "interview_rounds": normalize_rounds(raw_interview.get("interviewRounds")),
        "other_comments": clean_text(raw_interview.get("other_comments")),
        "job_description": clean_text(raw_interview.get("jobDescription")),
        "rounds": raw_interview.get(
            "rounds",
            [],
        ),
        # ---------- Metadata ----------
        "status": clean_text(raw_interview.get("status")),
        "created_at": raw_interview.get("createdAt"),
        "updated_at": raw_interview.get("updatedAt"),
        "source_url": (f"{BASE_EXPERIENCE_URL}{interview_id}"),
    }

    # Basic validation

    if not interview["id"]:
        raise ValueError("Interview ID missing.")

    if not interview["company"]:
        raise ValueError("Company missing.")

    return interview
