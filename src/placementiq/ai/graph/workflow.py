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
    answer_node,
)


def build_workflow():
    """
    Build the PlacementIQ LangGraph workflow.

    Initial Workflow:

        START
          │
          ▼
      Planner
          │
          ▼
       Answer
          │
          ▼
         END
    """

    # Create a graph that passes around AgentState
    workflow = StateGraph(AgentState)

    # Register nodes
    workflow.add_node("planner", planner_node)
    workflow.add_node("answer", answer_node)

    # Define execution flow
    workflow.add_edge(START, "planner")
    workflow.add_edge("planner", "answer")
    workflow.add_edge("answer", END)

    return workflow
