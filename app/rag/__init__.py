import os
import google.genai as genai

# Configure Gemini with your environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use the correct model name for the new SDK
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def rag_answer(query):
    # 1. Retrieve documents (your existing retrieval code)
    from app.rag.retrieval import retrieve_docs
    docs = retrieve_docs(query)

    # 2. Rerank documents (your existing reranker)
    from app.rag.rerank import rerank_docs
    ranked = rerank_docs(query, docs)

    # 3. Build context
    context = "\n\n".join([doc.page_content for doc in ranked])

    # 4. Build final prompt
    prompt = f"""
You are a policy assistant. Use ONLY the context below to answer.

Context:
{context}

User question:
{query}

Answer clearly and concisely.
"""

    # 5. Generate answer using Gemini 1.5 Pro (new SDK)
    response = model.generate_content(prompt)

    return response.text
