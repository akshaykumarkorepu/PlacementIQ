"""
Routing logic for the LangGraph workflow.
"""

from placementiq.ai.state.agent_state import AgentState


def route_after_planner(state: AgentState) -> str:
    """
    Decide which node should execute next based on the planner's intent.
    """

    intent = state["intent"]

    if intent == "search":
        return "search"

    if intent == "retrieval":
        return "retrieval"

    if intent == "analytics":
        return "analytics"

    if intent == "comparison":
        return "comparison"

    # Fallback
    return "answer"
