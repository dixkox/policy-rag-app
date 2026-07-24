import os
from google.genai import Client

client = Client(api_key=os.getenv("GOOGLE_API_KEY"))

def rag_answer(question: str):
    context = retrieve_context(question)  # your FAISS + rerank pipeline

    prompt = f"""
You are a policy assistant. Use ONLY the context below to answer.

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""

    response = client.models.generate_content(
        model="gemini-1.5-pro-001",
        contents=prompt
    )

    return response.text
