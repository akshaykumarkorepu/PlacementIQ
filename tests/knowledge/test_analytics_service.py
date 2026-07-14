from placementiq.knowledge.analytics import AnalyticsService
from placementiq.knowledge.retrieval import RetrievalService
from placementiq.repository.knowledge_repository import KnowledgeRepository

repository = KnowledgeRepository()
retrieval = RetrievalService(repository)
analytics = AnalyticsService(retrieval)

company = "Oracle"

print("=" * 60)
print("Analytics Service Tests")
print("=" * 60)

print(f"\nCompany: {company}")

# --------------------------------------------------
# Topic Frequency
# --------------------------------------------------

topic_frequency = analytics.get_topic_frequency(company)

print("\nTopic Frequency")
print("-" * 60)

if topic_frequency:
    for topic, count in sorted(
        topic_frequency.items(),
        key=lambda item: item[1],
        reverse=True,
    ):
        print(f"{topic}: {count}")
else:
    print("No topics found.")

# --------------------------------------------------
# Difficulty Distribution
# --------------------------------------------------

difficulty_distribution = analytics.get_difficulty_distribution(company)

print("\nDifficulty Distribution")
print("-" * 60)

if difficulty_distribution:
    for difficulty, count in sorted(
        difficulty_distribution.items(),
        key=lambda item: item[1],
        reverse=True,
    ):
        print(f"{difficulty}: {count}")
else:
    print("No difficulty information found.")

# --------------------------------------------------
# Interview Pattern
# --------------------------------------------------

interview_pattern = analytics.get_interview_pattern(company)

print("\nInterview Pattern")
print("-" * 60)

if interview_pattern:
    for round_type, count in sorted(
        interview_pattern.items(),
        key=lambda item: item[1],
        reverse=True,
    ):
        print(f"{round_type}: {count}")
else:
    print("No interview pattern found.")

# --------------------------------------------------
# HR Question Frequency
# --------------------------------------------------

hr_question_frequency = analytics.get_hr_question_frequency(company)

print("\nHR Question Frequency")
print("-" * 60)

if hr_question_frequency:
    for question_type, count in sorted(
        hr_question_frequency.items(),
        key=lambda item: item[1],
        reverse=True,
    ):
        print(f"{question_type}: {count}")
else:
    print("No HR question information found.")

# --------------------------------------------------
# Company Summary
# --------------------------------------------------

company_summary = analytics.get_company_summary(company)

print("\nCompany Summary")
print("-" * 60)

for key, value in company_summary.items():
    if isinstance(value, dict):
        print(f"{key}:")
        for sub_key, sub_value in sorted(
            value.items(),
            key=lambda item: item[1],
            reverse=True,
        ):
            print(f"  {sub_key}: {sub_value}")
    else:
        print(f"{key}: {value}")

print("\n" + "=" * 60)
print("Analytics Service Test Completed Successfully")
print("=" * 60)
