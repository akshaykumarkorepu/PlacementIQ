from placementiq.ai.state.agent_state import AgentState
from placementiq.knowledge.analytics import AnalyticsService
from placementiq.knowledge.comparison import ComparisonService
from placementiq.knowledge.retrieval import RetrievalService
from placementiq.repository.knowledge_repository import KnowledgeRepository


class ComparisonAgent:
    def __init__(self):
        repository = KnowledgeRepository()
        retrieval_service = RetrievalService(repository)
        analytics_service = AnalyticsService(retrieval_service)
        self.comparison_service = ComparisonService(analytics_service)

    def execute(self, state: AgentState) -> AgentState:

        companies = state.get("companies", [])

        if len(companies) < 2:
            state["errors"].append("Comparison requires at least two companies.")
            return state

        company_1 = companies[0]
        company_2 = companies[1]

        try:
            comparison = self.comparison_service.compare_companies(
                company_1,
                company_2,
            )

            state["comparison_result"] = comparison

        except Exception as e:
            state["errors"].append(
                f"Failed to compare '{company_1}' and '{company_2}': {e}"
            )

        return state
