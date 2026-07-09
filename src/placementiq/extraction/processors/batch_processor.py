"""
PlacementIQ Batch Processor

Processes every raw interview through the complete
AI extraction pipeline.
"""

import json
import sqlite3

from placementiq.extraction.extractors.interview_extractor import (
    InterviewExtractor,
)
from placementiq.repository.extraction_repository import (
    ExtractionRepository,
)


class BatchProcessor:
    """
    Runs the complete extraction pipeline for
    every interview stored in the raw database.
    """

    def __init__(
        self,
        database_path: str = "data/placementiq.db",
    ):
        """
        Initialize the batch processor.

        Args:
            database_path:
                Path to the SQLite database.
        """

        self.database_path = database_path

        self.extractor = InterviewExtractor()

        self.repository = ExtractionRepository(database_path)

    def run(self):
        """
        Run the complete extraction pipeline for
        every interview in the database.
        """

        connection = sqlite3.connect(self.database_path)

        connection.row_factory = sqlite3.Row

        cursor = connection.cursor()

        try:
            cursor.execute(
                """
                SELECT *
                FROM interviews
                WHERE id NOT IN (
                   SELECT interview_id
                   FROM structured_experiences
            )
            LIMIT 20
            """
            )

            interviews = cursor.fetchall()

            total = len(interviews)

            successful = 0

            failed = 0

            print("=" * 60)
            print("PLACEMENTIQ BATCH PROCESSOR")
            print("=" * 60)
            print(f"\nFound {total} interviews.\n")

            for index, row in enumerate(interviews, start=1):
                print("-" * 60)
                print(f"Processing {index}/{total}")

                interview = dict(row)

                interview["eligible_branches"] = json.loads(
                    interview["eligible_branches"]
                )

                interview["online_test"] = json.loads(interview["online_test"])

                interview["interview_rounds"] = json.loads(
                    interview["interview_rounds"]
                )

                interview["rounds"] = json.loads(interview["rounds"])

                try:
                    structured_data = self.extractor.extract(interview)

                    self.repository.save_extraction(
                        interview["id"],
                        structured_data,
                    )

                    successful += 1

                    print(f"✓ {interview['company']} processed successfully.")

                except Exception as error:
                    failed += 1

                    print(f"✗ Failed to process {interview['company']}")

                    print(f"Reason: {error}")

                    continue

            print("\n" + "=" * 60)
            print("BATCH PROCESSING COMPLETE")
            print("=" * 60)

            print(f"Total Interviews : {total}")
            print(f"Successful       : {successful}")
            print(f"Failed           : {failed}")

            success_rate = (successful / total) * 100 if total > 0 else 0

            print(f"Success Rate     : {success_rate:.2f}%")

            print("=" * 60)

        finally:
            connection.close()
