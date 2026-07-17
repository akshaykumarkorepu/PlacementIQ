"""
PlacementIQ LangGraph Builder

Compiles the workflow into an executable LangGraph.

This module is responsible for creating the final graph
that can be executed using graph.invoke().
"""

from placementiq.ai.graph.workflow import build_workflow


def create_graph():
    """
    Build and compile the PlacementIQ LangGraph.
    """

    workflow = build_workflow()

    graph = workflow.compile()

    return graph
