from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
POLICY_DIR = BASE_DIR / "rag" / "policies"
VECTOR_DIR = BASE_DIR / "rag" / "embeddings"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = []

for file in POLICY_DIR.glob("*.*"):
    text = file.read_text(encoding="utf-8")
    chunks = splitter.split_text(text)
    for chunk in chunks:
        docs.append(Document(page_content=chunk))

vectorstore = FAISS.from_documents(docs, embeddings)

VECTOR_DIR.mkdir(parents=True, exist_ok=True)

vectorstore.save_local(
    folder_path=str(VECTOR_DIR),
    index_name="vectorstore"
)

print("Vectorstore built successfully.")
