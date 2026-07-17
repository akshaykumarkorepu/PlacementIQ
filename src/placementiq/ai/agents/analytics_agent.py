from placementiq.ai.state.agent_state import AgentState
from placementiq.knowledge.analytics import AnalyticsService
from placementiq.knowledge.retrieval import RetrievalService
from placementiq.repository.knowledge_repository import KnowledgeRepository


class AnalyticsAgent:
    def __init__(self):
        repository = KnowledgeRepository()
        retrieval_service = RetrievalService(repository)
        self.analytics_service = AnalyticsService(retrieval_service)

    def execute(self, state: AgentState) -> AgentState:

        companies = state.get("companies", [])

        if not companies:
            companies = self.analytics_service.get_all_companies()

        analytics_results = {}

        for company in companies:
            try:
                summary = self.analytics_service.get_company_summary(company)

                analytics_results[company] = summary

            except Exception as e:
                state["errors"].append(
                    f"Failed to compute analytics for '{company}': {e}"
                )

        state["analytics_result"] = analytics_results

        return state
