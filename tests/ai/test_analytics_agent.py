from pprint import pprint

from placementiq.ai.agents.analytics_agent import AnalyticsAgent
from placementiq.ai.state.agent_state import AgentState


def run_test(
    user_query: str,
    company: str,
):
    print("=" * 100)
    print(f"USER QUERY:\n{user_query}\n")

    state: AgentState = {
        "user_query": user_query,
        "intent": "analytics",
        "companies": [company],
        "topics": [],
        "search_category": "",
        "execution_plan": [],
        "retrieval_result": {},
        "search_result": {},
        "analytics_result": {},
        "comparison_result": {},
        "evidence_result": [],
        "context_result": {},
        "final_answer": "",
        "errors": [],
    }

    agent = AnalyticsAgent()

    result = agent.execute(state)

    print("ANALYTICS RESULT\n")
    pprint(result["analytics_result"])

    print("\nERRORS\n")
    pprint(result["errors"])

    print("=" * 100)
    print()


if __name__ == "__main__":
    run_test(
        user_query="Show Oracle interview analytics.",
        company="Oracle",
    )

    run_test(
        user_query="Show Microsoft interview analytics.",
        company="Microsoft",
    )
