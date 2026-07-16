from placementiq.ai.state.agent_state import AgentState
from placementiq.knowledge.retrieval import RetrievalService
from placementiq.knowledge.search import SearchService
from placementiq.repository.knowledge_repository import KnowledgeRepository


class SearchAgent:
    def __init__(self):
        repository = KnowledgeRepository()
        retrieval_service = RetrievalService(repository)
        self.search_service = SearchService(retrieval_service)

    def execute(self, state: AgentState) -> AgentState:

        companies = state.get("companies", [])
        topics = state.get("topics", [])
        search_category = state.get("search_category", "")

        if not topics:
            state["errors"].append("No search topics found.")
            return state

        if not search_category:
            state["errors"].append("No search category found.")
            return state

        if companies:
            logger_message = "Performing company-specific search."
        else:
            logger_message = "Performing global search across all companies."

        print(logger_message)

        try:
            search_results = self.search_service.search(
                search_category,
                companies,
                topics,
            )

        except Exception as e:
            state["errors"].append(
                f"Search failed: {e}"
            )
            return state

        state["search_result"] = search_results

        return state
