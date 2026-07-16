from placementiq.ai.agents.analytics_agent import AnalyticsAgent
from placementiq.ai.agents.answer_agent import AnswerAgent
from placementiq.ai.agents.comparison_agent import ComparisonAgent
from placementiq.ai.agents.context_agent import ContextAgent
from placementiq.ai.agents.evidence_agent import EvidenceAgent
from placementiq.ai.agents.planner_agent import PlannerAgent
from placementiq.ai.agents.retrieval_agent import RetrievalAgent
from placementiq.ai.agents.search_agent import SearchAgent
from placementiq.ai.state.agent_state import AgentState


def run_query(query: str):
    print("=" * 120)
    print("USER QUERY")
    print("-" * 120)
    print(query)
    print()

    state: AgentState = {
        "user_query": query,
        "intent": "",
        "companies": [],
        "topics": [],
        "search_category": "",
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

    planner = PlannerAgent()
    retrieval = RetrievalAgent()
    search = SearchAgent()
    analytics = AnalyticsAgent()
    comparison = ComparisonAgent()
    evidence = EvidenceAgent()
    context = ContextAgent()
    answer = AnswerAgent()

    # ----------------------------------------------------
    # Planner
    # ----------------------------------------------------

    state = planner.plan(state)

    print("PLANNER")
    print("-" * 120)
    print(f"Intent          : {state['intent']}")
    print(f"Companies       : {state['companies']}")
    print(f"Topics          : {state['topics']}")
    print(f"Search Category : {state['search_category']}")
    print(f"Execution Plan  : {state['execution_plan']}")
    print()

    # ----------------------------------------------------
    # Execute Tool Agents
    # ----------------------------------------------------

    for step in state["execution_plan"]:
        print(f"> Executing {step}...")

        if step == "retrieval":
            state = retrieval.execute(state)

        elif step == "search":
            state = search.execute(state)

        elif step == "analytics":
            state = analytics.execute(state)

        elif step == "comparison":
            state = comparison.execute(state)

        elif step == "evidence":
            state = evidence.execute(state)

        elif step == "context":
            state = context.execute(state)

    # ----------------------------------------------------
    # Answer
    # ----------------------------------------------------

    state = answer.execute(state)

    print()
    print("=" * 120)
    print("FINAL ANSWER")
    print("-" * 120)
    print(state["final_answer"])

    print()
    print("SEARCH RESULT (per company)")
    print("-" * 120)
    for company, results in (state.get("search_result") or {}).items():
        print(f"{company}: {len(results)} record(s)")

    print()
    print("ERRORS")
    print("-" * 120)
    print(state["errors"])

    print("=" * 120)
    print()


if __name__ == "__main__":
    # ----------------------------------------------------
    # Test 1: Global search
    # Expected: Planner -> Search -> Evidence -> Context -> Answer
    # ----------------------------------------------------

    run_query("Where was LRU Cache asked?")

    # ----------------------------------------------------
    # Test 2: Company comparison
    # Expected: Planner -> Comparison -> Analytics -> Context -> Answer
    # ----------------------------------------------------

    run_query("Compare Oracle and Microsoft.")

    # ----------------------------------------------------
    # Test 3: Preparation guidance (analytics)
    # Expected: Planner -> Analytics -> Evidence -> Context -> Answer
    # ----------------------------------------------------

    run_query("How should I prepare for Oracle interviews?")
