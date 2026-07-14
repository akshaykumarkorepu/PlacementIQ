"""
Knowledge Engine - Search Module

Responsible for searching structured interview data based
on user queries.

This module locates relevant information across the knowledge base.
"""

from placementiq.common.logger import logger
from placementiq.knowledge.retrieval import RetrievalService


class SearchService:
    """
    Provides search functionality over structured
    interview data using the RetrievalService.
    """

    def __init__(self, retrieval_service: RetrievalService):
        """
        Initialize the SearchService.

        Args:
            retrieval_service:
                RetrievalService instance used to
                access structured interview data.
        """

        self.retrieval_service = retrieval_service

    def search_coding_questions(
        self,
        company: str,
        keyword: str,
    ) -> list[dict]:
        """
        Search coding questions for a given company
        using a keyword.

        The keyword is matched against the question
        title, topic, and tags.

        Args:
            company:
                Name of the company.

            keyword:
                Search keyword.

        Returns:
            List of matching coding question dictionaries.
            Returns an empty list if the company name,
            keyword, or matching results do not exist.
        """

        cleaned_company = company.strip()
        cleaned_keyword = keyword.strip().lower()

        if not cleaned_company:
            logger.info("Skipping search: empty company name provided.")
            return []

        if not cleaned_keyword:
            logger.info("Skipping search: empty keyword provided.")
            return []

        logger.info(
            "Searching coding questions for company: %s using keyword: %s",
            cleaned_company,
            cleaned_keyword,
        )

        coding_questions = self.retrieval_service.get_coding_questions(cleaned_company)

        matching_questions: list[dict] = []

        for question in coding_questions:
            title = (question.get("title") or "").lower()
            topic = (question.get("topic") or "").lower()
            tags = (question.get("tags") or "").lower()

            if (
                cleaned_keyword in title
                or cleaned_keyword in topic
                or cleaned_keyword in tags
            ):
                matching_questions.append(question)

        logger.info(
            "Found %d matching coding question(s).",
            len(matching_questions),
        )

        return matching_questions

    def search_subject_questions(
        self,
        company: str,
        keyword: str,
    ) -> list[dict]:
        """
        Search subject questions for a given company
        using a keyword.

        The keyword is matched against the question
        subject and question text.

        Args:
            company:
                Name of the company.

            keyword:
                Search keyword.

        Returns:
            List of matching subject question dictionaries.
            Returns an empty list if the company name,
            keyword, or matching results do not exist.
        """

        cleaned_company = company.strip()
        cleaned_keyword = keyword.strip().lower()

        if not cleaned_company:
            logger.info("Skipping search: empty company name provided.")
            return []

        if not cleaned_keyword:
            logger.info("Skipping search: empty keyword provided.")
            return []

        logger.info(
            "Searching subject questions for company: %s using keyword: %s",
            cleaned_company,
            cleaned_keyword,
        )

        subject_questions = self.retrieval_service.get_subject_questions(cleaned_company)

        matching_questions: list[dict] = []

        for question in subject_questions:
            subject = (question.get("subject") or "").lower()
            text = (question.get("question") or "").lower()

            if (
                cleaned_keyword in subject
                or cleaned_keyword in text
            ):
                matching_questions.append(question)

        logger.info(
            "Found %d matching subject question(s).",
            len(matching_questions),
        )

        return matching_questions

    def search_sql_questions(
        self,
        company: str,
        keyword: str,
    ) -> list[dict]:
        """
        Search SQL questions for a given company
        using a keyword.

        The keyword is matched against the question
        text.

        Args:
            company:
                Name of the company.

            keyword:
                Search keyword.

        Returns:
            List of matching SQL question dictionaries.
            Returns an empty list if the company name,
            keyword, or matching results do not exist.
        """

        cleaned_company = company.strip()
        cleaned_keyword = keyword.strip().lower()

        if not cleaned_company:
            logger.info("Skipping search: empty company name provided.")
            return []

        if not cleaned_keyword:
            logger.info("Skipping search: empty keyword provided.")
            return []

        logger.info(
            "Searching SQL questions for company: %s using keyword: %s",
            cleaned_company,
            cleaned_keyword,
        )

        sql_questions = self.retrieval_service.get_sql_questions(cleaned_company)

        matching_questions: list[dict] = []

        for question in sql_questions:
            text = (question.get("question") or "").lower()

            if cleaned_keyword in text:
                matching_questions.append(question)

        logger.info(
            "Found %d matching SQL question(s).",
            len(matching_questions),
        )

        return matching_questions

    def search_hr_questions(
        self,
        company: str,
        keyword: str,
    ) -> list[dict]:
        """
        Search HR questions for a given company
        using a keyword.

        The keyword is matched against the question
        text and type.

        Args:
            company:
                Name of the company.

            keyword:
                Search keyword.

        Returns:
            List of matching HR question dictionaries.
            Returns an empty list if the company name,
            keyword, or matching results do not exist.
        """

        cleaned_company = company.strip()
        cleaned_keyword = keyword.strip().lower()

        if not cleaned_company:
            logger.info("Skipping search: empty company name provided.")
            return []

        if not cleaned_keyword:
            logger.info("Skipping search: empty keyword provided.")
            return []

        logger.info(
            "Searching HR questions for company: %s using keyword: %s",
            cleaned_company,
            cleaned_keyword,
        )

        hr_questions = self.retrieval_service.get_hr_questions(cleaned_company)

        matching_questions: list[dict] = []

        for question in hr_questions:
            text = (question.get("question") or "").lower()
            question_type = (question.get("type") or "").lower()

            if (
                cleaned_keyword in text
                or cleaned_keyword in question_type
            ):
                matching_questions.append(question)

        logger.info(
            "Found %d matching HR question(s).",
            len(matching_questions),
        )

        return matching_questions

    def search_rounds(
        self,
        company: str,
        keyword: str,
    ) -> list[dict]:
        """
        Search interview rounds for a given company
        using a keyword.

        The keyword is matched against the round name,
        round type, and summary.

        Args:
            company:
                Name of the company.

            keyword:
                Search keyword.

        Returns:
            List of matching interview round dictionaries.
            Returns an empty list if the company name,
            keyword, or matching results do not exist.
        """

        cleaned_company = company.strip()
        cleaned_keyword = keyword.strip().lower()

        if not cleaned_company:
            logger.info("Skipping search: empty company name provided.")
            return []

        if not cleaned_keyword:
            logger.info("Skipping search: empty keyword provided.")
            return []

        logger.info(
            "Searching interview rounds for company: %s using keyword: %s",
            cleaned_company,
            cleaned_keyword,
        )

        rounds = self.retrieval_service.get_rounds(cleaned_company)

        matching_rounds: list[dict] = []

        for round_data in rounds:
            round_name = (round_data.get("round_name") or "").lower()
            round_type = (round_data.get("round_type") or "").lower()
            summary = (round_data.get("summary") or "").lower()

            if (
                cleaned_keyword in round_name
                or cleaned_keyword in round_type
                or cleaned_keyword in summary
            ):
                matching_rounds.append(round_data)

        logger.info(
            "Found %d matching interview round(s).",
            len(matching_rounds),
        )

        return matching_rounds

    def search_puzzles(
        self,
        company: str,
        keyword: str,
    ) -> list[dict]:
        """
        Search puzzles for a given company using
        a keyword.

        The keyword is matched against the puzzle
        title and difficulty.

        Args:
            company:
                Name of the company.

            keyword:
                Search keyword.

        Returns:
            List of matching puzzle dictionaries.
            Returns an empty list if the company name,
            keyword, or matching results do not exist.
        """

        cleaned_company = company.strip()
        cleaned_keyword = keyword.strip().lower()

        if not cleaned_company:
            logger.info("Skipping search: empty company name provided.")
            return []

        if not cleaned_keyword:
            logger.info("Skipping search: empty keyword provided.")
            return []

        logger.info(
            "Searching puzzles for company: %s using keyword: %s",
            cleaned_company,
            cleaned_keyword,
        )

        puzzles = self.retrieval_service.get_puzzles(cleaned_company)

        matching_puzzles: list[dict] = []

        for puzzle in puzzles:
            title = (puzzle.get("title") or "").lower()
            difficulty = (puzzle.get("difficulty") or "").lower()

            if (
                cleaned_keyword in title
                or cleaned_keyword in difficulty
            ):
                matching_puzzles.append(puzzle)

        logger.info(
            "Found %d matching puzzle(s).",
            len(matching_puzzles),
        )

        return matching_puzzles
