"""
PlacementIQ Answer Agent

Generates the final natural language response
using the outputs produced by the Tool Agents.
"""

import os

from dotenv import load_dotenv
from groq import Groq

from placementiq.ai.prompts.answer_prompt import ANSWER_PROMPT
from placementiq.ai.state.agent_state import AgentState
from placementiq.ai.utils.prompt_builder import build_answer_context

# Load environment variables
load_dotenv()


class AnswerAgent:
    """
    Uses an LLM to generate the final response
    from the information collected by all Tool Agents.
    """

    def __init__(self):
        """
        Initialize the Answer Agent.
        """

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found. Please add it to your .env file.")

        self.client = Groq(api_key=api_key)

        self.model = os.getenv(
            "GROQ_MODEL",
            "llama-3.3-70b-versatile",
        )

        self.system_prompt = ANSWER_PROMPT

    def execute(self, state: AgentState) -> AgentState:
        """
        Generate the final answer for the user.

        Args:
            state:
                Shared AgentState containing outputs
                from all previously executed agents.

        Returns:
            Updated AgentState containing final_answer.
        """

        try:
            prompt_context = build_answer_context(state)

            user_prompt = f"""
User Question:

{state.get("user_query", "")}

Available Information:

{prompt_context}
"""

            response = self.client.chat.completions.create(
                model=self.model,
                temperature=0.2,
                messages=[
                    {
                        "role": "system",
                        "content": self.system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
                    },
                ],
            )

            answer = response.choices[0].message.content

            if not answer:
                raise ValueError("Groq returned an empty response.")

            state["final_answer"] = answer.strip()

            return state

        except ValueError:
            raise

        except Exception as e:
            raise RuntimeError(f"Answer generation failed: {e}") from e
