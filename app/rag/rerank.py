import numpy as np
from langchain_huggingface import HuggingFaceEmbeddings

# Use the same embedding model as retrieval
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two vectors.
    """
    a = np.array(a)
    b = np.array(b)
    return float(a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def rerank_docs(query: str, docs: list):
    """
    Rerank retrieved documents using cosine similarity.
    Returns documents sorted by relevance.
    """
    if not docs:
        return []

    # Embed the query
    query_embedding = embeddings.embed_query(query)

    scored_docs = []
    for doc in docs:
        doc_embedding = embeddings.embed_query(doc.page_content)
        score = cosine_similarity(query_embedding, doc_embedding)
        scored_docs.append((score, doc))

    # Sort by score (highest first)
    scored_docs.sort(key=lambda x: x[0], reverse=True)

    # Return only the documents
    return [doc for score, doc in scored_docs]
