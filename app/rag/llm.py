import os
import json
import requests

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def answer_question(question: str, contexts):
    print("ANSWER_QUESTION FUNCTION WAS CALLED")

    # If retrieval is broken, fallback to empty context
    if not contexts:
        context_text = "No context was retrieved."
    else:
        context_text = "\n\n".join([doc for doc, _ in contexts])

    prompt = f"""
You are a policy assistant. Use ONLY the context below to answer the question.

Context:
{context_text}

Question:
{question}

Answer:
"""

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You answer questions using provided policy context only."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()

    os.makedirs("logs", exist_ok=True)
    with open("logs/llm_response.json", "w", encoding="utf-8") as f:
        json.dump(response_json, f, indent=4)

    if "error" in response_json:
        return f"LLM Error: {response_json['error']['message']}"

    return response_json["choices"][0]["message"]["content"]
