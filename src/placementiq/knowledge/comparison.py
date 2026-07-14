"""
Knowledge Engine - Comparison Module

Responsible for comparing interview data across companies,
topics, and other entities.

This module highlights similarities and differences between
datasets.
"""

from placementiq.common.logger import logger
from placementiq.knowledge.analytics import AnalyticsService


class ComparisonService:
    """
    Compares interview analytics across companies
    using the AnalyticsService.
    """

    def __init__(self, analytics_service: AnalyticsService):
        """
        Initialize the ComparisonService.

        Args:
            analytics_service:
                AnalyticsService instance used to
                generate interview analytics.
        """

        self.analytics_service = analytics_service

    def compare_companies(
        self,
        company_1: str,
        company_2: str,
    ) -> dict:
        """
        Compare interview analytics between two companies.

        Args:
            company_1:
                Name of the first company.

            company_2:
                Name of the second company.

        Returns:
            Dictionary containing analytics summaries
            for both companies. Returns an empty
            dictionary if either company name is empty.
        """

        cleaned_company_1 = company_1.strip()
        cleaned_company_2 = company_2.strip()

        if not cleaned_company_1:
            logger.info("Skipping comparison: empty first company name provided.")
            return {}

        if not cleaned_company_2:
            logger.info("Skipping comparison: empty second company name provided.")
            return {}

        logger.info(
            "Comparing companies: %s and %s",
            cleaned_company_1,
            cleaned_company_2,
        )

        company_1_summary = self.analytics_service.get_company_summary(
            cleaned_company_1,
        )

        company_2_summary = self.analytics_service.get_company_summary(
            cleaned_company_2,
        )

        comparison = {
            "company_1": company_1_summary,
            "company_2": company_2_summary,
        }

        logger.info(
            "Completed comparison between %s and %s",
            cleaned_company_1,
            cleaned_company_2,
        )

        return comparison

    def compare_topic_frequency(
        self,
        company_1: str,
        company_2: str,
    ) -> dict:
        """
        Compare coding topic frequency between
        two companies.

        Args:
            company_1:
                Name of the first company.

            company_2:
                Name of the second company.

        Returns:
            Dictionary containing the union of topics
            with counts for each company. Returns an
            empty dictionary if either company name
            is empty.
        """

        cleaned_company_1 = company_1.strip()
        cleaned_company_2 = company_2.strip()

        if not cleaned_company_1:
            logger.info("Skipping comparison: empty first company name provided.")
            return {}

        if not cleaned_company_2:
            logger.info("Skipping comparison: empty second company name provided.")
            return {}

        logger.info(
            "Comparing topic frequency between %s and %s",
            cleaned_company_1,
            cleaned_company_2,
        )

        topics_1 = self.analytics_service.get_topic_frequency(cleaned_company_1)
        topics_2 = self.analytics_service.get_topic_frequency(cleaned_company_2)

        all_topics = set(topics_1.keys()) | set(topics_2.keys())

        comparison: dict = {}

        for topic in all_topics:
            comparison[topic] = {
                cleaned_company_1: topics_1.get(topic, 0),
                cleaned_company_2: topics_2.get(topic, 0),
            }

        logger.info(
            "Completed topic frequency comparison between %s and %s",
            cleaned_company_1,
            cleaned_company_2,
        )

        return {
            "company_1": cleaned_company_1,
            "company_2": cleaned_company_2,
            "comparison": comparison,
        }

    def compare_difficulty_distribution(
        self,
        company_1: str,
        company_2: str,
    ) -> dict:
        """
        Compare coding question difficulty distribution
        between two companies.

        Args:
            company_1:
                Name of the first company.

            company_2:
                Name of the second company.

        Returns:
            Dictionary containing the union of difficulty
            levels with counts for each company. Returns
            an empty dictionary if either company name
            is empty.
        """

        cleaned_company_1 = company_1.strip()
        cleaned_company_2 = company_2.strip()

        if not cleaned_company_1:
            logger.info("Skipping comparison: empty first company name provided.")
            return {}

        if not cleaned_company_2:
            logger.info("Skipping comparison: empty second company name provided.")
            return {}

        logger.info(
            "Comparing difficulty distribution between %s and %s",
            cleaned_company_1,
            cleaned_company_2,
        )

        difficulty_1 = self.analytics_service.get_difficulty_distribution(cleaned_company_1)
        difficulty_2 = self.analytics_service.get_difficulty_distribution(cleaned_company_2)

        all_difficulties = set(difficulty_1.keys()) | set(difficulty_2.keys())

        comparison: dict = {}

        for difficulty in all_difficulties:
            comparison[difficulty] = {
                cleaned_company_1: difficulty_1.get(difficulty, 0),
                cleaned_company_2: difficulty_2.get(difficulty, 0),
            }

        logger.info(
            "Completed difficulty distribution comparison between %s and %s",
            cleaned_company_1,
            cleaned_company_2,
        )

        return {
            "company_1": cleaned_company_1,
            "company_2": cleaned_company_2,
            "comparison": comparison,
        }

    def compare_interview_pattern(
        self,
        company_1: str,
        company_2: str,
    ) -> dict:
        """
        Compare interview round type patterns
        between two companies.

        Args:
            company_1:
                Name of the first company.

            company_2:
                Name of the second company.

        Returns:
            Dictionary containing the union of round
            types with counts for each company. Returns
            an empty dictionary if either company name
            is empty.
        """

        cleaned_company_1 = company_1.strip()
        cleaned_company_2 = company_2.strip()

        if not cleaned_company_1:
            logger.info("Skipping comparison: empty first company name provided.")
            return {}

        if not cleaned_company_2:
            logger.info("Skipping comparison: empty second company name provided.")
            return {}

        logger.info(
            "Comparing interview patterns between %s and %s",
            cleaned_company_1,
            cleaned_company_2,
        )

        rounds_1 = self.analytics_service.get_interview_pattern(cleaned_company_1)
        rounds_2 = self.analytics_service.get_interview_pattern(cleaned_company_2)

        all_round_types = set(rounds_1.keys()) | set(rounds_2.keys())

        comparison: dict = {}

        for round_type in all_round_types:
            comparison[round_type] = {
                cleaned_company_1: rounds_1.get(round_type, 0),
                cleaned_company_2: rounds_2.get(round_type, 0),
            }

        logger.info(
            "Completed interview pattern comparison between %s and %s",
            cleaned_company_1,
            cleaned_company_2,
        )

        return {
            "company_1": cleaned_company_1,
            "company_2": cleaned_company_2,
            "comparison": comparison,
        }

    def compare_hr_patterns(
        self,
        company_1: str,
        company_2: str,
    ) -> dict:
        """
        Compare HR question type patterns between
        two companies.

        Args:
            company_1:
                Name of the first company.

            company_2:
                Name of the second company.

        Returns:
            Dictionary containing the union of HR
            question categories with counts for each
            company. Returns an empty dictionary if
            either company name is empty.
        """

        cleaned_company_1 = company_1.strip()
        cleaned_company_2 = company_2.strip()

        if not cleaned_company_1:
            logger.info("Skipping comparison: empty first company name provided.")
            return {}

        if not cleaned_company_2:
            logger.info("Skipping comparison: empty second company name provided.")
            return {}

        logger.info(
            "Comparing HR patterns between %s and %s",
            cleaned_company_1,
            cleaned_company_2,
        )

        hr_1 = self.analytics_service.get_hr_question_frequency(cleaned_company_1)
        hr_2 = self.analytics_service.get_hr_question_frequency(cleaned_company_2)

        all_hr_categories = set(hr_1.keys()) | set(hr_2.keys())

        comparison: dict = {}

        for category in all_hr_categories:
            comparison[category] = {
                cleaned_company_1: hr_1.get(category, 0),
                cleaned_company_2: hr_2.get(category, 0),
            }

        logger.info(
            "Completed HR pattern comparison between %s and %s",
            cleaned_company_1,
            cleaned_company_2,
        )

        return {
            "company_1": cleaned_company_1,
            "company_2": cleaned_company_2,
            "comparison": comparison,
        }

    def compare_company_strengths(
        self,
        company_1: str,
        company_2: str,
    ) -> dict:
        """
        Compare the analytical strengths of two
        companies.

        Args:
            company_1:
                Name of the first company.

            company_2:
                Name of the second company.

        Returns:
            Dictionary containing the strongest topics
            and dominant categories for each company.
            Returns an empty dictionary if either
            company name is empty.
        """

        cleaned_company_1 = company_1.strip()
        cleaned_company_2 = company_2.strip()

        if not cleaned_company_1:
            logger.info("Skipping comparison: empty first company name provided.")
            return {}

        if not cleaned_company_2:
            logger.info("Skipping comparison: empty second company name provided.")
            return {}

        logger.info(
            "Comparing company strengths between %s and %s",
            cleaned_company_1,
            cleaned_company_2,
        )

        topics_1 = self.analytics_service.get_topic_frequency(cleaned_company_1)
        difficulty_1 = self.analytics_service.get_difficulty_distribution(cleaned_company_1)
        rounds_1 = self.analytics_service.get_interview_pattern(cleaned_company_1)
        hr_1 = self.analytics_service.get_hr_question_frequency(cleaned_company_1)

        topics_2 = self.analytics_service.get_topic_frequency(cleaned_company_2)
        difficulty_2 = self.analytics_service.get_difficulty_distribution(cleaned_company_2)
        rounds_2 = self.analytics_service.get_interview_pattern(cleaned_company_2)
        hr_2 = self.analytics_service.get_hr_question_frequency(cleaned_company_2)

        ranked_topics_1 = sorted(
            topics_1.items(),
            key=lambda item: item[1],
            reverse=True,
        )
        strongest_topics_1: dict = dict(ranked_topics_1[:5])

        ranked_topics_2 = sorted(
            topics_2.items(),
            key=lambda item: item[1],
            reverse=True,
        )
        strongest_topics_2: dict = dict(ranked_topics_2[:5])

        dominant_difficulty_1 = (
            max(difficulty_1, key=difficulty_1.get) if difficulty_1 else None
        )
        dominant_difficulty_2 = (
            max(difficulty_2, key=difficulty_2.get) if difficulty_2 else None
        )

        most_common_round_1 = (
            max(rounds_1, key=rounds_1.get) if rounds_1 else None
        )
        most_common_round_2 = (
            max(rounds_2, key=rounds_2.get) if rounds_2 else None
        )

        most_common_hr_1 = (
            max(hr_1, key=hr_1.get) if hr_1 else None
        )
        most_common_hr_2 = (
            max(hr_2, key=hr_2.get) if hr_2 else None
        )

        strengths_1 = {
            "company": cleaned_company_1,
            "strongest_topics": strongest_topics_1,
            "dominant_difficulty": dominant_difficulty_1,
            "most_common_round": most_common_round_1,
            "most_common_hr_category": most_common_hr_1,
        }

        strengths_2 = {
            "company": cleaned_company_2,
            "strongest_topics": strongest_topics_2,
            "dominant_difficulty": dominant_difficulty_2,
            "most_common_round": most_common_round_2,
            "most_common_hr_category": most_common_hr_2,
        }

        comparison = {
            "company_1": strengths_1,
            "company_2": strengths_2,
        }

        logger.info(
            "Completed company strength comparison between %s and %s",
            cleaned_company_1,
            cleaned_company_2,
        )

        return comparison
