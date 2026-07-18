from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from app.routes import router as api_router

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

# Jinja2 environment (no caching)
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

# API routes
app.include_router(api_router)
