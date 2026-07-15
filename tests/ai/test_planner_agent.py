"""
Tests for the PlannerAgent.

This script validates that the Planner Agent correctly
converts different natural language queries into
structured execution plans.
"""

from placementiq.ai.agents.planner_agent import PlannerAgent
from placementiq.ai.state.agent_state import AgentState


def create_state(query: str) -> AgentState:
    """
    Create a fresh AgentState for testing.
    """

    return {
        # User Input
        "user_query": query,
        # Planner Output
        "intent": "",
        "companies": [],
        "topics": [],
        "search_category": "",
        "execution_plan": [],
        # Tool Outputs
        "retrieval_result": {},
        "analytics_result": {},
        "search_result": [],
        "comparison_result": {},
        "evidence_result": [],
        "context_result": {},
        # Final Output
        "final_answer": "",
        # System
        "errors": [],
    }


def main():

    planner = PlannerAgent()

    test_queries = [
        "Show Oracle Dynamic Programming questions.",
        "Show Oracle DBMS questions.",
        "Show Oracle SQL JOIN questions.",
        "Show Oracle HR questions.",
        "Show Oracle interview rounds.",
        "Show Oracle puzzles.",
    ]

    for query in test_queries:
        print("=" * 100)
        print(f"USER QUERY:\n{query}\n")

        state = create_state(query)

        updated_state = planner.plan(state)

        print("PLANNER OUTPUT\n")

        print(f"Intent            : {updated_state['intent']}")
        print(f"Companies         : {updated_state['companies']}")
        print(f"Topics            : {updated_state['topics']}")
        print(f"Search Category   : {updated_state['search_category']}")
        print(f"Execution Plan    : {updated_state['execution_plan']}")

        print()


if __name__ == "__main__":
    main()
