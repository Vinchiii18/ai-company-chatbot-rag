from fastapi import APIRouter
from pydantic import BaseModel

from app.services.azure_openai_service import azure_openai_service

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    answer = azure_openai_service.chat(request.message)

    return {
        "answer": answer
    }