from placementiq.knowledge.analytics import AnalyticsService
from placementiq.knowledge.comparison import ComparisonService
from placementiq.knowledge.retrieval import RetrievalService
from placementiq.repository.knowledge_repository import KnowledgeRepository

repository = KnowledgeRepository()
retrieval = RetrievalService(repository)
analytics = AnalyticsService(retrieval)
comparison = ComparisonService(analytics)

company_1 = "Oracle"
company_2 = "Microsoft"

print("=" * 60)
print("Comparison Service Tests")
print("=" * 60)

# ==========================================================
# Company Summary Comparison
# ==========================================================

print(f"\nCompany 1 : {company_1}")
print(f"Company 2 : {company_2}")

comparison_result = comparison.compare_companies(
    company_1,
    company_2,
)

print("\nCompany Summary")
print("-" * 60)

print(
    f"Experiences : "
    f"{comparison_result['company_1']['total_experiences']} vs "
    f"{comparison_result['company_2']['total_experiences']}"
)

print(
    f"Coding Questions : "
    f"{comparison_result['company_1']['coding_questions']} vs "
    f"{comparison_result['company_2']['coding_questions']}"
)

print(
    f"Subject Questions : "
    f"{comparison_result['company_1']['subject_questions']} vs "
    f"{comparison_result['company_2']['subject_questions']}"
)

print(
    f"SQL Questions : "
    f"{comparison_result['company_1']['sql_questions']} vs "
    f"{comparison_result['company_2']['sql_questions']}"
)

print(
    f"HR Questions : "
    f"{comparison_result['company_1']['hr_questions']} vs "
    f"{comparison_result['company_2']['hr_questions']}"
)

print(
    f"Interview Rounds : "
    f"{comparison_result['company_1']['interview_rounds']} vs "
    f"{comparison_result['company_2']['interview_rounds']}"
)

print(
    f"Puzzles : "
    f"{comparison_result['company_1']['puzzles']} vs "
    f"{comparison_result['company_2']['puzzles']}"
)

print("\n" + "=" * 60)

# ==========================================================
# Topic Frequency Comparison
# ==========================================================

print("Topic Frequency Comparison")
print("-" * 60)

result = comparison.compare_topic_frequency(
    company_1,
    company_2,
)

for topic, counts in sorted(
    result["comparison"].items(),
)[:10]:
    print(f"{topic}: {counts[company_1]} vs {counts[company_2]}")

print("\n" + "=" * 60)

# ==========================================================
# Difficulty Distribution Comparison
# ==========================================================

print("Difficulty Distribution Comparison")
print("-" * 60)

result = comparison.compare_difficulty_distribution(
    company_1,
    company_2,
)

for difficulty, counts in result["comparison"].items():
    print(f"{difficulty}: {counts[company_1]} vs {counts[company_2]}")

print("\n" + "=" * 60)

# ==========================================================
# Interview Pattern Comparison
# ==========================================================

print("Interview Pattern Comparison")
print("-" * 60)

result = comparison.compare_interview_pattern(
    company_1,
    company_2,
)

for round_type, counts in result["comparison"].items():
    print(f"{round_type}: {counts[company_1]} vs {counts[company_2]}")

print("\n" + "=" * 60)

# ==========================================================
# HR Pattern Comparison
# ==========================================================

print("HR Pattern Comparison")
print("-" * 60)

result = comparison.compare_hr_patterns(
    company_1,
    company_2,
)

for category, counts in result["comparison"].items():
    print(f"{category}: {counts[company_1]} vs {counts[company_2]}")

print("\n" + "=" * 60)

# ==========================================================
# Company Strength Comparison
# ==========================================================

print("Company Strength Comparison")
print("-" * 60)

result = comparison.compare_company_strengths(
    company_1,
    company_2,
)

for company_key in ["company_1", "company_2"]:
    company = result[company_key]

    print(f"\n{company['company']}")

    print(f"Dominant Difficulty : {company['dominant_difficulty']}")

    print(f"Most Common Round : {company['most_common_round']}")

    print(f"Most Common HR Category : {company['most_common_hr_category']}")

    print("Top Topics:")

    for topic, count in company["strongest_topics"].items():
        print(f"  {topic}: {count}")

print("\n" + "=" * 60)
print("Comparison Service Test Completed Successfully")
print("=" * 60)
