from placementiq.knowledge.search import SearchService
from placementiq.knowledge.retrieval import RetrievalService
from placementiq.repository.knowledge_repository import KnowledgeRepository

repository = KnowledgeRepository()
retrieval = RetrievalService(repository)
search = SearchService(retrieval)

company = "Oracle"

print("=" * 60)
print("Search Service Tests")
print("=" * 60)

# ==========================================================
# Coding Questions
# ==========================================================

keyword = "Dynamic"

print(f"\nCompany : {company}")
print(f"\nCoding Search Keyword : {keyword}")

results = search.search_coding_questions(
    company,
    keyword,
)

print(f"Matches : {len(results)}")

for index, question in enumerate(results[:10], start=1):
    print(f"{index}. {question['title']}")

print("-" * 60)

# ==========================================================
# Subject Questions
# ==========================================================

keyword = "DBMS"

print(f"\nSubject Search Keyword : {keyword}")

results = search.search_subject_questions(
    company,
    keyword,
)

print(f"Matches : {len(results)}")

for index, question in enumerate(results[:10], start=1):
    print(f"{index}. {question['subject']}")
    print(f"   {question['question']}")

print("-" * 60)

# ==========================================================
# SQL Questions
# ==========================================================

keyword = "Query"

print(f"\nSQL Search Keyword : {keyword}")

results = search.search_sql_questions(
    company,
    keyword,
)

print(f"Matches : {len(results)}")

for index, question in enumerate(results[:10], start=1):
    print(f"{index}. {question['question']}")

print("-" * 60)

# ==========================================================
# HR Questions
# ==========================================================

keyword = "Project"

print(f"\nHR Search Keyword : {keyword}")

results = search.search_hr_questions(
    company,
    keyword,
)

print(f"Matches : {len(results)}")

for index, question in enumerate(results[:10], start=1):
    print(f"{index}. [{question['type']}]")
    print(f"   {question['question']}")

print("-" * 60)

# ==========================================================
# Interview Rounds
# ==========================================================

keyword = "Technical"

print(f"\nRound Search Keyword : {keyword}")

results = search.search_rounds(
    company,
    keyword,
)

print(f"Matches : {len(results)}")

for index, round_data in enumerate(results[:10], start=1):
    print(f"{index}. {round_data['round_name']}")
    print(f"   Type : {round_data['round_type']}")

print("-" * 60)

# ==========================================================
# Puzzles
# ==========================================================

keyword = "Easy"

print(f"\nPuzzle Search Keyword : {keyword}")

results = search.search_puzzles(
    company,
    keyword,
)

print(f"Matches : {len(results)}")

for index, puzzle in enumerate(results[:10], start=1):
    print(f"{index}. {puzzle['title']}")
    print(f"   Difficulty : {puzzle['difficulty']}")

print("-" * 60)

print("\nSearch Service Test Completed Successfully")
