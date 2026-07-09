"""
PlacementIQ Repository Integration Test

Pipeline:

Raw Interview
        ↓
InterviewExtractor
        ↓
ExtractionRepository
        ↓
SQLite
"""

import json
import sqlite3

from placementiq.extraction.extractors.interview_extractor import InterviewExtractor
from placementiq.repository.extraction_repository import (
    ExtractionRepository,
)

DATABASE_PATH = "data/placementiq.db"


def print_table_count(cursor, table_name: str):
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    print(f"{table_name:<25}: {count}")


def main():
    print("=" * 60)
    print("PLACEMENTIQ REPOSITORY TEST")
    print("=" * 60)

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    print("\nLoading one interview...")

    cursor.execute(
        """
        SELECT *
        FROM interviews
        LIMIT 1
        """
    )

    row = cursor.fetchone()

    if row is None:
        raise ValueError("No interviews found in database.")

    interview = dict(row)

    # Convert JSON strings back into Python objects
    interview["eligible_branches"] = json.loads(interview["eligible_branches"])
    interview["online_test"] = json.loads(interview["online_test"])
    interview["interview_rounds"] = json.loads(interview["interview_rounds"])
    interview["rounds"] = json.loads(interview["rounds"])

    print(f"✓ Company : {interview['company']}")
    print(f"✓ Batch   : {interview['batch']}")

    connection.close()

    print("\nInitializing InterviewExtractor...")

    extractor = InterviewExtractor()

    print("✓ InterviewExtractor initialized.")

    print("\nRunning extraction...")

    structured_data = extractor.extract(interview)

    print("✓ Extraction completed.")

    print("\nInitializing ExtractionRepository...")

    repository = ExtractionRepository()

    print("✓ Repository initialized.")

    print("\nSaving extraction...")

    structured_experience_id = repository.save_extraction(
        interview["id"],
        structured_data,
    )

    print("✓ Saved successfully.")

    print(f"\nStructured Experience ID : {structured_experience_id}")

    print("\n" + "=" * 60)
    print("DATABASE VERIFICATION")
    print("=" * 60)

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    print_table_count(cursor, "structured_experiences")
    print_table_count(cursor, "coding_questions")
    print_table_count(cursor, "subject_questions")
    print_table_count(cursor, "sql_questions")
    print_table_count(cursor, "puzzles")
    print_table_count(cursor, "hr_questions")
    print_table_count(cursor, "interview_rounds")

    connection.close()

    print("\n" + "=" * 60)
    print("TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()
