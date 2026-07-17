import os
import faiss
import pickle
from pathlib import Path
from sentence_transformers import SentenceTransformer

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / "data"
DOCS_PATH = DATA_DIR / "documents.pkl"
EMB_PATH = DATA_DIR / "embeddings.pkl"
INDEX_PATH = DATA_DIR / "faiss.index"

model = None
documents = None
embeddings = None
faiss_index = None


def load_model():
    global model
    if model is None:
        print("🔵 Loading embedding model...")
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model


def load_documents():
    global documents
    if documents is None:
        print("🔵 Loading documents...")
        with open(DOCS_PATH, "rb") as f:
            documents = pickle.load(f)
    return documents


def load_embeddings():
    global embeddings
    if embeddings is None:
        print("🔵 Loading embeddings...")
        with open(EMB_PATH, "rb") as f:
            embeddings = pickle.load(f)
    return embeddings


def load_index():
    global faiss_index
    if faiss_index is None:
        print("🔵 Loading FAISS index...")
        faiss_index = faiss.read_index(str(INDEX_PATH))
    return faiss_index


def initialize_rag():
    load_model()
    load_documents()
    load_embeddings()
    load_index()
    print("✅ RAG initialized")
