import json
from datetime import datetime
from pathlib import Path


INTERVIEWS_PATH = Path("data") / "interviews.json"
METADATA_PATH = Path("data") / "metadata.json"


class MetadataGenerator:
    """
    Generate metadata for the interview dataset.
    """

    def __init__(self):
        self.interviews_path = INTERVIEWS_PATH
        self.metadata_path = METADATA_PATH

    def generate(self):
        """
        Generate metadata.json from interviews.json.
        """

        # Read interviews
        with open(self.interviews_path, "r", encoding="utf-8") as file:
            interviews = json.load(file)

        print(f"Loaded {len(interviews)} interviews.")

        # Companies
        companies = sorted({interview["company"] for interview in interviews})

        # Experience Types
        experience_types = sorted(
            {interview["experience_type"] for interview in interviews}
        )

        # Batches
        batches = sorted({interview["batch"] for interview in interviews})

        # Status Counts
        status_counts = {}

        for interview in interviews:
            status = interview["status"]

            status_counts[status] = status_counts.get(status, 0) + 1

        # Metadata
        metadata = {
            "generated_at": datetime.now().isoformat(),
            "total_interviews": len(interviews),
            "total_companies": len(companies),
            "companies": companies,
            "experience_types": experience_types,
            "batches": batches,
            "status_counts": status_counts,
        }

        # Write metadata
        with open(self.metadata_path, "w", encoding="utf-8") as file:
            json.dump(metadata, file, indent=4, ensure_ascii=False)

        print("Metadata generated successfully.")

        return metadata
