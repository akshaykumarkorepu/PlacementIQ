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

    experiences = repo.get_company_experiences(company)
    coding_questions = repo.get_coding_questions(company)
    subject_questions = repo.get_subject_questions(company)
    sql_questions = repo.get_sql_questions(company)
    hr_questions = repo.get_hr_questions(company)
    rounds = repo.get_rounds(company)
    puzzles = repo.get_puzzles(company)

    print(f"Experiences: {len(experiences)}")
    print(f"Coding: {len(coding_questions)}")
    print(f"Subjects: {len(subject_questions)}")
    print(f"SQL: {len(sql_questions)}")
    print(f"HR: {len(hr_questions)}")
    print(f"Rounds: {len(rounds)}")
    print(f"Puzzles: {len(puzzles)}")

    print("\nFirst 10 Coding Questions")

    if coding_questions:
        for index, question in enumerate(coding_questions[:10], start=1):
            print(
                f"{index}. "
                f"{question['title']} | "
                f"{question['topic']} | "
                f"{question['difficulty']}"
            )
    else:
        print("No coding questions found.")

    print("-" * 60)
