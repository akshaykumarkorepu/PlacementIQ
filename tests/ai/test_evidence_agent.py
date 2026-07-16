from pprint import pprint

from placementiq.ai.agents.evidence_agent import EvidenceAgent
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
        "intent": "evidence",
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

    agent = EvidenceAgent()

    result = agent.execute(state)

    print("EVIDENCE RESULT\n")
    pprint(result["evidence_result"])

    print("\nERRORS\n")
    pprint(result["errors"])

    print("=" * 100)
    print()


if __name__ == "__main__":
    # Test 1
    run_test(
        user_query="Show evidence for Oracle Dynamic Programming questions.",
        company="Oracle",
        topic="Dynamic Programming",
        category="coding",
    )

    # Test 2
    run_test(
        user_query="Show evidence for Oracle DBMS questions.",
        company="Oracle",
        topic="DBMS",
        category="subject",
    )
