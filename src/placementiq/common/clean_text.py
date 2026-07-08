import re

from ftfy import fix_text


def fix_encoding(text: str) -> str:
    """
    Repair malformed Unicode text returned by the API.
    """

    if not text:
        return ""

    return fix_text(text)


def clean_text(text: str) -> str:
    """
    Clean and normalize text.
    """

    if not text:
        return ""

    # Fix encoding issues
    text = fix_encoding(text)

    # Normalize newlines
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # Replace tabs with spaces
    text = text.replace("\t", "    ")

    # Remove trailing spaces
    text = "\n".join(line.rstrip() for line in text.split("\n"))

    # Collapse multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def clean_text_list(items: list[str] | None) -> list[str]:
    """
    Clean every string in a list.
    Remove duplicates while preserving order.
    """

    if not items:
        return []

    cleaned = []
    seen = set()

    for item in items:
        item = clean_text(item)

        if not item:
            continue

        if item in seen:
            continue

        seen.add(item)
        cleaned.append(item)

    return cleaned
