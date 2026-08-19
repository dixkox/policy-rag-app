# Evaluation Summary – Policy‑RAG‑App

## Overview
The Policy‑RAG‑App uses TF‑IDF vectorization and cosine similarity to retrieve grounded policy answers. The system is deterministic, fast, and fully offline.

## Correctness
The system performs strongly on direct, well‑structured questions. Out of 20 questions, 16 were fully correct and grounded. Four questions showed typical TF‑IDF failure modes such as header dominance or ambiguity.

## Groundedness
All correct answers were directly supported by retrieved policy text. Incorrect answers occurred only when the question was ambiguous or not explicitly answered in the policy.

## Latency
- Average latency: ~860 ms  
- p50 latency: ~720 ms  
- p95 latency: ~1380 ms  
- Worst-case latency: ~21 seconds (cold start)

## Failure Modes
- Header dominance (TF‑IDF matches section titles)
- Ambiguous questions return nearest lexical match
- Multi-policy context drift
- No semantic understanding or synonym handling

## Recommendations
- Add semantic embeddings (MiniLM)
- Add FAISS for scalable vector search
- Add reranking (BM25 or cross‑encoder)
- Improve chunking granularity
