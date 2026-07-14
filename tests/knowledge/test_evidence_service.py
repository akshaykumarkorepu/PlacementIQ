from placementiq.knowledge.evidence import EvidenceService
from placementiq.knowledge.retrieval import RetrievalService
from placementiq.repository.knowledge_repository import KnowledgeRepository

repository = KnowledgeRepository()
retrieval = RetrievalService(repository)
evidence = EvidenceService(retrieval)

company = "Oracle"

print("=" * 60)
print("Evidence Service Tests")
print("=" * 60)

# ==========================================================
# Coding Evidence
# ==========================================================

keyword = "Dynamic"

print("\nCoding Evidence")
print("-" * 60)
print(f"Company : {company}")
print(f"Keyword : {keyword}")

results = evidence.get_coding_evidence(
    company,
    keyword,
)

print(f"\nEvidence Records Found : {len(results)}")

if results:
    for index, record in enumerate(results, start=1):
        print(f"\nEvidence #{index}")
        print("-" * 60)

        print(f"Title      : {record.get('title')}")
        print(f"Topic      : {record.get('topic')}")
        print(f"Round      : {record.get('round')}")
        print(f"Difficulty : {record.get('difficulty')}")

        print("\nEvidence")
        print(record.get("evidence"))

else:
    print("No evidence found.")

print("\n" + "=" * 60)

# ==========================================================
# Subject Evidence
# ==========================================================

keyword = "DBMS"

print("Subject Evidence")
print("-" * 60)
print(f"Company : {company}")
print(f"Keyword : {keyword}")

results = evidence.get_subject_evidence(
    company,
    keyword,
)

print(f"\nEvidence Records Found : {len(results)}")

if results:
    for index, record in enumerate(results, start=1):
        print(f"\nEvidence #{index}")
        print("-" * 60)

        print(f"Subject : {record.get('subject')}")
        print(f"Round   : {record.get('round')}")

        print("\nEvidence")
        print(record.get("evidence"))

else:
    print("No evidence found.")

print("\n" + "=" * 60)

# ==========================================================
# SQL Evidence
# ==========================================================

keyword = "JOIN"

print("SQL Evidence")
print("-" * 60)
print(f"Company : {company}")
print(f"Keyword : {keyword}")

results = evidence.get_sql_evidence(
    company,
    keyword,
)

print(f"\nEvidence Records Found : {len(results)}")

if results:
    for index, record in enumerate(results, start=1):
        print(f"\nEvidence #{index}")
        print("-" * 60)

        print(f"Round : {record.get('round')}")

        print("\nEvidence")
        print(record.get("evidence"))

else:
    print("No evidence found.")

print("\n" + "=" * 60)

# ==========================================================
# HR Evidence
# ==========================================================

keyword = "Project"

print("HR Evidence")
print("-" * 60)
print(f"Company : {company}")
print(f"Keyword : {keyword}")

results = evidence.get_hr_evidence(
    company,
    keyword,
)

print(f"\nEvidence Records Found : {len(results)}")

if results:
    for index, record in enumerate(results, start=1):
        print(f"\nEvidence #{index}")
        print("-" * 60)

        print(f"Type  : {record.get('type')}")
        print(f"Round : {record.get('round')}")

        print("\nEvidence")
        print(record.get("evidence"))

else:
    print("No evidence found.")

print("\n" + "=" * 60)

# ==========================================================
# Interview Round Evidence
# ==========================================================

keyword = "Technical"

print("Interview Round Evidence")
print("-" * 60)
print(f"Company : {company}")
print(f"Keyword : {keyword}")

results = evidence.get_round_evidence(
    company,
    keyword,
)

print(f"\nEvidence Records Found : {len(results)}")

if results:
    for index, record in enumerate(results, start=1):
        print(f"\nEvidence #{index}")
        print("-" * 60)

        print(f"Round Type : {record.get('round_type')}")
        print(f"Difficulty : {record.get('difficulty')}")

        print("\nSummary")
        print(record.get("summary"))

else:
    print("No evidence found.")

print("\n" + "=" * 60)

# ==========================================================
# Puzzle Evidence
# ==========================================================

keyword = "Puzzle"

print("Puzzle Evidence")
print("-" * 60)
print(f"Company : {company}")
print(f"Keyword : {keyword}")

results = evidence.get_puzzle_evidence(
    company,
    keyword,
)

print(f"\nEvidence Records Found : {len(results)}")

if results:
    for index, record in enumerate(results, start=1):
        print(f"\nEvidence #{index}")
        print("-" * 60)

        print(f"Title      : {record.get('title')}")
        print(f"Difficulty : {record.get('difficulty')}")

        print("\nEvidence")
        print(record.get("evidence"))

else:
    print("No evidence found.")

print("\n" + "=" * 60)
print("Evidence Service Test Completed Successfully")
print("=" * 60)
