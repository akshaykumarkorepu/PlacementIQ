from pprint import pprint

from placementiq.ai.agents.context_agent import ContextAgent
from placementiq.ai.state.agent_state import AgentState


def run_test(
    user_query: str,
    company: str,
    topic: str,
    category: str,
):
    print("=" * 100)
    print(f"USER QUERY:\n{user_query}\n")

    state: AgentState = {
        "user_query": user_query,
        "intent": "context",
        "companies": [company],
        "topics": [topic],
        "search_category": category,
        "execution_plan": [],
        "retrieval_result": {},
        "search_result": {},
        "analytics_result": {},
        "comparison_result": {},
        "evidence_result": {},
        "context_result": {},
        "final_answer": "",
        "errors": [],
    }

    agent = ContextAgent()

    result = agent.execute(state)

    print("CONTEXT RESULT\n")
    pprint(result["context_result"])

    print("\nERRORS\n")
    pprint(result["errors"])

    print("=" * 100)
    print()


if __name__ == "__main__":
    # Test 1 - Coding Topic Context
    run_test(
        user_query="Show Oracle Dynamic Programming context.",
        company="Oracle",
        topic="Dynamic Programming",
        category="coding",
    )

    # Test 2 - Overall Company Context
    run_test(
        user_query="Tell me about Oracle.",
        company="Oracle",
        topic="",
        category="",
    )
