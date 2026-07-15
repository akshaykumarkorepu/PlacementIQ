from placementiq.ai.agents.planner_agent import PlannerAgent
from placementiq.ai.agents.retrieval_agent import RetrievalAgent
from placementiq.ai.state.agent_state import AgentState


def main():
    # Create the initial AgentState
    state: AgentState = {
        "user_query": "Show Oracle interview experiences.",
        # Planner Output
        "intent": "",
        "companies": [],
        "topics": [],
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

    # Run Planner
    planner = PlannerAgent()
    state = planner.plan(state)

    # Run Retrieval Agent
    retrieval_agent = RetrievalAgent()
    state = retrieval_agent.execute(state)

    print("=" * 80)
    print("RETRIEVAL AGENT TEST")
    print("=" * 80)

    print(f"Intent              : {state['intent']}")
    print(f"Companies           : {state['companies']}")
    print(f"Execution Plan      : {state['execution_plan']}")

    print()

    for company, experiences in state["retrieval_result"].items():
        print(f"{company} Experiences : {len(experiences)}")

    print()

    if state["errors"]:
        print("Errors:")
        for error in state["errors"]:
            print(f"  - {error}")
    else:
        print("Errors              : None")

    print("\n✅ Retrieval Agent working successfully!")


if __name__ == "__main__":
    main()
