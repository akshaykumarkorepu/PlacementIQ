import json
import sqlite3
from pathlib import Path

DATABASE_PATH = Path("data") / "placementiq.db"
INTERVIEWS_PATH = Path("data") / "interviews.json"


class SQLiteLoader:
    def __init__(self):
        self.database_path = DATABASE_PATH
        self.interviews_path = INTERVIEWS_PATH

    def load(self):
        """
        Load all interviews from interviews.json into SQLite.
        """

        # Read JSON
        with open(self.interviews_path, "r", encoding="utf-8") as file:
            interviews = json.load(file)

        print(f"Loaded {len(interviews)} interviews from JSON.")

        # Connect to SQLite
        connection = sqlite3.connect(self.database_path)

        try:
            print("Connected to SQLite database.")

            cursor = connection.cursor()

            print("Cursor created successfully.")

            # Remove old data
            cursor.execute("DELETE FROM interviews")

            print("Cleared existing interviews.")

            # Insert every interview
            for interview in interviews:
                cursor.execute(
                    """
                    INSERT INTO interviews (
                        id,
                        company,
                        experience_type,
                        batch,
                        start_year,
                        end_year,
                        cgpa_cutoff,
                        eligible_branches,
                        number_of_selections,
                        online_test,
                        interview_rounds,
                        other_comments,
                        job_description,
                        rounds,
                        status,
                        created_at,
                        updated_at,
                        source_url
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        interview["id"],
                        interview["company"],
                        interview["experience_type"],
                        interview["batch"],
                        interview["start_year"],
                        interview["end_year"],
                        interview["cgpa_cutoff"],
                        json.dumps(interview["eligible_branches"]),
                        interview["number_of_selections"],
                        json.dumps(interview["online_test"]),
                        json.dumps(interview["interview_rounds"]),
                        interview["other_comments"],
                        interview["job_description"],
                        json.dumps(interview["rounds"]),
                        interview["status"],
                        interview["created_at"],
                        interview["updated_at"],
                        interview["source_url"],
                    ),
                )

            connection.commit()

            print(f"Inserted {len(interviews)} interviews successfully.")

            return interviews

        finally:
            connection.close()
            print("Database connection closed.")


if __name__ == "__main__":
    loader = SQLiteLoader()
    loader.load()
