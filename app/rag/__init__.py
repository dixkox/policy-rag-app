from typing import List, Tuple
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from langchain_core.documents import Document

# 1. Query Rewriter
def rewrite_query(question: str) -> str:
    return question.strip()

# 2. Embeddings model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 3. Vector store (FAISS)
db = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

# 4. Retriever
def retrieve_docs(query: str, k: int = 8) -> List[Document]:
    return db.similarity_search(query, k=k)

# 5. Reranker
def rerank_docs(query: str, docs: List[Document], top_k: int = 3) -> List[Document]:
    query_vec = embeddings.embed_query(query)
    scored: List[Tuple[float, Document]] = []

    for doc in docs:
        doc_vec = embeddings.embed_query(doc.page_content)
        score = sum(q * d for q, d in zip(query_vec, doc_vec))
        scored.append((score, doc))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [doc for _, doc in scored[:top_k]]

# 6. LLM
llm = OpenAI(temperature=0)

# 7. Final RAG answer
def rag_answer(question: str) -> str:
    rewritten = rewrite_query(question)
    retrieved = retrieve_docs(rewritten, k=8)
    top_docs = rerank_docs(rewritten, retrieved, top_k=3)

    context = "\n\n".join(doc.page_content for doc in top_docs)

    prompt = (
        "You are a policy assistant. Use ONLY the context below to answer.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}\n\n"
        "Answer:"
    )

    return llm(prompt)
