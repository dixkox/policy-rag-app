SYSTEM_PROMPT = """You are an assistant that answers questions strictly about company policies.
If a question is outside the policies, say: "I can only answer questions about our policies."
Always ground your answers in the provided context and cite document IDs/titles.
Keep answers concise.
"""


def build_rag_prompt(question: str, context: str) -> str:
    return f"""{SYSTEM_PROMPT}

Context:
{context}

Question: {question}

Answer:"""
