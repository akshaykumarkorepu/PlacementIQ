"""
Knowledge Engine - Evidence Module

Responsible for providing supporting interview records for
Knowledge Engine responses.

This module enables traceable and evidence-backed answers.
"""

from placementiq.common.logger import logger
from placementiq.knowledge.retrieval import RetrievalService


class EvidenceService:
    """
    Retrieves supporting interview evidence using
    the RetrievalService.
    """

    def __init__(self, retrieval_service: RetrievalService):
        """
        Initialize the EvidenceService.

        Args:
            retrieval_service:
                RetrievalService instance used to
                access structured interview data.
        """

        self.retrieval_service = retrieval_service

    def get_coding_evidence(
        self,
        company: str,
        keyword: str,
    ) -> list[dict]:
        """
        Retrieve coding interview evidence for a given
        company using a keyword.

        The keyword is matched against the coding
        question title, topic, and tags.

        Returns the complete matching coding question
        records as supporting evidence.

        Args:
            company:
                Name of the company.

            keyword:
                Search keyword.

        Returns:
            List of matching coding question dictionaries.
            Returns an empty list if the company name,
            keyword, or matching records do not exist.
        """

        cleaned_company = company.strip()
        cleaned_keyword = keyword.strip().lower()

        if not cleaned_company:
            logger.info("Skipping evidence retrieval: empty company name provided.")
            return []

        if not cleaned_keyword:
            logger.info("Skipping evidence retrieval: empty keyword provided.")
            return []

        logger.info(
            "Retrieving coding evidence for company: %s using keyword: %s",
            cleaned_company,
            cleaned_keyword,
        )

        coding_questions = self.retrieval_service.get_coding_questions(
            cleaned_company,
        )

        evidence: list[dict] = []

        for question in coding_questions:
            title = (question.get("title") or "").lower()
            topic = (question.get("topic") or "").lower()
            concepts = str(question.get("concepts") or "").lower()
            tags = str(question.get("tags") or "").lower()
            text = (question.get("evidence") or "").lower()

            if (
                cleaned_keyword in title
                or cleaned_keyword in topic
                or cleaned_keyword in concepts
                or cleaned_keyword in tags
                or cleaned_keyword in text
            ):
                evidence.append(question)

        logger.info(
            "Found %d coding evidence record(s).",
            len(evidence),
        )

        if evidence:
            logger.debug(
                "Evidence record fields: %s",
                list(evidence[0].keys()),
            )

        return evidence

    def get_subject_evidence(
        self,
        company: str,
        keyword: str,
    ) -> list[dict]:
        """
        Retrieve subject interview evidence for a given
        company using a keyword.

        The keyword is matched against the subject
        name, question text, and evidence.

        Returns the complete matching subject question
        records as supporting evidence.

        Args:
            company:
                Name of the company.

            keyword:
                Search keyword.

        Returns:
            List of matching subject question dictionaries.
            Returns an empty list if the company name,
            keyword, or matching records do not exist.
        """

        cleaned_company = company.strip()
        cleaned_keyword = keyword.strip().lower()

        if not cleaned_company:
            logger.info("Skipping evidence retrieval: empty company name provided.")
            return []

        if not cleaned_keyword:
            logger.info("Skipping evidence retrieval: empty keyword provided.")
            return []

        logger.info(
            "Retrieving subject evidence for company: %s using keyword: %s",
            cleaned_company,
            cleaned_keyword,
        )

        subject_questions = self.retrieval_service.get_subject_questions(
            cleaned_company,
        )

        evidence: list[dict] = []

        for question in subject_questions:
            subject = (question.get("subject") or "").lower()
            text = (question.get("question") or "").lower()
            round_label = (question.get("round") or "").lower()
            quote = (question.get("evidence") or "").lower()

            if (
                cleaned_keyword in subject
                or cleaned_keyword in text
                or cleaned_keyword in round_label
                or cleaned_keyword in quote
            ):
                evidence.append(question)

        logger.info(
            "Found %d subject evidence record(s).",
            len(evidence),
        )

        if evidence:
            logger.debug(
                "Evidence record fields: %s",
                list(evidence[0].keys()),
            )

        return evidence

    def get_sql_evidence(
        self,
        company: str,
        keyword: str,
    ) -> list[dict]:
        """
        Retrieve SQL interview evidence for a given
        company using a keyword.

        The keyword is matched against the SQL
        question text and evidence.

        Returns the complete matching SQL question
        records as supporting evidence.

        Args:
            company:
                Name of the company.

            keyword:
                Search keyword.

        Returns:
            List of matching SQL question dictionaries.
            Returns an empty list if the company name,
            keyword, or matching records do not exist.
        """

        cleaned_company = company.strip()
        cleaned_keyword = keyword.strip().lower()

        if not cleaned_company:
            logger.info("Skipping evidence retrieval: empty company name provided.")
            return []

        if not cleaned_keyword:
            logger.info("Skipping evidence retrieval: empty keyword provided.")
            return []

        logger.info(
            "Retrieving SQL evidence for company: %s using keyword: %s",
            cleaned_company,
            cleaned_keyword,
        )

        sql_questions = self.retrieval_service.get_sql_questions(
            cleaned_company,
        )

        evidence: list[dict] = []

        for question in sql_questions:
            text = (question.get("question") or "").lower()
            round_label = (question.get("round") or "").lower()
            quote = (question.get("evidence") or "").lower()

            if (
                cleaned_keyword in text
                or cleaned_keyword in round_label
                or cleaned_keyword in quote
            ):
                evidence.append(question)

        logger.info(
            "Found %d SQL evidence record(s).",
            len(evidence),
        )

        if evidence:
            logger.debug(
                "Evidence record fields: %s",
                list(evidence[0].keys()),
            )

        return evidence

    def get_hr_evidence(
        self,
        company: str,
        keyword: str,
    ) -> list[dict]:
        """
        Retrieve HR interview evidence for a given
        company using a keyword.

        The keyword is matched against the HR
        question text, type, and evidence.

        Returns the complete matching HR question
        records as supporting evidence.

        Args:
            company:
                Name of the company.

            keyword:
                Search keyword.

        Returns:
            List of matching HR question dictionaries.
            Returns an empty list if the company name,
            keyword, or matching records do not exist.
        """

        cleaned_company = company.strip()
        cleaned_keyword = keyword.strip().lower()

        if not cleaned_company:
            logger.info("Skipping evidence retrieval: empty company name provided.")
            return []

        if not cleaned_keyword:
            logger.info("Skipping evidence retrieval: empty keyword provided.")
            return []

        logger.info(
            "Retrieving HR evidence for company: %s using keyword: %s",
            cleaned_company,
            cleaned_keyword,
        )

        hr_questions = self.retrieval_service.get_hr_questions(
            cleaned_company,
        )

        evidence: list[dict] = []

        for question in hr_questions:
            text = (question.get("question") or "").lower()
            question_type = (question.get("type") or "").lower()
            round_label = (question.get("round") or "").lower()
            quote = (question.get("evidence") or "").lower()

            if (
                cleaned_keyword in text
                or cleaned_keyword in question_type
                or cleaned_keyword in round_label
                or cleaned_keyword in quote
            ):
                evidence.append(question)

        logger.info(
            "Found %d HR evidence record(s).",
            len(evidence),
        )

        if evidence:
            logger.debug(
                "Evidence record fields: %s",
                list(evidence[0].keys()),
            )

        return evidence

    def get_round_evidence(
        self,
        company: str,
        keyword: str,
    ) -> list[dict]:
        """
        Retrieve interview round evidence for a given
        company using a keyword.

        The keyword is matched against the round
        name, round type, and round summary.

        Returns the complete matching interview round
        records as supporting evidence.

        Args:
            company:
                Name of the company.

            keyword:
                Search keyword.

        Returns:
            List of matching interview round dictionaries.
            Returns an empty list if the company name,
            keyword, or matching records do not exist.
        """

        cleaned_company = company.strip()
        cleaned_keyword = keyword.strip().lower()

        if not cleaned_company:
            logger.info("Skipping evidence retrieval: empty company name provided.")
            return []

        if not cleaned_keyword:
            logger.info("Skipping evidence retrieval: empty keyword provided.")
            return []

        logger.info(
            "Retrieving interview round evidence for company: %s using keyword: %s",
            cleaned_company,
            cleaned_keyword,
        )

        rounds = self.retrieval_service.get_rounds(cleaned_company)

        evidence: list[dict] = []

        for round_data in rounds:
            round_name = (round_data.get("round_name") or "").lower()
            round_type = (round_data.get("round_type") or "").lower()
            difficulty = (round_data.get("difficulty") or "").lower()
            summary = (round_data.get("summary") or "").lower()

            if (
                cleaned_keyword in round_name
                or cleaned_keyword in round_type
                or cleaned_keyword in difficulty
                or cleaned_keyword in summary
            ):
                evidence.append(round_data)

        logger.info(
            "Found %d interview round evidence record(s).",
            len(evidence),
        )

        if evidence:
            logger.debug(
                "Evidence record fields: %s",
                list(evidence[0].keys()),
            )

        return evidence

    def get_puzzle_evidence(
        self,
        company: str,
        keyword: str,
    ) -> list[dict]:
        """
        Retrieve puzzle interview evidence for a given
        company using a keyword.

        The keyword is matched against the puzzle
        title and difficulty.

        Returns the complete matching puzzle records
        as supporting evidence.

        Args:
            company:
                Name of the company.

            keyword:
                Search keyword.

        Returns:
            List of matching puzzle dictionaries.
            Returns an empty list if the company name,
            keyword, or matching records do not exist.
        """

        cleaned_company = company.strip()
        cleaned_keyword = keyword.strip().lower()

        if not cleaned_company:
            logger.info("Skipping evidence retrieval: empty company name provided.")
            return []

        if not cleaned_keyword:
            logger.info("Skipping evidence retrieval: empty keyword provided.")
            return []

        logger.info(
            "Retrieving puzzle evidence for company: %s using keyword: %s",
            cleaned_company,
            cleaned_keyword,
        )

        puzzles = self.retrieval_service.get_puzzles(cleaned_company)

        evidence: list[dict] = []

        for puzzle in puzzles:
            title = (puzzle.get("title") or "").lower()
            difficulty = (puzzle.get("difficulty") or "").lower()
            round_label = (puzzle.get("round") or "").lower()
            quote = (puzzle.get("evidence") or "").lower()

            if (
                cleaned_keyword in title
                or cleaned_keyword in difficulty
                or cleaned_keyword in round_label
                or cleaned_keyword in quote
            ):
                evidence.append(puzzle)

        logger.info(
            "Found %d puzzle evidence record(s).",
            len(evidence),
        )

        if evidence:
            logger.debug(
                "Evidence record fields: %s",
                list(evidence[0].keys()),
            )

        return evidence
