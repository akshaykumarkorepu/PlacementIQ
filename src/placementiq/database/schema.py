import sqlite3
from pathlib import Path

# Database file
DATABASE_PATH = Path("data") / "placementiq.db"


class DatabaseSchema:
    """
    Creates the PlacementIQ SQLite database
    and its tables.
    """

    def __init__(self):
        self.database_path = DATABASE_PATH

    def create_database(self):
        """
        Create the SQLite database and
        the interviews table.
        """

        connection = sqlite3.connect(self.database_path)

        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS interviews (

            id TEXT PRIMARY KEY,

            company TEXT NOT NULL,

            experience_type TEXT,

            batch TEXT,

            start_year INTEGER,

            end_year INTEGER,

            cgpa_cutoff REAL,

            eligible_branches TEXT,

            number_of_selections INTEGER,

            online_test TEXT,

            interview_rounds TEXT,

            other_comments TEXT,

            job_description TEXT,

            rounds TEXT,

            status TEXT,

            created_at TEXT,

            updated_at TEXT,

            source_url TEXT

        )
        """)

        connection.commit()

        connection.close()
