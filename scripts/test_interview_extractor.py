"""
Manual Integration Test for InterviewExtractor

This script:

1. Loads one interview from the database.
2. Sends it to the InterviewExtractor.
3. Prints the extracted structured JSON.
"""

import json
import sqlite3

from placementiq.extraction.extractors.interview_extractor import (
    InterviewExtractor,
)

DATABASE_PATH = "data/placementiq.db"


def load_one_interview() -> dict:
    """
    Load one interview from the raw interviews table.
    """

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM interviews
        LIMIT 1
        """
    )

    row = cursor.fetchone()

    connection.close()

    if row is None:
        raise ValueError("No interviews found in the database.")

    return dict(row)


def main():
    print("=" * 70)
    print("PLACEMENTIQ INTERVIEW EXTRACTOR TEST")
    print("=" * 70)

    print("\nLoading interview from database...")

    interview = load_one_interview()

    print(f"✓ Company : {interview['company']}")
    print(f"✓ Batch   : {interview['batch']}")

    print("\nInitializing InterviewExtractor...")

    extractor = InterviewExtractor()

    print("✓ InterviewExtractor initialized.")

    print("\nSending interview to Groq...\n")

    structured_interview = extractor.extract(interview)

    print("=" * 70)
    print("EXTRACTION SUCCESSFUL")
    print("=" * 70)

    print(json.dumps(structured_interview, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
