from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from app.rag import rag_answer  # enhanced RAG pipeline

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

# Jinja2 environment
env = Environment(
    loader=FileSystemLoader(str(BASE_DIR / "templates")),
    auto_reload=True,
    cache_size=0
)

# Static files
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Homepage route
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    template = env.get_template("chat.html")
    return HTMLResponse(template.render(request=request))

# Enhanced RAG endpoint
@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question", "")

    answer = rag_answer(question)
    return JSONResponse({"answer": answer})
