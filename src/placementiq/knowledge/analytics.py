"""
Knowledge Engine - Analytics Module

Responsible for computing insights and statistics from
retrieved interview data.

This module transforms raw data into meaningful information.
"""

from placementiq.common.logger import logger
from placementiq.knowledge.retrieval import RetrievalService


class AnalyticsService:
    """
    Generates interview insights using data provided
    by the RetrievalService.
    """

    def __init__(self, retrieval_service: RetrievalService):
        """
        Initialize the AnalyticsService.

        Args:
            retrieval_service:
                RetrievalService instance used to
                access structured interview data.
        """

        self.retrieval_service = retrieval_service

    def get_all_companies(self) -> list[str]:
        """
        Retrieve all companies available in the knowledge base.
        """

        return self.retrieval_service.get_all_companies()

    def get_topic_frequency(self, company: str) -> dict[str, int]:
        """
        Compute the frequency of coding topics
        for a given company.

        Args:
            company:
                Name of the company.

        Returns:
            Dictionary containing topic frequencies.
            Returns an empty dictionary if the
            company name is empty or no topics exist.
        """

        cleaned_company = company.strip()

        if not cleaned_company:
            logger.info("Skipping analytics: empty company name provided.")
            return {}

        logger.info(
            "Computing topic frequency for company: %s",
            cleaned_company,
        )

        coding_questions = self.retrieval_service.get_coding_questions(cleaned_company)

        topic_frequency: dict[str, int] = {}

        for question in coding_questions:
            topic = question.get("topic")

            if not topic:
                continue

            topic_frequency[topic] = topic_frequency.get(topic, 0) + 1

        logger.info(
            "Computed topic frequency for %d topic(s).",
            len(topic_frequency),
        )

        return topic_frequency

    def get_difficulty_distribution(
        self,
        company: str,
    ) -> dict[str, int]:
        """
        Compute the frequency of coding question
        difficulty levels for a given company.

        Args:
            company:
                Name of the company.

        Returns:
            Dictionary containing difficulty frequencies.
            Returns an empty dictionary if the company
            name is empty or no difficulty information
            exists.
        """

        cleaned_company = company.strip()

        if not cleaned_company:
            logger.info("Skipping analytics: empty company name provided.")
            return {}

        logger.info(
            "Computing difficulty distribution for company: %s",
            cleaned_company,
        )

        coding_questions = self.retrieval_service.get_coding_questions(cleaned_company)

        difficulty_distribution: dict[str, int] = {}

        for question in coding_questions:
            difficulty = question.get("difficulty")

            if not difficulty:
                continue

            difficulty_distribution[difficulty] = (
                difficulty_distribution.get(
                    difficulty,
                    0,
                )
                + 1
            )

        logger.info(
            "Computed difficulty distribution for %d difficulty level(s).",
            len(difficulty_distribution),
        )

        return difficulty_distribution

    def get_interview_pattern(self, company: str) -> dict[str, int]:
        """
        Compute the frequency of interview round types
        for a given company.

        Args:
            company:
                Name of the company.

        Returns:
            Dictionary containing round type frequencies.
            Returns an empty dictionary if the company
            name is empty or no round types exist.
        """

        cleaned_company = company.strip()

        if not cleaned_company:
            logger.info("Skipping analytics: empty company name provided.")
            return {}

        logger.info(
            "Computing interview pattern for company: %s",
            cleaned_company,
        )

        rounds = self.retrieval_service.get_rounds(cleaned_company)

        interview_pattern: dict[str, int] = {}

        for round_data in rounds:
            round_type = round_data.get("round_type")

            if not round_type:
                continue

            interview_pattern[round_type] = (
                interview_pattern.get(
                    round_type,
                    0,
                )
                + 1
            )

        logger.info(
            "Computed interview pattern for %d round type(s).",
            len(interview_pattern),
        )

        return interview_pattern

    def get_hr_question_frequency(
        self,
        company: str,
    ) -> dict[str, int]:
        """
        Compute the frequency of HR question types
        for a given company.

        Args:
            company:
                Name of the company.

        Returns:
            Dictionary containing HR question type frequencies.
            Returns an empty dictionary if the company
            name is empty or no HR question types exist.
        """

        cleaned_company = company.strip()

        if not cleaned_company:
            logger.info("Skipping analytics: empty company name provided.")
            return {}

        logger.info(
            "Computing HR question frequency for company: %s",
            cleaned_company,
        )

        hr_questions = self.retrieval_service.get_hr_questions(cleaned_company)

        hr_question_frequency: dict[str, int] = {}

        for question in hr_questions:
            question_type = question.get("type")

            if not question_type:
                continue

            hr_question_frequency[question_type] = (
                hr_question_frequency.get(
                    question_type,
                    0,
                )
                + 1
            )

        logger.info(
            "Computed HR question frequency for %d category(s).",
            len(hr_question_frequency),
        )

        return hr_question_frequency

    def get_company_summary(self, company: str) -> dict:
        """
        Generate a complete analytics summary for a
        given company.

        Args:
            company:
                Name of the company.

        Returns:
            Dictionary containing aggregated analytics
            for the company. Returns an empty dictionary
            if the company name is empty.
        """

        cleaned_company = company.strip()

        if not cleaned_company:
            logger.info("Skipping analytics: empty company name provided.")
            return {}

        logger.info(
            "Computing company summary for company: %s",
            cleaned_company,
        )

        experiences = self.retrieval_service.get_company_experiences(cleaned_company)
        coding_questions = self.retrieval_service.get_coding_questions(cleaned_company)
        subject_questions = self.retrieval_service.get_subject_questions(
            cleaned_company
        )
        sql_questions = self.retrieval_service.get_sql_questions(cleaned_company)
        hr_questions = self.retrieval_service.get_hr_questions(cleaned_company)
        rounds = self.retrieval_service.get_rounds(cleaned_company)
        puzzles = self.retrieval_service.get_puzzles(cleaned_company)

        summary = {
            "company": cleaned_company,
            "total_experiences": len(experiences),
            "coding_questions": len(coding_questions),
            "subject_questions": len(subject_questions),
            "sql_questions": len(sql_questions),
            "hr_questions": len(hr_questions),
            "interview_rounds": len(rounds),
            "puzzles": len(puzzles),
            "topic_frequency": self.get_topic_frequency(cleaned_company),
            "difficulty_distribution": self.get_difficulty_distribution(
                cleaned_company
            ),
            "interview_pattern": self.get_interview_pattern(cleaned_company),
            "hr_question_frequency": self.get_hr_question_frequency(cleaned_company),
        }

        logger.info(
            "Computed company summary for company: %s",
            cleaned_company,
        )

        return summary
