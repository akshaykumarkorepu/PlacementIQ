"""
PlacementIQ Knowledge Repository

Responsible for read-only access to the structured
experiences stored in the database.
"""

import sqlite3

from placementiq.common.logger import logger


class KnowledgeRepository:
    """
    Handles read operations against the structured
    database for the knowledge layer.
    """

    def __init__(self, database_path: str = "data/placementiq.db"):
        """
        Initialize the repository.

        Args:
            database_path:
                Path to the SQLite database.
        """

        self.database_path = database_path

    def get_company_experiences(self, company: str) -> list[dict]:
        """
        Retrieve all structured experiences for a given company.

        Args:
            company:
                Name of the company whose experiences are fetched.

        Returns:
            A list of dictionaries, one per structured experience.
            Returns an empty list if no records exist.
        """

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        try:
            logger.info(
                "Fetching structured experiences for company: %s",
                company,
            )

            cursor.execute(
                """
                SELECT
                    id,
                    interview_id,
                    company,
                    role,
                    batch,
                    experience_type,
                    result,
                    overall_difficulty,
                    number_of_rounds,
                    oa_platform,
                    summary,
                    technologies,
                    keywords,
                    tips,
                    mistakes,
                    resources,
                    important_concepts,
                    projects_discussed,
                    schema_version,
                    model_used,
                    processed_at
                FROM structured_experiences
                WHERE company = ?
                ORDER BY processed_at DESC
                """,
                (company,),
            )

            rows = cursor.fetchall()

            results = [dict(row) for row in rows]

            logger.info(
                "Found %d structured experience(s) for company: %s",
                len(results),
                company,
            )

            return results

        except Exception:
            logger.exception(
                "Failed to fetch structured experiences for company: %s",
                company,
            )
            raise

        finally:
            connection.close()

    def get_coding_questions(self, company: str) -> list[dict]:
        """
        Retrieve all coding questions for a given company.

        Args:
            company:
                Name of the company whose coding questions are fetched.

        Returns:
            A list of dictionaries, one per coding question.
            Returns an empty list if no records exist.
        """

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        try:
            logger.info(
                "Fetching coding questions for company: %s", company
            )

            cursor.execute(
                """
                SELECT
                    cq.id,
                    cq.structured_experience_id,
                    cq.title,
                    cq.topic,
                    cq.concepts,
                    cq.difficulty,
                    cq.round,
                    cq.platform,
                    cq.tags,
                    cq.evidence
                FROM coding_questions AS cq
                INNER JOIN structured_experiences AS se
                    ON cq.structured_experience_id = se.id
                WHERE se.company = ?
                ORDER BY cq.id
                """,
                (company,),
            )

            rows = cursor.fetchall()

            results = [dict(row) for row in rows]

            logger.info(
                "Found %d coding question(s) for company: %s",
                len(results),
                company,
            )

            return results

        except Exception:
            logger.exception(
                "Failed to fetch coding questions for company: %s",
                company,
            )
            raise

        finally:
            connection.close()

    def get_subject_questions(self, company: str) -> list[dict]:
        """
        Retrieve all subject questions for a given company.

        Args:
            company:
                Name of the company whose subject questions are fetched.

        Returns:
            A list of dictionaries, one per subject question.
            Returns an empty list if no records exist.
        """

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        try:
            logger.info(
                "Fetching subject questions for company: %s", company
            )

            cursor.execute(
                """
                SELECT
                    sq.id,
                    sq.structured_experience_id,
                    sq.subject,
                    sq.question,
                    sq.round,
                    sq.evidence
                FROM subject_questions AS sq
                INNER JOIN structured_experiences AS se
                    ON sq.structured_experience_id = se.id
                WHERE se.company = ?
                ORDER BY sq.id
                """,
                (company,),
            )

            rows = cursor.fetchall()

            results = [dict(row) for row in rows]

            logger.info(
                "Found %d subject question(s) for company: %s",
                len(results),
                company,
            )

            return results

        except Exception:
            logger.exception(
                "Failed to fetch subject questions for company: %s",
                company,
            )
            raise

        finally:
            connection.close()

    def get_sql_questions(self, company: str) -> list[dict]:
        """
        Retrieve all SQL questions for a given company.

        Args:
            company:
                Name of the company whose SQL questions are fetched.

        Returns:
            A list of dictionaries, one per SQL question.
            Returns an empty list if no records exist.
        """

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        try:
            logger.info(
                "Fetching SQL questions for company: %s", company
            )

            cursor.execute(
                """
                SELECT
                    sqlq.id,
                    sqlq.structured_experience_id,
                    sqlq.question,
                    sqlq.round,
                    sqlq.evidence
                FROM sql_questions AS sqlq
                INNER JOIN structured_experiences AS se
                    ON sqlq.structured_experience_id = se.id
                WHERE se.company = ?
                ORDER BY sqlq.id
                """,
                (company,),
            )

            rows = cursor.fetchall()

            results = [dict(row) for row in rows]

            logger.info(
                "Found %d SQL question(s) for company: %s",
                len(results),
                company,
            )

            return results

        except Exception:
            logger.exception(
                "Failed to fetch SQL questions for company: %s",
                company,
            )
            raise

        finally:
            connection.close()

    def get_hr_questions(self, company: str) -> list[dict]:
        """
        Retrieve all HR questions for a given company.

        Args:
            company:
                Name of the company whose HR questions are fetched.

        Returns:
            A list of dictionaries, one per HR question.
            Returns an empty list if no records exist.
        """

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        try:
            logger.info(
                "Fetching HR questions for company: %s", company
            )

            cursor.execute(
                """
                SELECT
                    hq.id,
                    hq.structured_experience_id,
                    hq.question,
                    hq.type,
                    hq.round,
                    hq.evidence
                FROM hr_questions AS hq
                INNER JOIN structured_experiences AS se
                    ON hq.structured_experience_id = se.id
                WHERE se.company = ?
                ORDER BY hq.id
                """,
                (company,),
            )

            rows = cursor.fetchall()

            results = [dict(row) for row in rows]

            logger.info(
                "Found %d HR question(s) for company: %s",
                len(results),
                company,
            )

            return results

        except Exception:
            logger.exception(
                "Failed to fetch HR questions for company: %s",
                company,
            )
            raise

        finally:
            connection.close()

    def get_rounds(self, company: str) -> list[dict]:
        """
        Retrieve all interview rounds for a given company.

        Args:
            company:
                Name of the company whose interview rounds are fetched.

        Returns:
            A list of dictionaries, one per interview round.
            Returns an empty list if no records exist.
        """

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        try:
            logger.info(
                "Fetching interview rounds for company: %s", company
            )

            cursor.execute(
                """
                SELECT
                    ir.id,
                    ir.structured_experience_id,
                    ir.round_number,
                    ir.round_name,
                    ir.round_type,
                    ir.duration,
                    ir.difficulty,
                    ir.summary
                FROM interview_rounds AS ir
                INNER JOIN structured_experiences AS se
                    ON ir.structured_experience_id = se.id
                WHERE se.company = ?
                ORDER BY ir.id
                """,
                (company,),
            )

            rows = cursor.fetchall()

            results = [dict(row) for row in rows]

            logger.info(
                "Found %d interview round(s) for company: %s",
                len(results),
                company,
            )

            return results

        except Exception:
            logger.exception(
                "Failed to fetch interview rounds for company: %s",
                company,
            )
            raise

        finally:
            connection.close()

    def get_puzzles(self, company: str) -> list[dict]:
        """
        Retrieve all puzzles for a given company.

        Args:
            company:
                Name of the company whose puzzles are fetched.

        Returns:
            A list of dictionaries, one per puzzle.
            Returns an empty list if no records exist.
        """

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        try:
            logger.info(
                "Fetching puzzles for company: %s", company
            )

            cursor.execute(
                """
                SELECT
                    p.id,
                    p.structured_experience_id,
                    p.title,
                    p.difficulty,
                    p.round,
                    p.evidence
                FROM puzzles AS p
                INNER JOIN structured_experiences AS se
                    ON p.structured_experience_id = se.id
                WHERE se.company = ?
                ORDER BY p.id
                """,
                (company,),
            )

            rows = cursor.fetchall()

            results = [dict(row) for row in rows]

            logger.info(
                "Found %d puzzle(s) for company: %s",
                len(results),
                company,
            )

            return results

        except Exception:
            logger.exception(
                "Failed to fetch puzzles for company: %s", company
            )
            raise

        finally:
            connection.close()

    def search_coding_questions(self, keyword: str) -> list[dict]:
        """
        Search coding questions across ALL companies using a keyword.

        The keyword is matched against the question
        title, topic, concepts, and tags.

        Args:
            keyword:
                Search keyword.

        Returns:
            A list of dictionaries, one per matching coding
            question. Each result includes the company name.
            Returns an empty list if no records match.
        """

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        try:
            logger.info(
                "Global search for coding questions using keyword: %s",
                keyword,
            )

            cursor.execute(
                """
                SELECT
                    cq.id,
                    cq.structured_experience_id,
                    se.company,
                    cq.title,
                    cq.topic,
                    cq.concepts,
                    cq.difficulty,
                    cq.round,
                    cq.platform,
                    cq.tags,
                    cq.evidence
                FROM coding_questions AS cq
                INNER JOIN structured_experiences AS se
                    ON cq.structured_experience_id = se.id
                WHERE LOWER(cq.title) LIKE ?
                    OR LOWER(cq.topic) LIKE ?
                    OR LOWER(IFNULL(cq.concepts, '')) LIKE ?
                    OR LOWER(IFNULL(cq.tags, '')) LIKE ?
                ORDER BY se.company, cq.id
                """,
                (
                    f"%{keyword.lower()}%",
                    f"%{keyword.lower()}%",
                    f"%{keyword.lower()}%",
                    f"%{keyword.lower()}%",
                ),
            )

            rows = cursor.fetchall()

            results = [dict(row) for row in rows]

            logger.info(
                "Found %d coding question(s) across all companies.",
                len(results),
            )

            return results

        except Exception:
            logger.exception(
                "Failed to globally search coding questions for keyword: %s",
                keyword,
            )
            raise

        finally:
            connection.close()

    def search_subject_questions(self, keyword: str) -> list[dict]:
        """
        Search subject questions across ALL companies using a keyword.

        The keyword is matched against the subject
        name and question text.

        Args:
            keyword:
                Search keyword.

        Returns:
            A list of dictionaries, one per matching subject
            question. Each result includes the company name.
            Returns an empty list if no records match.
        """

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        try:
            logger.info(
                "Global search for subject questions using keyword: %s",
                keyword,
            )

            cursor.execute(
                """
                SELECT
                    sq.id,
                    sq.structured_experience_id,
                    se.company,
                    sq.subject,
                    sq.question,
                    sq.round,
                    sq.evidence
                FROM subject_questions AS sq
                INNER JOIN structured_experiences AS se
                    ON sq.structured_experience_id = se.id
                WHERE LOWER(sq.subject) LIKE ?
                    OR LOWER(sq.question) LIKE ?
                ORDER BY se.company, sq.id
                """,
                (
                    f"%{keyword.lower()}%",
                    f"%{keyword.lower()}%",
                ),
            )

            rows = cursor.fetchall()

            results = [dict(row) for row in rows]

            logger.info(
                "Found %d subject question(s) across all companies.",
                len(results),
            )

            return results

        except Exception:
            logger.exception(
                "Failed to globally search subject questions for keyword: %s",
                keyword,
            )
            raise

        finally:
            connection.close()

    def search_sql_questions(self, keyword: str) -> list[dict]:
        """
        Search SQL questions across ALL companies using a keyword.

        The keyword is matched against the SQL
        question text.

        Args:
            keyword:
                Search keyword.

        Returns:
            A list of dictionaries, one per matching SQL
            question. Each result includes the company name.
            Returns an empty list if no records match.
        """

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        try:
            logger.info(
                "Global search for SQL questions using keyword: %s",
                keyword,
            )

            cursor.execute(
                """
                SELECT
                    sqlq.id,
                    sqlq.structured_experience_id,
                    se.company,
                    sqlq.question,
                    sqlq.round,
                    sqlq.evidence
                FROM sql_questions AS sqlq
                INNER JOIN structured_experiences AS se
                    ON sqlq.structured_experience_id = se.id
                WHERE LOWER(sqlq.question) LIKE ?
                ORDER BY se.company, sqlq.id
                """,
                (f"%{keyword.lower()}%",),
            )

            rows = cursor.fetchall()

            results = [dict(row) for row in rows]

            logger.info(
                "Found %d SQL question(s) across all companies.",
                len(results),
            )

            return results

        except Exception:
            logger.exception(
                "Failed to globally search SQL questions for keyword: %s",
                keyword,
            )
            raise

        finally:
            connection.close()

    def search_hr_questions(self, keyword: str) -> list[dict]:
        """
        Search HR questions across ALL companies using a keyword.

        The keyword is matched against the HR
        question text and type.

        Args:
            keyword:
                Search keyword.

        Returns:
            A list of dictionaries, one per matching HR
            question. Each result includes the company name.
            Returns an empty list if no records match.
        """

        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()

        try:
            logger.info(
                "Global search for HR questions using keyword: %s",
                keyword,
            )

            cursor.execute(
                """
                SELECT
                    hq.id,
                    hq.structured_experience_id,
                    se.company,
                    hq.question,
                    hq.type,
                    hq.round,
                    hq.evidence
                FROM hr_questions AS hq
                INNER JOIN structured_experiences AS se
                    ON hq.structured_experience_id = se.id
                WHERE LOWER(hq.question) LIKE ?
                    OR LOWER(IFNULL(hq.type, '')) LIKE ?
                ORDER BY se.company, hq.id
                """,
                (
                    f"%{keyword.lower()}%",
                    f"%{keyword.lower()}%",
                ),
            )

            rows = cursor.fetchall()

            results = [dict(row) for row in rows]

            logger.info(
                "Found %d HR question(s) across all companies.",
                len(results),
            )

            return results

        except Exception:
            logger.exception(
                "Failed to globally search HR questions for keyword: %s",
                keyword,
            )
            raise

        finally:
            connection.close()
