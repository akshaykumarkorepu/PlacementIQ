from placementiq.ai.state.agent_state import AgentState


def build_answer_context(state: AgentState) -> str:
    """
    Convert the AgentState into a structured text prompt
    for the Answer Agent.

    This keeps prompt formatting separate from the
    AnswerAgent itself.
    """

    sections = []

    sections.append(f"User Question:\n{state.get('user_query', '')}")

    retrieval = state.get("retrieval_result")
    if retrieval:
        sections.append(f"Retrieved Interview Experiences:\n{retrieval}")

    search = state.get("search_result")
    if search:
        sections.append(f"Search Results:\n{search}")

    analytics = state.get("analytics_result")
    if analytics:
        sections.append(f"Analytics:\n{analytics}")

    comparison = state.get("comparison_result")
    if comparison:
        sections.append(f"Comparison:\n{comparison}")

    evidence = state.get("evidence_result")
    if evidence:
        sections.append(f"Supporting Evidence:\n{evidence}")

    context = state.get("context_result")
    if context:
        sections.append(f"Dataset Context:\n{context}")

    return "\n\n".join(sections)
