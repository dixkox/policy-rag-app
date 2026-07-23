from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path

# Base directory: POLICY_RAG_APP/app
BASE_DIR = Path(__file__).resolve().parents[1]

# Path to the FAISS metadata file
VECTORSTORE_PATH = BASE_DIR / "rag" / "embeddings" / "vectorstore.pkl"

# Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def load_vectorstore():
    """
    Load the FAISS vectorstore from disk.
    Requires BOTH:
        - vectorstore.faiss
        - vectorstore.pkl
    """
    return FAISS.load_local(
        folder_path=str(VECTORSTORE_PATH.parent),
        embeddings=embeddings,
        index_name="vectorstore",
        allow_dangerous_deserialization=True
    )

def retrieve_docs(query: str):
    """
    Retrieve the most relevant policy chunks for the given query.
    Returns a list of LangChain Document objects.
    """
    vs = load_vectorstore()
    docs = vs.similarity_search(query, k=4)

    return docs
