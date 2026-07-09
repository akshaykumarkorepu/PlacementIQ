"""
Clear all extracted interview data while
keeping the raw interviews intact.
"""

import sqlite3

DATABASE_PATH = "data/placementiq.db"


def main():
    connection = sqlite3.connect(DATABASE_PATH)

    try:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM interview_rounds")
        cursor.execute("DELETE FROM hr_questions")
        cursor.execute("DELETE FROM puzzles")
        cursor.execute("DELETE FROM sql_questions")
        cursor.execute("DELETE FROM subject_questions")
        cursor.execute("DELETE FROM coding_questions")
        cursor.execute("DELETE FROM structured_experiences")

        connection.commit()

        print("Extraction tables cleared successfully.")

    finally:
        connection.close()


if __name__ == "__main__":
    main()
