from pprint import pprint

from placementiq.ai.agents.comparison_agent import ComparisonAgent
from placementiq.ai.state.agent_state import AgentState


def run_test(
    user_query: str,
    company_1: str,
    company_2: str,
):
    print("=" * 100)
    print(f"USER QUERY:\n{user_query}\n")

    state: AgentState = {
        "user_query": user_query,
        "intent": "compare",
        "companies": [
            company_1,
            company_2,
        ],
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

    agent = ComparisonAgent()

    result = agent.execute(state)

    print("COMPARISON RESULT\n")
    pprint(result["comparison_result"])

    print("\nERRORS\n")
    pprint(result["errors"])

    print("=" * 100)
    print()


if __name__ == "__main__":
    run_test(
        user_query="Compare Oracle and Microsoft.",
        company_1="Oracle",
        company_2="Microsoft",
    )

    run_test(
        user_query="Compare Amazon and Goldman Sachs.",
        company_1="Amazon",
        company_2="Goldman Sachs",
    )
