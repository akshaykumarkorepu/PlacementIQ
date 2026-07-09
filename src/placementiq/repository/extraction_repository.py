"""
PlacementIQ Extraction Repository

Responsible for persisting structured interview data
into the extraction database.
"""

import json
import sqlite3


class ExtractionRepository:
    """
    Handles all database operations related to the
    extraction layer.
    """

    def __init__(self, database_path: str = "data/placementiq.db"):
        """
        Initialize the repository.

        Args:
            database_path:
                Path to the SQLite database.
        """

        self.database_path = database_path

    def save_extraction(
        self,
        interview_id: int,
        structured_data: dict,
    ) -> int:
        """
        Save one extracted interview into the database.

        Args:
            interview_id:
                ID of the raw interview from the
                interviews table.

            structured_data:
                Dictionary returned by InterviewExtractor.

        Returns:
            ID of the inserted structured experience.
        """

        connection = sqlite3.connect(self.database_path)
        cursor = connection.cursor()

        try:
            structured = structured_data["structured_experience"]

            cursor.execute(
                """
                INSERT INTO structured_experiences (
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
                    projects_discussed
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    interview_id,
                    structured["company"],
                    structured["role"],
                    structured["batch"],
                    structured["experience_type"],
                    structured["result"],
                    structured["overall_difficulty"],
                    structured["number_of_rounds"],
                    structured["oa_platform"],
                    structured["summary"],
                    json.dumps(structured["technologies"]),
                    json.dumps(structured["keywords"]),
                    json.dumps(structured["tips"]),
                    json.dumps(structured["mistakes"]),
                    json.dumps(structured["resources"]),
                    json.dumps(structured["important_concepts"]),
                    json.dumps(structured["projects_discussed"]),
                ),
            )

            structured_experience_id = cursor.lastrowid

            for question in structured_data["coding_questions"]:
                cursor.execute(
                    """
                    INSERT INTO coding_questions (
                        structured_experience_id,
                        title,
                        topic,
                        concepts,
                        difficulty,
                        round,
                        platform,
                        tags,
                        evidence
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        structured_experience_id,
                        question["title"],
                        question["topic"],
                        json.dumps(question["concepts"]),
                        question["difficulty"],
                        question["round"],
                        question["platform"],
                        json.dumps(question["tags"]),
                        question["evidence"],
                    ),
                )

            for question in structured_data["subject_questions"]:
                cursor.execute(
                    """
                    INSERT INTO subject_questions (
                        structured_experience_id,
                        subject,
                        question,
                        round,
                        evidence
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        structured_experience_id,
                        question["subject"],
                        question["question"],
                        question["round"],
                        question["evidence"],
                    ),
                )

            for question in structured_data["sql_questions"]:
                cursor.execute(
                    """
                    INSERT INTO sql_questions (
                        structured_experience_id,
                        question,
                        round,
                        evidence
                    )
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        structured_experience_id,
                        question["question"],
                        question["round"],
                        question["evidence"],
                    ),
                )

            for puzzle in structured_data["puzzles"]:
                cursor.execute(
                    """
                    INSERT INTO puzzles (
                        structured_experience_id,
                        title,
                        difficulty,
                        round,
                        evidence
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        structured_experience_id,
                        puzzle["title"],
                        puzzle["difficulty"],
                        puzzle["round"],
                        puzzle["evidence"],
                    ),
                )

            for question in structured_data["hr_questions"]:
                cursor.execute(
                    """
                    INSERT INTO hr_questions (
                        structured_experience_id,
                        question,
                        type,
                        round,
                        evidence
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        structured_experience_id,
                        question["question"],
                        question["type"],
                        question["round"],
                        question["evidence"],
                    ),
                )

            for index, round_data in enumerate(
                structured_data["interview_rounds"], start=1
            ):
                cursor.execute(
                    """
                    INSERT INTO interview_rounds (
                        structured_experience_id,
                        round_number,
                        round_name,
                        round_type,
                        duration,
                        difficulty,
                        summary
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        structured_experience_id,
                        index,
                        round_data["round_name"],
                        round_data["round_type"],
                        round_data["round_duration"],
                        round_data["round_difficulty"],
                        round_data["round_summary"],
                    ),
                )

            connection.commit()

            return structured_experience_id

        except Exception:
            connection.rollback()
            raise

        finally:
            connection.close()
