from placementiq.repository.knowledge_repository import KnowledgeRepository
from placementiq.knowledge.retrieval import RetrievalService

repo = KnowledgeRepository()
service = RetrievalService(repo)

print("=" * 60)
print("Retrieval Service Tests")
print("=" * 60)

oracle = service.get_coding_questions("Oracle")
print(f"Oracle Coding Questions: {len(oracle)}")

empty = service.get_coding_questions("")
print(f"Empty Company: {empty}")

whitespace = service.get_coding_questions("   Oracle   ")
print(f"Whitespace Company: {len(whitespace)}")

unknown = service.get_coding_questions("UnknownCompany")
print(f"Unknown Company: {len(unknown)}")
