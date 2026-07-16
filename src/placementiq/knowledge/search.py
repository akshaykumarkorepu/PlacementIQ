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

    Supports both company-specific search (when a company
    name is provided) and global search across all
    companies (when no company is provided).
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

    # ======================================================
    # Company-specific search
    # ======================================================

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

    # ======================================================
    # Global search across all companies
    # ======================================================

    def global_search_coding_questions(
        self,
        keyword: str,
    ) -> list[dict]:
        """
        Search coding questions across ALL companies
        using a keyword.

        Args:
            keyword:
                Search keyword.

        Returns:
            List of matching coding question dictionaries.
            Each result includes the company name.
            Returns an empty list if the keyword is empty
            or no records match.
        """

        cleaned_keyword = keyword.strip()

        if not cleaned_keyword:
            logger.info("Skipping global search: empty keyword provided.")
            return []

        logger.info(
            "Globally searching coding questions for keyword: %s",
            cleaned_keyword,
        )

        results = self.retrieval_service.search_coding_questions(cleaned_keyword)

        logger.info(
            "Found %d global matching coding question(s).",
            len(results),
        )

        return results

    def global_search_subject_questions(
        self,
        keyword: str,
    ) -> list[dict]:
        """
        Search subject questions across ALL companies
        using a keyword.

        Args:
            keyword:
                Search keyword.

        Returns:
            List of matching subject question dictionaries.
            Each result includes the company name.
            Returns an empty list if the keyword is empty
            or no records match.
        """

        cleaned_keyword = keyword.strip()

        if not cleaned_keyword:
            logger.info("Skipping global search: empty keyword provided.")
            return []

        logger.info(
            "Globally searching subject questions for keyword: %s",
            cleaned_keyword,
        )

        results = self.retrieval_service.search_subject_questions(cleaned_keyword)

        logger.info(
            "Found %d global matching subject question(s).",
            len(results),
        )

        return results

    def global_search_sql_questions(
        self,
        keyword: str,
    ) -> list[dict]:
        """
        Search SQL questions across ALL companies
        using a keyword.

        Args:
            keyword:
                Search keyword.

        Returns:
            List of matching SQL question dictionaries.
            Each result includes the company name.
            Returns an empty list if the keyword is empty
            or no records match.
        """

        cleaned_keyword = keyword.strip()

        if not cleaned_keyword:
            logger.info("Skipping global search: empty keyword provided.")
            return []

        logger.info(
            "Globally searching SQL questions for keyword: %s",
            cleaned_keyword,
        )

        results = self.retrieval_service.search_sql_questions(cleaned_keyword)

        logger.info(
            "Found %d global matching SQL question(s).",
            len(results),
        )

        return results

    def global_search_hr_questions(
        self,
        keyword: str,
    ) -> list[dict]:
        """
        Search HR questions across ALL companies
        using a keyword.

        Args:
            keyword:
                Search keyword.

        Returns:
            List of matching HR question dictionaries.
            Each result includes the company name.
            Returns an empty list if the keyword is empty
            or no records match.
        """

        cleaned_keyword = keyword.strip()

        if not cleaned_keyword:
            logger.info("Skipping global search: empty keyword provided.")
            return []

        logger.info(
            "Globally searching HR questions for keyword: %s",
            cleaned_keyword,
        )

        results = self.retrieval_service.search_hr_questions(cleaned_keyword)

        logger.info(
            "Found %d global matching HR question(s).",
            len(results),
        )

        return results

    # ======================================================
    # Unified search (company-specific or global)
    # ======================================================

    def search(
        self,
        category: str,
        companies: list[str],
        topics: list[str],
    ) -> dict[str, list[dict]]:
        """
        Unified search entry point.

        If ``companies`` is non-empty, performs a
        company-specific search and groups results
        by company. If ``companies`` is empty, performs
        a global search across all companies and groups
        the matching results by company.

        Args:
            category:
                Search category. One of:
                coding, subject, sql, hr,
                rounds, puzzles.

            companies:
                List of company names. May be empty,
                which triggers a global search.

            topics:
                List of keywords to search for.

        Returns:
            A dictionary mapping company name to a list
            of matching question dictionaries. When the
            company list is empty, the keys are derived
            from each matching result's ``company`` field.
        """

        normalized_companies = [
            company.strip() for company in companies if company and company.strip()
        ]

        normalized_topics = [
            topic.strip() for topic in topics if topic and topic.strip()
        ]

        if not normalized_topics:
            logger.info("Skipping search: no topics provided.")
            return {}

        if not normalized_companies:
            logger.info(
                "Performing global search for category: %s",
                category,
            )
            return self._run_global_search(category, normalized_topics)

        logger.info(
            "Performing company search for companies: %s and category: %s",
            normalized_companies,
            category,
        )
        return self._run_company_search(
            category,
            normalized_companies,
            normalized_topics,
        )

    def _run_company_search(
        self,
        category: str,
        companies: list[str],
        topics: list[str],
    ) -> dict[str, list[dict]]:
        """
        Execute a company-specific search and group
        results by company.
        """

        search_results: dict[str, list[dict]] = {}

        for company in companies:
            company_results: list[dict] = []

            for topic in topics:
                if category == "coding":
                    results = self.search_coding_questions(company, topic)

                elif category == "subject":
                    results = self.search_subject_questions(company, topic)

                elif category == "sql":
                    results = self.search_sql_questions(company, topic)

                elif category == "hr":
                    results = self.search_hr_questions(company, topic)

                elif category == "rounds":
                    results = self.search_rounds(company, topic)

                elif category == "puzzles":
                    results = self.search_puzzles(company, topic)

                else:
                    logger.info(
                        "Unknown search category: %s",
                        category,
                    )
                    continue

                company_results.extend(results)

            search_results[company] = company_results

        return search_results

    def _run_global_search(
        self,
        category: str,
        topics: list[str],
    ) -> dict[str, list[dict]]:
        """
        Execute a global search across all companies
        and group results by company.
        """

        search_results: dict[str, list[dict]] = {}

        for topic in topics:
            if category == "coding":
                matches = self.global_search_coding_questions(topic)

            elif category == "subject":
                matches = self.global_search_subject_questions(topic)

            elif category == "sql":
                matches = self.global_search_sql_questions(topic)

            elif category == "hr":
                matches = self.global_search_hr_questions(topic)

            else:
                logger.info(
                    "Global search is only supported for coding, subject, "
                    "sql, and hr. Skipping category: %s",
                    category,
                )
                continue

            for match in matches:
                company = match.get("company") or "Unknown"

                if company not in search_results:
                    search_results[company] = []

                search_results[company].append(match)

        return search_results
