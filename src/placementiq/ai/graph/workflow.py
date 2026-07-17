"""
PlacementIQ LangGraph Workflow

Defines the execution flow of the LangGraph.

This module only describes:
- What nodes exist
- How they are connected

It does NOT execute or compile the graph.
"""

from langgraph.graph import StateGraph, START, END

from placementiq.ai.state.agent_state import AgentState

from placementiq.ai.graph.nodes import (
    planner_node,
    retrieval_node,
    search_node,
    analytics_node,
    comparison_node,
    evidence_node,
    context_node,
    answer_node,
)

from placementiq.ai.graph.router import route_after_planner


def build_workflow():

    # Create a graph that passes around AgentState
    workflow = StateGraph(AgentState)

    # Register nodes
    workflow.add_node("planner", planner_node)
    workflow.add_node("retrieval", retrieval_node)
    workflow.add_node("search", search_node)
    workflow.add_node("analytics", analytics_node)
    workflow.add_node("comparison", comparison_node)
    workflow.add_node("evidence", evidence_node)
    workflow.add_node("context", context_node)
    workflow.add_node("answer", answer_node)

    # Start the workflow
    workflow.add_edge(START, "planner")

    # Route dynamically after planner
    workflow.add_conditional_edges(
        "planner",
        route_after_planner,
    )

    # Every specialized branch goes to Evidence
    workflow.add_edge("search", "evidence")
    workflow.add_edge("retrieval", "evidence")
    workflow.add_edge("analytics", "evidence")
    workflow.add_edge("comparison", "evidence")

    # Evidence enriches the response before context building
    workflow.add_edge("evidence", "context")

    # Context prepares the final prompt
    workflow.add_edge("context", "answer")

    # End the workflow
    workflow.add_edge("answer", END)

    return workflow
