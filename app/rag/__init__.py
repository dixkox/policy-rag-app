import os
from google.genai import Client

# Create Gemini client using your API key
client = Client(api_key=os.getenv("GOOGLE_API_KEY"))

def rag_answer(query):
    # 1. Retrieve documents
    from app.rag.retrieval import retrieve_docs
    docs = retrieve_docs(query)

    # 2. Rerank documents
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

    # 5. Generate answer using Gemini 1.5 Pro
    response = client.models.generate_content(
        model="gemini-1.5-pro-latest",
        contents=prompt
    )

    return response.text
