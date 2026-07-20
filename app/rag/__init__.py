from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load FAISS index from the correct folder
db = FAISS.load_local(
    "app/rag/embeddings",
    embeddings,
    allow_dangerous_deserialization=True
)

# Retrieval function
def retrieve_docs(query: str, k: int = 3):
    return db.similarity_search(query, k=k)

