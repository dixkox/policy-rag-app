import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from pathlib import Path
from app.rag.vectorstore import add_documents

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = BASE_DIR / "data" / "docs"

def load_docs():
    texts = []
    ids = []
    metadatas = []

    for i, path in enumerate(DOCS_DIR.glob("*.txt")):
        content = path.read_text(encoding="utf-8")
        texts.append(content)
        ids.append(f"doc_{i}")
        metadatas.append({"filename": path.name})

    return texts, ids, metadatas

if __name__ == "__main__":
    texts, ids, metadatas = load_docs()
    print(f"Loading {len(texts)} documents...")
    add_documents(texts, ids, metadatas)
    print("Done.")
