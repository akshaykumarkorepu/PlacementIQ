from placementiq.ai.state.agent_state import AgentState
from placementiq.knowledge.analytics import AnalyticsService
from placementiq.knowledge.context import ContextService
from placementiq.knowledge.retrieval import RetrievalService
from placementiq.repository.knowledge_repository import KnowledgeRepository


class ContextAgent:
    def __init__(self):
        repository = KnowledgeRepository()
        retrieval_service = RetrievalService(repository)
        analytics_service = AnalyticsService(retrieval_service)
        self.context_service = ContextService(analytics_service)

    def execute(self, state: AgentState) -> AgentState:

        companies = state.get("companies", [])
        topics = state.get("topics", [])
        search_category = state.get("search_category", "")

        # When no companies were extracted, fall back to the
        # companies discovered by a previous step (search or
        # analytics) so global search flows still receive
        # per-company context.

        if not companies:
            search_results = state.get("search_result") or {}
            analytics_results = state.get("analytics_result") or {}

            discovered = []

            for company in search_results.keys():
                if company and company not in discovered:
                    discovered.append(company)

            for company in analytics_results.keys():
                if company and company not in discovered:
                    discovered.append(company)

            companies = discovered

        if not companies:
            state["errors"].append("No companies found for context generation.")
            return state

        context_results = {}

        for company in companies:
            try:
                if search_category == "coding":
                    if not topics:
                        state["errors"].append("No coding topic found.")
                        continue

                    context = self.context_service.get_topic_context(
                        company,
                        topics[0],
                    )

                elif search_category == "subject":
                    if not topics:
                        state["errors"].append("No subject found.")
                        continue

                    context = self.context_service.get_subject_context(
                        company,
                        topics[0],
                    )

                elif search_category == "sql":
                    context = self.context_service.get_sql_context(
                        company,
                    )

                elif search_category == "hr":
                    context = self.context_service.get_hr_context(
                        company,
                    )

                elif search_category == "rounds":
                    context = self.context_service.get_round_context(
                        company,
                    )

                else:
                    context = self.context_service.get_company_context(
                        company,
                    )

                context_results[company] = context

            except Exception as e:
                state["errors"].append(
                    f"Failed to generate context for '{company}': {e}"
                )

        state["context_result"] = context_results

        return state
