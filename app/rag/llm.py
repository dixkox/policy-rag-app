import os
import requests

HF_API_KEY = os.getenv("HF_API_KEY")  # optional, free tier works without key

def call_llama(prompt: str) -> str:
    url = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3.1-8B-Instruct"

    headers = {
        "Content-Type": "application/json"
    }

    if HF_API_KEY:
        headers["Authorization"] = f"Bearer {HF_API_KEY}"

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.2
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    data = response.json()

    # HF returns a list with generated_text
    return data[0]["generated_text"]
