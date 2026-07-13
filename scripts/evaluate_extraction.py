"""
PlacementIQ Extraction Evaluation

Displays statistics about the current
state of the extraction database.
"""

import sqlite3

DATABASE_PATH = "data/placementiq.db"


def get_count(cursor, table_name):
    """
    Return the number of rows in a table.
    """

    cursor.execute(
        f"""
        SELECT COUNT(*)
        FROM {table_name}
        """
    )

    return cursor.fetchone()[0]


def main():
    """
    Generate and display the extraction report.
    """

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    try:
        raw_interviews = get_count(
            cursor,
            "interviews",
        )

        structured_experiences = get_count(
            cursor,
            "structured_experiences",
        )

        coding_questions = get_count(
            cursor,
            "coding_questions",
        )

        subject_questions = get_count(
            cursor,
            "subject_questions",
        )

        sql_questions = get_count(
            cursor,
            "sql_questions",
        )

        hr_questions = get_count(
            cursor,
            "hr_questions",
        )

        puzzles = get_count(
            cursor,
            "puzzles",
        )

        interview_rounds = get_count(
            cursor,
            "interview_rounds",
        )

        remaining = raw_interviews - structured_experiences

        success_rate = (
            (structured_experiences / raw_interviews) * 100 if raw_interviews > 0 else 0
        )

        print("=" * 45)
        print("PLACEMENTIQ EXTRACTION REPORT")
        print("=" * 45)

        print()

        print(f"Raw Interviews         : {raw_interviews}")

        print(f"Processed              : {structured_experiences}")

        print(f"Remaining              : {remaining}")

        print()

        print(f"Success Rate           : {success_rate:.2f}%")

        print("-" * 45)

        print()

        print(f"Structured Experiences : {structured_experiences}")

        print(f"Coding Questions       : {coding_questions}")

        print(f"Subject Questions      : {subject_questions}")

        print(f"SQL Questions          : {sql_questions}")

        print(f"HR Questions           : {hr_questions}")

        print(f"Puzzles                : {puzzles}")

        print(f"Interview Rounds       : {interview_rounds}")

        print()

        print("=" * 45)

    finally:
        connection.close()


if __name__ == "__main__":
    main()
