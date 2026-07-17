from typing import List, Optional
from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


class Citation(BaseModel):
    doc_id: str
    title: str
    snippet: str


class ChatResponse(BaseModel):
    answer: str
    citations: List[Citation]
    latency_ms: Optional[float] = None
