"""
Test the initial LangGraph workflow.
"""

from pprint import pprint

from placementiq.ai.graph.builder import create_graph
from placementiq.ai.state.agent_state import AgentState


graph = create_graph()


initial_state: AgentState = {
    "user_query": "Show Oracle Dynamic Programming questions.",
    "intent": "",
    "companies": [],
    "topics": [],
    "search_category": "",
    "execution_plan": [],
    "retrieval_result": {},
    "analytics_result": {},
    "search_result": [],  # ✅ list
    "comparison_result": {},
    "evidence_result": [],
    "context_result": {},
    "final_answer": "",
    "errors": [],
}


result = graph.invoke(initial_state)

print("\n" + "=" * 80)
print("LANGGRAPH EXECUTION RESULT")
print("=" * 80)

pprint(result)
