"""Response schemas for the PlacementIQ API."""
from pydantic import BaseModel


class AskResponse(BaseModel):
    """Payload returned by the question-answering endpoint."""
    answer: str
    intent: str
