from placementiq.repository.knowledge_repository import KnowledgeRepository

repo = KnowledgeRepository()

print("=" * 60)
print("Knowledge Repository Tests")
print("=" * 60)

companies = [
    "Oracle",
    "Amazon",
    "Microsoft",
]

for company in companies:
    print(f"\nCompany: {company}")

    print("Experiences:", len(repo.get_company_experiences(company)))

    print("Coding:", len(repo.get_coding_questions(company)))

    print("Subjects:", len(repo.get_subject_questions(company)))

    print("SQL:", len(repo.get_sql_questions(company)))

    print("HR:", len(repo.get_hr_questions(company)))

    print("Rounds:", len(repo.get_rounds(company)))

    print("Puzzles:", len(repo.get_puzzles(company)))
