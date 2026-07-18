from typing import List, Tuple
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.schema import Document

# 1. Query Rewriter (simple enhancement)
def rewrite_query(question: str) -> str:
    # You can make this smarter later (expand acronyms, add synonyms, etc.)
    return question.strip()

# 2. Embeddings model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 3. Vector store (FAISS)
db = FAISS.load_local("vectorstore", embeddings)

# 4. Retriever (basic top-k)
def retrieve_docs(query: str, k: int = 8) -> List[Document]:
    return db.similarity_search(query, k=k)

# 5. Reranker (simple scoring by embedding similarity)
def rerank_docs(query: str, docs: List[Document], top_k: int = 3) -> List[Document]:
    query_vec = embeddings.embed_query(query)
    scored: List[Tuple[float, Document]] = []

    for doc in docs:
        doc_vec = embeddings.embed_query(doc.page_content)
        # cosine similarity approximation via dot product
        score = sum(q * d for q, d in zip(query_vec, doc_vec))
        scored.append((score, doc))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [doc for _, doc in scored[:top_k]]

# 6. LLM
llm = OpenAI(temperature=0)

# 7. Final RAG answer
def rag_answer(question: str) -> str:
    # Step 1: rewrite query
    rewritten = rewrite_query(question)

    # Step 2: retrieve docs
    retrieved = retrieve_docs(rewritten, k=8)

    # Step 3: rerank docs
    top_docs = rerank_docs(rewritten, retrieved, top_k=3)

    # Step 4: build context
    context = "\n\n".join(doc.page_content for doc in top_docs)

    # Step 5: ask LLM with context
    prompt = (
        "You are a policy assistant. Use ONLY the context below to answer.\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}\n\n"
        "Answer:"
    )

    return llm(prompt)
