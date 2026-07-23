import os
from google.genai import Client

# Initialize Gemini client once
client = Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_answer(question: str, context: str) -> str:
    """
    Generate a final RAG answer using Gemini 1.5 Pro.
    """

    if not context or context.strip() == "":
        context = "No relevant policy information was found in the knowledge base."

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
