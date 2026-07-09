"""
PlacementIQ Interview Extractor

Converts one normalized interview experience into
structured interview knowledge using Groq.
"""

import json
import os

from dotenv import load_dotenv
from groq import Groq

from placementiq.extraction.prompts.interview_extraction_prompt import (
    INTERVIEW_EXTRACTION_PROMPT,
)

# Load environment variables from .env
load_dotenv()


class InterviewExtractor:
    """
    Uses an LLM to convert one interview experience into
    structured interview knowledge.
    """

    def __init__(self):
        """
        Initialize the Interview Extractor.
        """

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY not found. Please add it to your .env file.")

        self.client = Groq(api_key=api_key)

        self.model = os.getenv(
            "GROQ_MODEL",
            "llama-3.3-70b-versatile",
        )

        self.prompt = INTERVIEW_EXTRACTION_PROMPT

    def extract(self, interview: dict) -> dict:
        """
        Extract structured information from one interview.

        Args:
            interview:
                One normalized interview dictionary.

        Returns:
            A structured interview dictionary following the
            PlacementIQ extraction schema.
        """

        try:
            interview_json = json.dumps(
                interview,
                indent=2,
                ensure_ascii=False,
            )

            response = self.client.chat.completions.create(
                model=self.model,
                temperature=0,
                response_format={"type": "json_object"},
                messages=[
                    {
                        "role": "system",
                        "content": self.prompt,
                    },
                    {
                        "role": "user",
                        "content": interview_json,
                    },
                ],
            )

            response_text = response.choices[0].message.content

            if not response_text:
                raise ValueError("Groq returned an empty response.")

            structured_interview = json.loads(response_text)

            return structured_interview

        except json.JSONDecodeError as e:
            raise ValueError("Failed to parse JSON returned by Groq.") from e

        except ValueError:
            raise

        except Exception as e:
            raise RuntimeError(f"Interview extraction failed: {e}") from e
