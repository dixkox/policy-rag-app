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
    if not context.strip():
        return "No relevant policy information was found."

    answer = (
        f"Here is the relevant policy information related to your question:\n\n"
        f"{context}\n\n"
        f"This information was retrieved based on similarity to your query: '{question}'."
    )
    return answer

# -----------------------------
# /ask endpoint (UPDATED WITH CITATIONS)
# -----------------------------
@app.post("/ask")
def ask_question(payload: AskRequest):
    question = payload.question.strip()

    if not question:
        return {"answer": "Please enter a valid question."}

    rag_result = retrieve_context(question)

    if not rag_result["available"]:
        return {
            "answer": "Invalid question. No relevant policy found.",
            "context": "",
            "reason": rag_result["reason"],
            "citation": None
        }

    context = rag_result["context"]
    reason = rag_result["reason"]
    citation = rag_result["citation"]

    if len(context.strip()) < 20:
        return {
            "answer": "Invalid question. No relevant policy found.",
            "context": "",
            "reason": "Low similarity score",
            "citation": None
        }

    answer = generate_answer(context, question)

    return {
        "answer": answer,
        "context": context,
        "reason": reason,
        "citation": citation
    }

# -----------------------------
# Root endpoint
# -----------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def home():
    return {"message": "Policy RAG API is running (TF-IDF version)."}
