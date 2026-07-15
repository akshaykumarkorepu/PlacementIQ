"""
Tests for the PlannerAgent.

This script validates that the Planner Agent correctly
converts different natural language queries into
structured execution plans.
"""

from pprint import pprint

from placementiq.ai.agents.planner_agent import PlannerAgent
from placementiq.ai.state.agent_state import AgentState


def create_state(query: str) -> AgentState:
    """
    Create a fresh AgentState for testing.
    """

    return {
        "user_query": query,
        "intent": "",
        "companies": [],
        "topics": [],
        "execution_plan": [],
        "retrieval_result": [],
        "analytics_result": {},
        "search_result": [],
        "comparison_result": {},
        "evidence_result": [],
        "context_result": {},
        "final_answer": "",
        "errors": [],
    }


def main():

    planner = PlannerAgent()

    test_queries = [
        "Compare Oracle and Microsoft and show evidence.",
        "Show Oracle SQL questions.",
        "Show Dynamic Programming questions.",
        "What are the most common DBMS topics in Oracle interviews?",
        "How much Oracle interview data do you have?",
    ]

    for query in test_queries:
        print("=" * 100)
        print(f"USER QUERY:\n{query}\n")

        state = create_state(query)

        updated_state = planner.plan(state)

        print("PLANNER OUTPUT:\n")

        pprint(updated_state)

        print()


if __name__ == "__main__":
    main()
