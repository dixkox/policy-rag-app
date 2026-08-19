import os
import json
import faiss
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_PATH = os.path.join(BASE_DIR, "faiss.index")
DOCS_PATH = os.path.join(BASE_DIR, "docs.json")
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "phi3")  # app/models/phi3

# -----------------------------
# Load FAISS index
# -----------------------------
faiss_index = faiss.read_index(INDEX_PATH)

# -----------------------------
# Load documents
# -----------------------------
with open(DOCS_PATH, "r", encoding="utf-8") as f:
    documents = json.load(f)

# -----------------------------
# Embedding model
# -----------------------------
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# -----------------------------
# Local Phi-3 Mini LLM (offline)
# -----------------------------
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.float32,
    device_map="cpu"
)

def call_local_llm(prompt: str) -> str:
    """
    Offline Phi-3 Mini inference.
    No internet, no external APIs.
    """
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=300,
        temperature=0.2,
        do_sample=False
    )
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text

# -----------------------------
# Retrieve context from FAISS
# -----------------------------
def retrieve_context(query: str, k: int = 3) -> str:
    query_embedding = embedder.encode([query]).astype("float32")
    distances, indices = faiss_index.search(query_embedding, k)

    retrieved_docs = []
    for idx in indices[0]:
        if idx < len(documents):
            retrieved_docs.append(documents[idx]["text"])

    return "\n\n".join(retrieved_docs)

# -----------------------------
# RAG answer
# -----------------------------
def rag_answer(question: str) -> str:
    context = retrieve_context(question)

    prompt = f"""
You are an AI assistant answering questions using company policies.

Context:
{context}

Question:
{question}

Answer clearly, concisely, and only based on the context. If the answer is not in the context, say you don't know.
"""

    return call_local_llm(prompt)
