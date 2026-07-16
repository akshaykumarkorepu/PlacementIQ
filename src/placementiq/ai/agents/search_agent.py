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

        if not companies:
            state["errors"].append("No companies found for search.")
            return state

        if not topics:
            state["errors"].append("No search topics found.")
            return state

        if not search_category:
            state["errors"].append("No search category found.")
            return state

        search_results = {}

        for company in companies:
            company_results = []

            for topic in topics:
                try:
                    if search_category == "coding":
                        results = self.search_service.search_coding_questions(
                            company,
                            topic,
                        )

                    elif search_category == "subject":
                        results = self.search_service.search_subject_questions(
                            company,
                            topic,
                        )

                    elif search_category == "sql":
                        results = self.search_service.search_sql_questions(
                            company,
                            topic,
                        )

                    elif search_category == "hr":
                        results = self.search_service.search_hr_questions(
                            company,
                            topic,
                        )

                    elif search_category == "rounds":
                        results = self.search_service.search_rounds(
                            company,
                            topic,
                        )

                    elif search_category == "puzzles":
                        results = self.search_service.search_puzzles(
                            company,
                            topic,
                        )

                    else:
                        state["errors"].append(
                            f"Unknown search category: {search_category}"
                        )
                        return state

                    company_results.extend(results)

                except Exception as e:
                    state["errors"].append(
                        f"Failed to search '{company}' for '{topic}': {e}"
                    )

            search_results[company] = company_results

        state["search_result"] = search_results

        return state
