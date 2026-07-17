import time
from typing import List

from app.rag.retrieval import retrieve_relevant_chunks
from app.rag.llm import generate_answer


def evaluate(questions: List[str]):
    latencies = []
    for q in questions:
        start = time.time()
        chunks = retrieve_relevant_chunks(q, k=5)
        answer, citations = generate_answer(q, chunks)
        latencies.append((time.time() - start) * 1000)
        print(f"Q: {q}\nA: {answer[:300]}...\nCitations: {len(citations)}\n")

    print("Latency ms:", latencies)


if __name__ == "__main__":
    sample_questions = [
        "What is the PTO policy?",
        "How are expenses reimbursed?",
        "What is the remote work policy?",
    ]
    evaluate(sample_questions)
