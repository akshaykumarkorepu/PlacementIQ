"""
Test the complete PlacementIQ LangGraph workflow.
"""

from pprint import pprint

from placementiq.ai.graph.builder import create_graph
from placementiq.ai.state.agent_state import AgentState


graph = create_graph()


TEST_QUERIES = [
    "Show Oracle Dynamic Programming questions.",
    "Tell me about Oracle interview process.",
    "Which company asks Dynamic Programming most frequently?",
    "Compare Oracle and Microsoft.",
]


def status(value):
    """Return a checkmark if data exists, otherwise a dash."""
    return "✅" if value else "—"


for i, query in enumerate(TEST_QUERIES, start=1):
    print("\n" + "=" * 100)
    print(f"TEST CASE {i}")
    print("=" * 100)
    print(f"USER QUERY:\n{query}")

    initial_state: AgentState = {
        "user_query": query,
        "intent": "",
        "companies": [],
        "topics": [],
        "search_category": "",
        "execution_plan": [],
        "retrieval_result": {},
        "analytics_result": {},
        "search_result": [],
        "comparison_result": {},
        "evidence_result": [],
        "context_result": {},
        "final_answer": "",
        "errors": [],
    }

    result = graph.invoke(initial_state)

    print("\nPIPELINE SUMMARY")
    print("-" * 100)
    print(f"Intent            : {result['intent']}")
    print(f"Companies         : {result['companies']}")
    print(f"Topics            : {result['topics']}")
    print(f"Search Category   : {result['search_category']}")

    execution = (
        " → ".join(result["execution_plan"]) if result["execution_plan"] else "None"
    )
    print(f"Execution Plan    : {execution}")

    print("\nAGENT OUTPUTS")
    print("-" * 100)
    print(f"Retrieval Agent   : {status(result['retrieval_result'])}")
    print(f"Search Agent      : {status(result['search_result'])}")
    print(f"Analytics Agent   : {status(result['analytics_result'])}")
    print(f"Comparison Agent  : {status(result['comparison_result'])}")
    print(f"Evidence Agent    : {status(result['evidence_result'])}")
    print(f"Context Agent     : {status(result['context_result'])}")

    print("\nRESULT COUNTS")
    print("-" * 100)
    print(f"Retrieved Companies : {len(result['retrieval_result'])}")
    print(f"Search Results      : {len(result['search_result'])}")
    print(f"Analytics Summaries : {len(result['analytics_result'])}")
    print(f"Comparisons         : {len(result['comparison_result'])}")
    print(f"Evidence Items      : {len(result['evidence_result'])}")

    print("\nERRORS")
    print("-" * 100)
    if result["errors"]:
        pprint(result["errors"])
    else:
        print("None")

    print("\nFINAL ANSWER")
    print("-" * 100)
    print(result["final_answer"] or "No answer generated.")

    print("\n" + "=" * 100)
