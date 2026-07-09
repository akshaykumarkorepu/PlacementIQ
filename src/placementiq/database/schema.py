import sqlite3
from pathlib import Path

# Database file
DATABASE_PATH = Path("data") / "placementiq.db"


class DatabaseSchema:
    """
    Creates the PlacementIQ SQLite database
    and its tables.

    Two layers live in this single SQLite file:

    - Phase 2 (raw layer): the immutable ``interviews`` table.
    - Phase 3 (extraction layer): the AI-derived knowledge tables
      ``structured_experiences`` and its child tables
      (``coding_questions``, ``subject_questions``, ``sql_questions``,
      ``puzzles``, ``hr_questions``, ``interview_rounds``).

    The raw layer is never modified by the extraction layer; the
    ``interviews`` table is the source of truth and ``structured_experiences``
    references it via ``interview_id``.
    """

    def __init__(self):
        self.database_path = DATABASE_PATH

    def create_database(self):
        """
        Create the SQLite database and all tables (raw + extraction).
        """

        connection = sqlite3.connect(self.database_path)

        try:
            cursor = connection.cursor()

            # ------------------------------------------------------------------
            # Phase 2 — Raw layer (immutable source of truth).
            # Kept exactly as before; never modified by the extraction layer.
            # ------------------------------------------------------------------
            cursor.execute(
                """
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
                """
            )

            # ------------------------------------------------------------------
            # Phase 3 — Extraction layer (AI-derived knowledge).
            # See ``docs/extraction_database.md`` for the contract.
            # ------------------------------------------------------------------

            # ``structured_experiences`` is the AI knowledge layer. One row
            # per accepted extraction of an interview. References the raw
            # ``interviews`` table via ``interview_id``; the raw row is never
            # mutated by the extraction pipeline.
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS structured_experiences (

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    interview_id TEXT NOT NULL,

                    company TEXT,

                    role TEXT,

                    batch TEXT,

                    experience_type TEXT,

                    result TEXT,

                    overall_difficulty TEXT,

                    number_of_rounds INTEGER,

                    oa_platform TEXT,

                    summary TEXT,

                    technologies JSON,

                    keywords JSON,

                    tips JSON,

                    mistakes JSON,

                    resources JSON,

                    important_concepts JSON,

                    projects_discussed JSON,

                    schema_version TEXT,

                    model_used TEXT,

                    processed_at DATETIME,

                    FOREIGN KEY (interview_id) REFERENCES interviews(id)

                )
                """
            )

            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_structured_experiences_company "
                "ON structured_experiences (company)"
            )
            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_structured_experiences_role "
                "ON structured_experiences (role)"
            )
            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_structured_experiences_batch "
                "ON structured_experiences (batch)"
            )
            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_structured_experiences_experience_type "
                "ON structured_experiences (experience_type)"
            )
            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_structured_experiences_overall_difficulty "
                "ON structured_experiences (overall_difficulty)"
            )
            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_structured_experiences_interview_id "
                "ON structured_experiences (interview_id)"
            )

            # ``coding_questions`` stores every coding question individually
            # so each one becomes searchable. ``tags`` is JSON because it is
            # retrieved together with the question rather than searched on
            # its own.
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS coding_questions (

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    structured_experience_id TEXT NOT NULL,

                    title TEXT,

                    topic TEXT,

                    concepts JSON,

                    difficulty TEXT,

                    round TEXT,

                    platform TEXT,

                    tags JSON,

                    evidence TEXT,

                    FOREIGN KEY (structured_experience_id)
                        REFERENCES structured_experiences(id)

                )
                """
            )

            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_coding_questions_experience "
                "ON coding_questions (structured_experience_id)"
            )
            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_coding_questions_topic "
                "ON coding_questions (topic)"
            )
            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_coding_questions_title "
                "ON coding_questions (title)"
            )
            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_coding_questions_difficulty "
                "ON coding_questions (difficulty)"
            )

            # ``subject_questions`` stores Core CS questions in a single
            # table, with ``subject`` constrained by application logic to
            # the allowed set (DBMS, OS, CN, OOP, Aptitude, System Design).
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS subject_questions (

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    structured_experience_id TEXT NOT NULL,

                    subject TEXT,

                    question TEXT,

                    round TEXT,

                    evidence TEXT,

                    FOREIGN KEY (structured_experience_id)
                        REFERENCES structured_experiences(id)

                )
                """
            )

            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_subject_questions_experience "
                "ON subject_questions (structured_experience_id)"
            )
            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_subject_questions_subject "
                "ON subject_questions (subject)"
            )

            # ``sql_questions`` stores SQL interview questions separately
            # from coding and subject questions because they are queried
            # and ranked on their own.
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS sql_questions (

                   id INTEGER PRIMARY KEY AUTOINCREMENT,

                    structured_experience_id TEXT NOT NULL,

                    question TEXT,

                    round TEXT,

                    evidence TEXT,

                    FOREIGN KEY (structured_experience_id)
                        REFERENCES structured_experiences(id)

                )
                """
            )

            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_sql_questions_experience "
                "ON sql_questions (structured_experience_id)"
            )
            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_sql_questions_question "
                "ON sql_questions (question)"
            )

            # ``puzzles`` stores logical puzzles asked during interviews.
            # ``title`` is indexed because the same puzzle recurs across
            # companies and is a primary retrieval key.
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS puzzles (

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    structured_experience_id TEXT NOT NULL,

                    title TEXT,

                    difficulty TEXT,

                    round TEXT,

                    evidence TEXT,

                    FOREIGN KEY (structured_experience_id)
                        REFERENCES structured_experiences(id)

                )
                """
            )

            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_puzzles_experience "
                "ON puzzles (structured_experience_id)"
            )
            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_puzzles_title ON puzzles (title)"
            )

            # ``hr_questions`` stores HR and behavioural questions.
            # ``type`` is constrained by application logic to
            # (HR, Behavioural, Resume).
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS hr_questions (

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    structured_experience_id TEXT NOT NULL,

                    question TEXT,

                    type TEXT,

                    round TEXT,

                    evidence TEXT,

                    FOREIGN KEY (structured_experience_id)
                        REFERENCES structured_experiences(id)

                )
                """
            )

            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_hr_questions_experience "
                "ON hr_questions (structured_experience_id)"
            )
            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_hr_questions_type "
                "ON hr_questions (type)"
            )

            # ``interview_rounds`` stores the complete interview flow for a
            # structured experience (one row per round, ordered by
            # ``round_number``).
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS interview_rounds (

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    structured_experience_id TEXT NOT NULL,

                    round_number INTEGER,

                    round_name TEXT,

                    round_type TEXT,

                    duration TEXT,

                    difficulty TEXT,

                    summary TEXT,

                    FOREIGN KEY (structured_experience_id)
                        REFERENCES structured_experiences(id)

                )
                """
            )

            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_interview_rounds_experience "
                "ON interview_rounds (structured_experience_id)"
            )
            cursor.execute(
                "CREATE INDEX IF NOT EXISTS idx_interview_rounds_experience_number "
                "ON interview_rounds (structured_experience_id, round_number)"
            )

            connection.commit()

        finally:
            connection.close()


if __name__ == "__main__":
    schema = DatabaseSchema()
    schema.create_database()
    print("PlacementIQ database created successfully.")
