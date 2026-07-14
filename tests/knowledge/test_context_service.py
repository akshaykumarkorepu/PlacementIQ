from placementiq.knowledge.analytics import AnalyticsService
from placementiq.knowledge.context import ContextService
from placementiq.knowledge.retrieval import RetrievalService
from placementiq.repository.knowledge_repository import KnowledgeRepository

repository = KnowledgeRepository()
retrieval = RetrievalService(repository)
analytics = AnalyticsService(retrieval)
context = ContextService(analytics)

company = "Oracle"

print("=" * 60)
print("Context Service Tests")
print("=" * 60)

# ==========================================================
# Company Context
# ==========================================================

print("\nCompany Context")
print("-" * 60)

result = context.get_company_context(
    company,
)

print(f"Company               : {result['company']}")
print(f"Interview Experiences : {result['total_experiences']}")
print(f"Coding Questions      : {result['coding_questions']}")

print("\nDataset Context")
print("-" * 60)
print(result["context"])

print("\n" + "=" * 60)

# ==========================================================
# Topic Context
# ==========================================================

topic = "Dynamic Programming"

print("\nTopic Context")
print("-" * 60)

result = context.get_topic_context(
    company,
    topic,
)

print(f"Company               : {result['company']}")
print(f"Topic                 : {result['topic']}")
print(f"Interview Experiences : {result['total_experiences']}")
print(f"Topic Count           : {result['topic_count']}")

print("\nDataset Context")
print("-" * 60)
print(result["context"])

print("\n" + "=" * 60)

# ==========================================================
# Subject Context
# ==========================================================

subject = "DBMS"

print("\nSubject Context")
print("-" * 60)

result = context.get_subject_context(
    company,
    subject,
)

print(f"Company               : {result['company']}")
print(f"Subject               : {result['subject']}")
print(f"Interview Experiences : {result['total_experiences']}")
print(f"Subject Questions     : {result['subject_questions']}")

print("\nDataset Context")
print("-" * 60)
print(result["context"])

print("\n" + "=" * 60)

# ==========================================================
# SQL Context
# ==========================================================

print("\nSQL Context")
print("-" * 60)

result = context.get_sql_context(
    company,
)

print(f"Company               : {result['company']}")
print(f"Interview Experiences : {result['total_experiences']}")
print(f"SQL Questions         : {result['sql_questions']}")

print("\nDataset Context")
print("-" * 60)
print(result["context"])

print("\n" + "=" * 60)

# ==========================================================
# HR Context
# ==========================================================

print("\nHR Context")
print("-" * 60)

result = context.get_hr_context(
    company,
)

print(f"Company               : {result['company']}")
print(f"Interview Experiences : {result['total_experiences']}")
print(f"HR Questions          : {result['hr_questions']}")

print("\nDataset Context")
print("-" * 60)
print(result["context"])

print("\n" + "=" * 60)

# ==========================================================
# Interview Round Context
# ==========================================================

print("\nInterview Round Context")
print("-" * 60)

result = context.get_round_context(
    company,
)

print(f"Company               : {result['company']}")
print(f"Interview Experiences : {result['total_experiences']}")
print(f"Interview Rounds      : {result['interview_rounds']}")

print("\nDataset Context")
print("-" * 60)
print(result["context"])

print("\n" + "=" * 60)

print("Context Service Test Completed Successfully")
print("=" * 60)
