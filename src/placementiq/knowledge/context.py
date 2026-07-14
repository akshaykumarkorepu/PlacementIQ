"""
Knowledge Engine - Context Module

Responsible for generating dataset context
for Knowledge Engine responses.

This module helps communicate the amount
of available interview data behind an answer.
"""

from placementiq.common.logger import logger
from placementiq.knowledge.analytics import AnalyticsService


class ContextService:
    """
    Generates dataset context using
    the AnalyticsService.
    """

    def __init__(self, analytics_service: AnalyticsService):
        """
        Initialize the ContextService.

        Args:
            analytics_service:
                AnalyticsService instance used to
                access interview analytics.
        """

        self.analytics_service = analytics_service

    def get_company_context(
        self,
        company: str,
    ) -> dict:
        """
        Generate dataset context for a given company.

        The returned context explains how much interview
        data is available for the company. This helps
        users understand the breadth of the available
        dataset without implying correctness.

        Args:
            company:
                Name of the company.

        Returns:
            Dictionary containing company statistics
            and a natural language dataset context.
            Returns an empty dictionary if the company
            name is empty.
        """

        cleaned_company = company.strip()

        if not cleaned_company:
            logger.info("Skipping context generation: empty company name provided.")
            return {}

        logger.info(
            "Generating dataset context for company: %s",
            cleaned_company,
        )

        summary = self.analytics_service.get_company_summary(
            cleaned_company,
        )

        total_experiences = summary.get(
            "total_experiences",
            0,
        )

        coding_questions = summary.get(
            "coding_questions",
            0,
        )

        if total_experiences == 0:
            context = (
                f"We currently do not have any "
                f"{cleaned_company} interview experiences "
                f"in the dataset. Therefore, PlacementIQ "
                f"cannot determine interview patterns for "
                f"this company at this time."
            )

        elif total_experiences == 1:
            context = (
                f"This answer is based on the only "
                f"available {cleaned_company} interview "
                f"experience in our dataset. The observations "
                f"should therefore be interpreted as the "
                f"current dataset rather than a definitive "
                f"interview pattern."
            )

        else:
            context = (
                f"This answer is based on "
                f"{total_experiences} interview experiences "
                f"and {coding_questions} coding questions "
                f"collected for {cleaned_company}."
            )

        logger.info(
            "Generated dataset context for company: %s",
            cleaned_company,
        )

        return {
            "company": cleaned_company,
            "total_experiences": total_experiences,
            "coding_questions": coding_questions,
            "context": context,
        }

    def get_topic_context(
        self,
        company: str,
        topic: str,
    ) -> dict:
        """
        Generate dataset context for a specific coding
        topic at a given company.

        The returned context reports how many coding
        questions observed the requested topic, or
        states that the topic was not observed in the
        available dataset.

        Args:
            company:
                Name of the company.

            topic:
                Name of the coding topic.

        Returns:
            Dictionary containing company statistics,
            the topic frequency, and a natural language
            dataset context. Returns an empty dictionary
            if the company or topic name is empty.
        """

        cleaned_company = company.strip()
        cleaned_topic = topic.strip()

        if not cleaned_company:
            logger.info("Skipping context generation: empty company name provided.")
            return {}

        if not cleaned_topic:
            logger.info("Skipping context generation: empty topic name provided.")
            return {}

        logger.info(
            "Generating topic context for company: %s and topic: %s",
            cleaned_company,
            cleaned_topic,
        )

        summary = self.analytics_service.get_company_summary(
            cleaned_company,
        )

        total_experiences = summary.get(
            "total_experiences",
            0,
        )

        topic_frequency = summary.get(
            "topic_frequency",
            {},
        )

        topic_count = 0
        for existing_topic, count in topic_frequency.items():
            if existing_topic.lower() == cleaned_topic.lower():
                topic_count = count
                break

        if total_experiences == 0:
            context = (
                f"We currently do not have any "
                f"{cleaned_company} interview experiences "
                f"in the dataset. Therefore, PlacementIQ "
                f"cannot determine interview patterns for "
                f"this company at this time."
            )

        elif topic_count == 0:
            context = (
                f"No {cleaned_topic} questions were reported "
                f"in the available {cleaned_company} interview "
                f"experiences."
            )

        else:
            context = (
                f"{cleaned_topic} was reported in "
                f"{topic_count} coding "
                f"{'question' if topic_count == 1 else 'questions'} "
                f"across {total_experiences} {cleaned_company} "
                f"interview experiences."
            )

        logger.info(
            "Generated topic context for company: %s and topic: %s",
            cleaned_company,
            cleaned_topic,
        )

        return {
            "company": cleaned_company,
            "topic": cleaned_topic,
            "total_experiences": total_experiences,
            "topic_count": topic_count,
            "context": context,
        }

    def get_subject_context(
        self,
        company: str,
        subject: str,
    ) -> dict:
        """
        Generate dataset context for a specific subject
        at a given company.

        The returned context reports the number of
        subject questions available for the company.

        Args:
            company:
                Name of the company.

            subject:
                Name of the subject area.

        Returns:
            Dictionary containing company statistics,
            subject question count, and a natural
            language dataset context. Returns an empty
            dictionary if the company or subject name
            is empty.
        """

        cleaned_company = company.strip()
        cleaned_subject = subject.strip()

        if not cleaned_company:
            logger.info("Skipping context generation: empty company name provided.")
            return {}

        if not cleaned_subject:
            logger.info("Skipping context generation: empty subject name provided.")
            return {}

        logger.info(
            "Generating subject context for company: %s and subject: %s",
            cleaned_company,
            cleaned_subject,
        )

        summary = self.analytics_service.get_company_summary(
            cleaned_company,
        )

        total_experiences = summary.get(
            "total_experiences",
            0,
        )

        subject_questions = summary.get(
            "subject_questions",
            0,
        )

        if total_experiences == 0:
            context = (
                f"We currently do not have any "
                f"{cleaned_company} interview experiences "
                f"in the dataset. Therefore, PlacementIQ "
                f"cannot determine interview patterns for "
                f"this company at this time."
            )

        else:
            context = (
                f"This answer is based on "
                f"{subject_questions} subject "
                f"{'question' if subject_questions == 1 else 'questions'} "
                f"reported across {total_experiences} "
                f"{cleaned_company} interview experiences."
            )

        logger.info(
            "Generated subject context for company: %s and subject: %s",
            cleaned_company,
            cleaned_subject,
        )

        return {
            "company": cleaned_company,
            "subject": cleaned_subject,
            "total_experiences": total_experiences,
            "subject_questions": subject_questions,
            "context": context,
        }

    def get_sql_context(
        self,
        company: str,
    ) -> dict:
        """
        Generate dataset context for SQL questions
        at a given company.

        The returned context reports the number of
        SQL questions available for the company.

        Args:
            company:
                Name of the company.

        Returns:
            Dictionary containing company statistics,
            SQL question count, and a natural language
            dataset context. Returns an empty dictionary
            if the company name is empty.
        """

        cleaned_company = company.strip()

        if not cleaned_company:
            logger.info("Skipping context generation: empty company name provided.")
            return {}

        logger.info(
            "Generating SQL context for company: %s",
            cleaned_company,
        )

        summary = self.analytics_service.get_company_summary(
            cleaned_company,
        )

        total_experiences = summary.get(
            "total_experiences",
            0,
        )

        sql_questions = summary.get(
            "sql_questions",
            0,
        )

        if total_experiences == 0:
            context = (
                f"We currently do not have any "
                f"{cleaned_company} interview experiences "
                f"in the dataset. Therefore, PlacementIQ "
                f"cannot determine interview patterns for "
                f"this company at this time."
            )

        else:
            context = (
                f"This answer is based on "
                f"{sql_questions} SQL "
                f"{'question' if sql_questions == 1 else 'questions'} "
                f"reported across {total_experiences} "
                f"{cleaned_company} interview experiences."
            )

        logger.info(
            "Generated SQL context for company: %s",
            cleaned_company,
        )

        return {
            "company": cleaned_company,
            "total_experiences": total_experiences,
            "sql_questions": sql_questions,
            "context": context,
        }

    def get_hr_context(
        self,
        company: str,
    ) -> dict:
        """
        Generate dataset context for HR questions
        at a given company.

        The returned context reports the number of
        HR questions available for the company.

        Args:
            company:
                Name of the company.

        Returns:
            Dictionary containing company statistics,
            HR question count, and a natural language
            dataset context. Returns an empty dictionary
            if the company name is empty.
        """

        cleaned_company = company.strip()

        if not cleaned_company:
            logger.info("Skipping context generation: empty company name provided.")
            return {}

        logger.info(
            "Generating HR context for company: %s",
            cleaned_company,
        )

        summary = self.analytics_service.get_company_summary(
            cleaned_company,
        )

        total_experiences = summary.get(
            "total_experiences",
            0,
        )

        hr_questions = summary.get(
            "hr_questions",
            0,
        )

        if total_experiences == 0:
            context = (
                f"We currently do not have any "
                f"{cleaned_company} interview experiences "
                f"in the dataset. Therefore, PlacementIQ "
                f"cannot determine interview patterns for "
                f"this company at this time."
            )

        else:
            context = (
                f"This answer is based on "
                f"{hr_questions} HR "
                f"{'question' if hr_questions == 1 else 'questions'} "
                f"reported across {total_experiences} "
                f"{cleaned_company} interview experiences."
            )

        logger.info(
            "Generated HR context for company: %s",
            cleaned_company,
        )

        return {
            "company": cleaned_company,
            "total_experiences": total_experiences,
            "hr_questions": hr_questions,
            "context": context,
        }

    def get_round_context(
        self,
        company: str,
    ) -> dict:
        """
        Generate dataset context for interview rounds
        at a given company.

        The returned context reports the number of
        interview rounds available for the company.

        Args:
            company:
                Name of the company.

        Returns:
            Dictionary containing company statistics,
            interview round count, and a natural language
            dataset context. Returns an empty dictionary
            if the company name is empty.
        """

        cleaned_company = company.strip()

        if not cleaned_company:
            logger.info("Skipping context generation: empty company name provided.")
            return {}

        logger.info(
            "Generating interview round context for company: %s",
            cleaned_company,
        )

        summary = self.analytics_service.get_company_summary(
            cleaned_company,
        )

        total_experiences = summary.get(
            "total_experiences",
            0,
        )

        interview_rounds = summary.get(
            "interview_rounds",
            0,
        )

        if total_experiences == 0:
            context = (
                f"We currently do not have any "
                f"{cleaned_company} interview experiences "
                f"in the dataset. Therefore, PlacementIQ "
                f"cannot determine interview patterns for "
                f"this company at this time."
            )

        else:
            context = (
                f"This answer summarizes "
                f"{interview_rounds} interview "
                f"{'round' if interview_rounds == 1 else 'rounds'} "
                f"reported across {total_experiences} "
                f"{cleaned_company} interview experiences."
            )

        logger.info(
            "Generated interview round context for company: %s",
            cleaned_company,
        )

        return {
            "company": cleaned_company,
            "total_experiences": total_experiences,
            "interview_rounds": interview_rounds,
            "context": context,
        }
