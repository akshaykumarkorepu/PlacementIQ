from fastapi import FastAPI

from placementiq.schemas.request import AskRequest
from placementiq.schemas.response import AskResponse
from placementiq.web.ai_service import AIService

app = FastAPI()

ai_service = AIService()


@app.get("/")
def root():
    return {"message": "Welcome to PlacementIQ API"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest) -> AskResponse:
    """Accept a user question, delegate to the AI service, and return its answer."""
    result = ai_service.ask(req.question)
    return AskResponse(answer=result["answer"], intent=result["intent"])
