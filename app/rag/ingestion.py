from pathlib import Path
from typing import List, Tuple

from sentence_transformers import SentenceTransformer

from ..config import settings
from .vectorstore import VectorStore


def load_documents() -> List[Tuple[str, str]]:
    docs = []
    raw_dir: Path = settings.RAW_DIR
    for path in raw_dir.glob("**/*"):
        if path.suffix.lower() in {".txt", ".md"}:
            docs.append((path.name, path.read_text(encoding="utf-8", errors="ignore")))
    return docs


def build_vectorstore():
    vs = VectorStore(settings.VECTORSTORE_DIR)
    model = SentenceTransformer(settings.EMBEDDING_MODEL)

    docs = load_documents()
    ids = []
    texts = []
    metas = []

    for idx, (name, content) in enumerate(docs):
        ids.append(f"doc-{idx}")
        texts.append(content)
        metas.append({"doc_id": f"doc-{idx}", "title": name})

    # Chroma will embed internally; we just store texts + metadata
    vs.add(ids=ids, texts=texts, metadatas=metas)
