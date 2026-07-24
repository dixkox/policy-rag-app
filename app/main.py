from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from app.rag import rag_answer

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent

app = FastAPI()

env = Environment(
    loader=FileSystemLoader(str(ROOT_DIR / "templates")),
    auto_reload=True,
    cache_size=0
)

app.mount(
    "/static",
    StaticFiles(directory=str(ROOT_DIR / "static")),
    name="static"
)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    template = env.get_template("chat.html")
    return HTMLResponse(template.render(request=request))

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question", "")

    answer = rag_answer(question)
    return JSONResponse({"answer": answer})
