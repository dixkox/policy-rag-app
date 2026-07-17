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

def get_context(question: str) -> str:
    """
    Retrieve the most relevant policy chunks for the given question.
    """
    vs = load_vectorstore()
    docs = vs.similarity_search(question, k=4)

    if not docs:
        return "No relevant policy documents found."

    return "\n\n".join([d.page_content for d in docs])
