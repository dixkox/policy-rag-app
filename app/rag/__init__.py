import os
from google.genai import Client
from sentence_transformers import SentenceTransformer, util
import faiss
import json

# -----------------------------
# Load Gemini client
# -----------------------------
client = Client(api_key=os.getenv("GOOGLE_API_KEY"))

# -----------------------------
# Load embedding model
# -----------------------------
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# -----------------------------
# Load FAISS index + documents
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "faiss.index")
DOCS_PATH = os.path.join(BASE_DIR, "docs.json")

faiss_index = faiss.read_index(INDEX_PATH)

with open(DOCS_PATH, "r", encoding="utf-8") as f:
    documents = json.load(f)


# -----------------------------
# Retrieve top documents
# -----------------------------
def retrieve_context(query: str, top_k: int = 5):
    query_embedding = embedder.encode(query)
    query_embedding = query_embedding.reshape(1, -1)

    distances, indices = faiss_index.search(query_embedding, top_k)

    retrieved_docs = []
    for idx in indices[0]:
        if idx < len(documents):
            retrieved_docs.append(documents[idx]["text"])

    return "\n\n".join(retrieved_docs)


# -----------------------------
# RAG Answer using Gemini
# -----------------------------
def rag_answer(question: str):
    context = retrieve_context(question)

    if not context.strip():
        context = "No relevant policy information was found."

    prompt = f"""
You are a policy assistant. Use ONLY the context below to answer.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""

    response = client.models.generate_content(
        model="gemini-1.5-pro-001",
        contents=prompt
    )

    return response.text
