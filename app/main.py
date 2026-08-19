from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.rag_pipeline import answer_question as retrieve_context

app = FastAPI()

# -----------------------------
# CORS (allow frontend)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Request model
# -----------------------------
class AskRequest(BaseModel):
    question: str

# -----------------------------
# Simple rule-based answer generator
# -----------------------------
def generate_answer(context: str, question: str) -> str:
    """
    Since we cannot load transformer models on this machine,
    we generate a simple answer using rule-based logic.
    """

    if not context.strip():
        return "No relevant policy information was found."

    # Basic answer style
    answer = (
        f"Here is the relevant policy information related to your question:\n\n"
        f"{context}\n\n"
        f"This information was retrieved based on similarity to your query: '{question}'."
    )

    return answer

# -----------------------------
# /ask endpoint
# -----------------------------
@app.post("/ask")
def ask_question(payload: AskRequest):
    question = payload.question.strip()

    if not question:
        return {"answer": "Please enter a valid question."}

    rag_result = retrieve_context(question)

    if not rag_result["available"]:
        return {
            "answer": "No relevant policy found.",
            "context": "",
            "reason": rag_result["reason"]
        }

    context = rag_result["context"]
    answer = generate_answer(context, question)

    return {
        "answer": answer,
        "context": context,
        "reason": rag_result["reason"]
    }

# -----------------------------
# Root endpoint
# -----------------------------
@app.get("/")
def home():
    return {"message": "Policy RAG API is running (TF-IDF version)."}
