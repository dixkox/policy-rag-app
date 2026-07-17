from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path
import time

router = APIRouter()

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = PROJECT_ROOT / "templates"
templates = Jinja2Templates(directory=str(TEMPLATE_DIR))

@router.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@router.post("/ask")
async def ask_question(request: Request):
    from app.rag.retrieval import get_context
    from app.rag.answer import generate_answer

    data = await request.json()
    question = data.get("question")

    start = time.time()

    # Retrieve context chunks
    context_chunks = get_context(question)

    # Generate answer using retrieved context
    answer = generate_answer(question, context_chunks)

    latency_ms = (time.time() - start) * 1000

    # Return EVERYTHING needed for evaluation
    return {
        "question": question,
        "context": context_chunks,
        "answer": answer,
        "latency_ms": latency_ms
    }
