# Design and Evaluation

## Design & Architecture

- FastAPI backend
- Chroma vectorstore
- SentenceTransformer embeddings
- RAG pipeline with top-k retrieval and citations

## Evaluation

- Groundedness: manual inspection of answers vs. source snippets
- Citation accuracy: check doc_id/title vs. supporting passages
- Latency: p50/p95 over 10–20 queries using `scripts/evaluate_rag.py`.
