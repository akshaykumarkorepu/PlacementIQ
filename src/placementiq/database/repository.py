import sqlite3
from pathlib import Path

DATABASE_PATH = Path("data") / "placementiq.db"


class InterviewRepository:
    """
    Repository for querying interview data.
    """

    def __init__(self):
        self.database_path = DATABASE_PATH

    def _connect(self):
        """
        Create and return a SQLite connection.
        """
        return sqlite3.connect(self.database_path)

    def count(self):
        """
        Return the total number of interviews.
        """

        connection = self._connect()

        try:
            cursor = connection.cursor()

            cursor.execute("SELECT COUNT(*) FROM interviews")

            total = cursor.fetchone()[0]

            return total

        finally:
            connection.close()
