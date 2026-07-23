"""Service layer that exposes the PlacementIQ AI to the web layer."""

from __future__ import annotations

from placementiq.ai.graph.builder import create_graph
from placementiq.ai.state.agent_state import AgentState


class AIService:
    """Thin wrapper around the AI system (currently stubbed)."""

    def __init__(self) -> None:
        """Compile the LangGraph once so request handlers reuse the same instance."""
        self.graph = create_graph()

    def ask(self, question: str) -> dict[str, str]:
        """Return a canned response for the given question."""
        state: AgentState = {
            "user_query": question,
            "intent": "",
            "companies": [],
            "topics": [],
            "search_category": "",
            "execution_plan": [],
            "retrieval_result": {},
            "analytics_result": {},
            "search_result": [],
            "comparison_result": {},
            "evidence_result": [],
            "context_result": {},
            "final_answer": "",
            "errors": [],
        }
        result = self.graph.invoke(state)

        return {
            "answer": result["final_answer"],
            "intent": result["intent"],
        }
