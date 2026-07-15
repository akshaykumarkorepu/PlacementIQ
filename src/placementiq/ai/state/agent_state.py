from typing import Any, TypedDict


class AgentState(TypedDict):
    """
    Shared state passed between all AI agents.

    Each agent reads from this state,
    updates the relevant fields,
    and returns the updated state.
    """

    # ==========================
    # User Input
    # ==========================

    user_query: str

    # ==========================
    # Planner Output
    # ==========================

    intent: str
    companies: list[str]
    topics: list[str]
    search_category: str
    execution_plan: list[str]

    # ==========================
    # Tool Outputs
    # ==========================

    retrieval_result: dict[str, list[dict[str, Any]]]
    analytics_result: dict[str, Any]
    search_result: list[dict[str, Any]]
    comparison_result: dict[str, Any]
    evidence_result: list[dict[str, Any]]
    context_result: dict[str, Any]

    # ==========================
    # Final Output
    # ==========================

    final_answer: str

    # ==========================
    # System
    # ==========================

    errors: list[str]
