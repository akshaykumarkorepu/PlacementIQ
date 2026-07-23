"""Request schemas for the PlacementIQ API."""
from pydantic import BaseModel


class AskRequest(BaseModel):
    """Payload accepted by the question-answering endpoint."""
    question: str
