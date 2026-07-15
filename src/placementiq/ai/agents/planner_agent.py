"""
PlacementIQ Planner Agent

Analyzes a user query and generates a structured execution plan
using Groq.
"""

import json
import os

from dotenv import load_dotenv
from groq import Groq

from placementiq.ai.prompts.planner_prompt import PLANNER_PROMPT
from placementiq.ai.state.agent_state import AgentState

# Load environment variables from .env
load_dotenv()


class PlannerAgent:
    """
    Uses an LLM to convert a user query into
    a structured execution plan.
    """

    def __init__(self):
        """
        Initialize the Planner Agent.
        """

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found. Please add it to your .env file.")

        self.client = Groq(api_key=api_key)

        self.model = os.getenv(
            "GROQ_MODEL",
            "llama-3.3-70b-versatile",
        )

        self.system_prompt = PLANNER_PROMPT

    def plan(self, state: AgentState) -> AgentState:
        """
        Analyze the user's query and update the shared
        AgentState with the execution plan.
        """

        try:
            # ------------------------------------
            # Read user query
            # ------------------------------------

            user_query = state["user_query"]

            # ------------------------------------
            # Call Groq
            # ------------------------------------

            response = self.client.chat.completions.create(
                model=self.model,
                temperature=0,
                response_format={"type": "json_object"},
                messages=[
                    {
                        "role": "system",
                        "content": self.system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_query,
                    },
                ],
            )

            response_text = response.choices[0].message.content

            if not response_text:
                raise ValueError("Groq returned an empty response.")

            # ------------------------------------
            # Parse JSON response
            # ------------------------------------

            planning = json.loads(response_text)

            # ------------------------------------
            # Update AgentState
            # ------------------------------------

            state["intent"] = planning.get("intent", "")
            state["companies"] = planning.get("companies", [])
            state["topics"] = planning.get("topics", [])
            state["search_category"] = planning.get("search_category", "")
            state["execution_plan"] = planning.get("execution_plan", [])

            return state

        except json.JSONDecodeError as e:
            raise ValueError("Failed to parse planning JSON returned by Groq.") from e

        except ValueError:
            raise

        except Exception as e:
            raise RuntimeError(f"Planner execution failed: {e}") from e
