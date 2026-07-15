from placementiq.ai.state.agent_state import AgentState
from placementiq.knowledge.retrieval import RetrievalService
from placementiq.repository.knowledge_repository import KnowledgeRepository


class RetrievalAgent:
    def __init__(self):
        repository = KnowledgeRepository()
        self.retrieval_service = RetrievalService(repository)

    def execute(self, state: AgentState) -> AgentState:

        companies = state.get("companies", [])

        if not companies:
            state["errors"].append("No companies found for retrieval.")
            return state

        retrieval_results = {}

        for company in companies:
            try:
                experiences = self.retrieval_service.get_company_experiences(company)

                retrieval_results[company] = experiences

            except Exception as e:
                state["errors"].append(f"Failed to retrieve '{company}': {e}")

        state["retrieval_result"] = retrieval_results

        return state
