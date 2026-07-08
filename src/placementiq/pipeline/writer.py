import json
from pathlib import Path
from typing import Any


DATA_DIR = Path("data")
OUTPUT_FILE = DATA_DIR / "interviews.json"


def write_interviews(
    interviews: list[dict[str, Any]],
) -> None:
    """
    Write normalized interviews to interviews.json.
    """

    DATA_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    with OUTPUT_FILE.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            interviews,
            file,
            indent=4,
            ensure_ascii=False,
        )
