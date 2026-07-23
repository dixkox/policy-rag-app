import os
from google.genai import Client

client = Client(api_key=os.getenv("GOOGLE_API_KEY"))

def rag_answer(query):
    from app.rag.retrieval import retrieve_docs
    docs = retrieve_docs(query)

    from app.rag.rerank import rerank_docs
    ranked = rerank_docs(query, docs)

    context = "\n\n".join([doc.page_content for doc in ranked])

    prompt = f"""
You are a policy assistant. Use ONLY the context below to answer.

Context:
{context}

User question:
{query}

Answer clearly and concisely.
"""

    response = client.models.generate_content(
        model="models/gemini-1.5-pro",
        contents=prompt
    )

    return response.text
