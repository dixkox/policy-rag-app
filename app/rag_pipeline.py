import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# -----------------------------
# Load and chunk policy documents
# -----------------------------
def load_policy_docs(folder: str = "data/policies") -> list[str]:

    docs = []
    if not os.path.isdir(folder):
        print(f"[RAG] Policy folder not found: {folder}")
        return docs

    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            path = os.path.join(folder, filename)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            # Split by headings (# Policy Title)
            chunks = re.split(r"\n# ", text)
            chunks = ["# " + c.strip() for c in chunks if c.strip()]

            docs.extend(chunks)

    print(f"[RAG] Loaded {len(docs)} policy chunks.")
    return docs


policy_docs = load_policy_docs()

# -----------------------------
# Build TF-IDF index
# -----------------------------
def build_tfidf_index(docs: list[str]):
    if not docs:
        print("[RAG] No documents found. Empty TF-IDF index created.")
        return None, None

    vectorizer = TfidfVectorizer()
    doc_vectors = vectorizer.fit_transform(docs)

    print(f"[RAG] TF-IDF index built with {len(docs)} vectors.")
    return vectorizer, doc_vectors


vectorizer, doc_vectors = build_tfidf_index(policy_docs)

# -----------------------------
# NEW: Safe Retrieval Function
# -----------------------------
def retrieve_policy(query, vectorizer, docs, doc_vectors):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, doc_vectors).flatten()

    best_score = scores.max()
    best_index = scores.argmax()

    # Reject irrelevant matches
    if best_score < 0.15:
        return None  # <-- important: return None so answer_question can handle it

    return docs[best_index]

# -----------------------------
# Core RAG answer function (UPDATED)
# -----------------------------
def answer_question(query: str):
    if vectorizer is None or doc_vectors is None:
        return {
            "available": False,
            "context": "",
            "reason": "No policy documents are loaded."
        }

    result = retrieve_policy(query, vectorizer, policy_docs, doc_vectors)

    if result is None:
        return {
            "available": False,
            "context": "",
            "reason": "No relevant policy found."
        }

    return {
        "available": True,
        "context": result,
        "reason": "Best match found."
    }
