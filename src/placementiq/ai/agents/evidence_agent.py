from placementiq.ai.state.agent_state import AgentState
from placementiq.knowledge.evidence import EvidenceService
from placementiq.knowledge.retrieval import RetrievalService
from placementiq.repository.knowledge_repository import KnowledgeRepository

import logging

logger = logging.getLogger(__name__)


class EvidenceAgent:
    def __init__(self):
        repository = KnowledgeRepository()
        retrieval_service = RetrievalService(repository)
        self.evidence_service = EvidenceService(retrieval_service)

    def execute(self, state: AgentState) -> AgentState:

        companies = state.get("companies", [])
        topics = state.get("topics", [])
        search_category = state.get("search_category", "")

        # When no companies were extracted, fall back to the
        # companies discovered by the search step so global
        # search flows still receive supporting evidence.

        if not companies:
            search_results = state.get("search_result") or {}
            companies = [company for company in search_results.keys() if company]

        if not companies:
            logger.info("Skipping EvidenceAgent: no companies available.")
            return state

        if not topics:
            logger.info("Skipping EvidenceAgent: no topics available.")
            return state

        if not search_category:
            logger.info("Skipping EvidenceAgent: no search category available.")
            return state

        evidence_results = {}

        for company in companies:
            company_evidence = []

            for topic in topics:
                try:
                    if search_category == "coding":
                        evidence = self.evidence_service.get_coding_evidence(
                            company,
                            topic,
                        )

                    elif search_category == "subject":
                        evidence = self.evidence_service.get_subject_evidence(
                            company,
                            topic,
                        )

                    elif search_category == "sql":
                        evidence = self.evidence_service.get_sql_evidence(
                            company,
                            topic,
                        )

                    elif search_category == "hr":
                        evidence = self.evidence_service.get_hr_evidence(
                            company,
                            topic,
                        )

                    elif search_category == "rounds":
                        evidence = self.evidence_service.get_round_evidence(
                            company,
                            topic,
                        )

                    elif search_category == "puzzles":
                        evidence = self.evidence_service.get_puzzle_evidence(
                            company,
                            topic,
                        )

                    else:
                        state["errors"].append(
                            f"Unknown search category: {search_category}"
                        )
                        return state

                    company_evidence.extend(evidence)

                except Exception as e:
                    state["errors"].append(
                        f"Failed to retrieve evidence for '{company}' and '{topic}': {e}"
                    )

            evidence_results[company] = company_evidence

        state["evidence_result"] = evidence_results

        return state
