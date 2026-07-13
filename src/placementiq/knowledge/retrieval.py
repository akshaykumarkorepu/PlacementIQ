"""
Knowledge Engine - Retrieval Module

Responsible for retrieving structured interview data from the
repository layer.

This module serves as the foundation of the Knowledge Engine.
"""

from placementiq.common.logger import logger
from placementiq.repository.knowledge_repository import KnowledgeRepository


class RetrievalService:
    """
    Provides read-only retrieval of structured interview
    data through the KnowledgeRepository.
    """

    def __init__(self, repository: KnowledgeRepository):
        """
        Initialize the service with a KnowledgeRepository.

        Args:
            repository:
                KnowledgeRepository instance used to read
                structured experiences from the database.
        """

        self.repository = repository

    def get_company_experiences(self, company: str) -> list[dict]:
        """
        Retrieve all structured experiences for a given company.

        Args:
            company:
                Name of the company whose experiences are fetched.

        Returns:
            A list of structured experience dictionaries.
            Returns an empty list if the company name is empty
            or no records exist.
        """

        cleaned_company = company.strip()

        if not cleaned_company:
            logger.info(
                "Skipping retrieval: empty company name provided."
            )
            return []

        logger.info(
            "Retrieving structured experiences for company: %s",
            cleaned_company,
        )

        return self.repository.get_company_experiences(cleaned_company)

    def get_coding_questions(self, company: str) -> list[dict]:
        """
        Retrieve all coding questions for a given company.

        Args:
            company:
                Name of the company whose coding questions are fetched.

        Returns:
            A list of coding question dictionaries.
            Returns an empty list if the company name is empty
            or no records exist.
        """

        cleaned_company = company.strip()

        if not cleaned_company:
            logger.info(
                "Skipping retrieval: empty company name provided."
            )
            return []

        logger.info(
            "Retrieving coding questions for company: %s",
            cleaned_company,
        )

        return self.repository.get_coding_questions(cleaned_company)

    def get_subject_questions(self, company: str) -> list[dict]:
        """
        Retrieve all subject questions for a given company.

        Args:
            company:
                Name of the company whose subject questions are fetched.

        Returns:
            A list of subject question dictionaries.
            Returns an empty list if the company name is empty
            or no records exist.
        """

        cleaned_company = company.strip()

        if not cleaned_company:
            logger.info(
                "Skipping retrieval: empty company name provided."
            )
            return []

        logger.info(
            "Retrieving subject questions for company: %s",
            cleaned_company,
        )

        return self.repository.get_subject_questions(cleaned_company)

    def get_sql_questions(self, company: str) -> list[dict]:
        """
        Retrieve all SQL questions for a given company.

        Args:
            company:
                Name of the company whose SQL questions are fetched.

        Returns:
            A list of SQL question dictionaries.
            Returns an empty list if the company name is empty
            or no records exist.
        """

        cleaned_company = company.strip()

        if not cleaned_company:
            logger.info(
                "Skipping retrieval: empty company name provided."
            )
            return []

        logger.info(
            "Retrieving SQL questions for company: %s",
            cleaned_company,
        )

        return self.repository.get_sql_questions(cleaned_company)

    def get_hr_questions(self, company: str) -> list[dict]:
        """
        Retrieve all HR questions for a given company.

        Args:
            company:
                Name of the company whose HR questions are fetched.

        Returns:
            A list of HR question dictionaries.
            Returns an empty list if the company name is empty
            or no records exist.
        """

        cleaned_company = company.strip()

        if not cleaned_company:
            logger.info(
                "Skipping retrieval: empty company name provided."
            )
            return []

        logger.info(
            "Retrieving HR questions for company: %s",
            cleaned_company,
        )

        return self.repository.get_hr_questions(cleaned_company)

    def get_rounds(self, company: str) -> list[dict]:
        """
        Retrieve all interview rounds for a given company.

        Args:
            company:
                Name of the company whose interview rounds are fetched.

        Returns:
            A list of interview round dictionaries.
            Returns an empty list if the company name is empty
            or no records exist.
        """

        cleaned_company = company.strip()

        if not cleaned_company:
            logger.info(
                "Skipping retrieval: empty company name provided."
            )
            return []

        logger.info(
            "Retrieving interview rounds for company: %s",
            cleaned_company,
        )

        return self.repository.get_rounds(cleaned_company)

    def get_puzzles(self, company: str) -> list[dict]:
        """
        Retrieve all puzzles for a given company.

        Args:
            company:
                Name of the company whose puzzles are fetched.

        Returns:
            A list of puzzle dictionaries.
            Returns an empty list if the company name is empty
            or no records exist.
        """

        cleaned_company = company.strip()

        if not cleaned_company:
            logger.info(
                "Skipping retrieval: empty company name provided."
            )
            return []

        logger.info(
            "Retrieving puzzles for company: %s",
            cleaned_company,
        )

        return self.repository.get_puzzles(cleaned_company)
