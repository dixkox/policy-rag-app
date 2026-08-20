import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# -----------------------------
# Load and chunk policy documents WITH FILENAMES
# -----------------------------
def load_policy_docs(folder: str = "data/policies"):
    docs = []
    filenames = []

    if not os.path.isdir(folder):
        print(f"[RAG] Policy folder not found: {folder}")
        return docs, filenames

    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            path = os.path.join(folder, filename)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()

            # Split by headings (# Policy Title)
            chunks = re.split(r"\n# ", text)
            chunks = ["# " + c.strip() for c in chunks if c.strip()]

            docs.extend(chunks)
            filenames.extend([filename] * len(chunks))

    print(f"[RAG] Loaded {len(docs)} policy chunks.")
    return docs, filenames


policy_docs, policy_filenames = load_policy_docs()

# -----------------------------
# Build TF-IDF index
# -----------------------------
def build_tfidf_index(docs):
    if not docs:
        print("[RAG] No documents found. Empty TF-IDF index created.")
        return None, None

    vectorizer = TfidfVectorizer(stop_words="english")
    doc_vectors = vectorizer.fit_transform(docs)

    print(f"[RAG] TF-IDF index built with {len(docs)} vectors.")
    return vectorizer, doc_vectors


vectorizer, doc_vectors = build_tfidf_index(policy_docs)

# -----------------------------
# Safe Retrieval Function WITH CITATIONS
# -----------------------------
def retrieve_policy(query, vectorizer, docs, doc_vectors, filenames):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, doc_vectors).flatten()

    best_score = scores.max()
    best_index = scores.argmax()

    threshold = 0.25

    if best_score < threshold:
        return None, best_score, None, None

    citation_file = filenames[best_index]
    citation_heading = docs[best_index].split("\n")[0].replace("# ", "").strip()

    return docs[best_index], best_score, citation_file, citation_heading

# -----------------------------
# Core RAG answer function WITH CITATIONS
# -----------------------------
def answer_question(query: str):
    if vectorizer is None or doc_vectors is None:
        return {
            "available": False,
            "context": "",
            "reason": "No policy documents are loaded.",
            "citation": None
        }

    result, score, citation_file, citation_heading = retrieve_policy(
        query, vectorizer, policy_docs, doc_vectors, policy_filenames
    )

    if result is None:
        return {
            "available": False,
            "context": "",
            "reason": f"Low similarity score ({score:.3f})",
            "citation": None
        }

    return {
        "available": True,
        "context": result,
        "reason": f"Similarity score = {score:.3f}",
        "citation": {
            "file": citation_file,
            "section": citation_heading
        }
    }
