"""
PlacementIQ LangGraph Nodes

This module adapts the existing AI Agents into LangGraph Nodes.

IMPORTANT:
The agents themselves remain unchanged.
Each node simply delegates execution to its corresponding agent.
"""

from placementiq.ai.agents.analytics_agent import AnalyticsAgent
from placementiq.ai.agents.answer_agent import AnswerAgent
from placementiq.ai.agents.comparison_agent import ComparisonAgent
from placementiq.ai.agents.context_agent import ContextAgent
from placementiq.ai.agents.evidence_agent import EvidenceAgent
from placementiq.ai.agents.planner_agent import PlannerAgent
from placementiq.ai.agents.retrieval_agent import RetrievalAgent
from placementiq.ai.agents.search_agent import SearchAgent
from placementiq.ai.state.agent_state import AgentState

# ------------------------------------------------------------------
# Singleton Agent Instances
# ------------------------------------------------------------------

planner_agent = PlannerAgent()
retrieval_agent = RetrievalAgent()
search_agent = SearchAgent()
analytics_agent = AnalyticsAgent()
comparison_agent = ComparisonAgent()
evidence_agent = EvidenceAgent()
context_agent = ContextAgent()
answer_agent = AnswerAgent()


# ------------------------------------------------------------------
# LangGraph Nodes
# ------------------------------------------------------------------


def planner_node(state: AgentState) -> AgentState:
    """Execute the Planner Agent."""
    return planner_agent.plan(state)


def retrieval_node(state: AgentState) -> AgentState:
    """Execute the Retrieval Agent."""
    return retrieval_agent.execute(state)


def search_node(state: AgentState) -> AgentState:
    """Execute the Search Agent."""
    return search_agent.execute(state)


def analytics_node(state: AgentState) -> AgentState:
    """Execute the Analytics Agent."""
    return analytics_agent.execute(state)


def comparison_node(state: AgentState) -> AgentState:
    """Execute the Comparison Agent."""
    return comparison_agent.execute(state)


def evidence_node(state: AgentState) -> AgentState:
    """Execute the Evidence Agent."""
    return evidence_agent.execute(state)


def context_node(state: AgentState) -> AgentState:
    """Execute the Context Agent."""
    return context_agent.execute(state)


def answer_node(state: AgentState) -> AgentState:
    """Execute the Answer Agent."""
    return answer_agent.execute(state)
