from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load FAISS index from the correct folder and correct filename
db = FAISS.load_local(
    "app/rag/embeddings",
    embeddings,
    index_name="vectorstore",
    allow_dangerous_deserialization=True
)

# Retrieval function
def retrieve_docs(query: str, k: int = 3):
    return db.similarity_search(query, k=k)

def rerank_docs(query: str, docs, top_k: int = 3):
    query_vec = embeddings.embed_query(query)
    scored = []

    for doc in docs:
        doc_vec = embeddings.embed_query(doc.page_content)
        score = sum(q * d for q, d in zip(query_vec, doc_vec))
        scored.append((score, doc))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [doc for _, doc in scored[:top_k]]
