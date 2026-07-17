AI Tooling
This document explains the AI tools, models, and frameworks used in the Policy‑RAG‑App, including the rationale behind each choice, alternatives considered, and tradeoffs.

🧠 Overview of AI Tools Used
The Policy‑RAG‑App uses a combination of:

FastAPI for backend orchestration

SentenceTransformer (MiniLM‑L6‑v2) for embeddings

FAISS for vector search

FLAN‑T5 for answer generation

Cursor + Copilot for assisted development

Manual engineering for RAG pipeline, evaluation, and documentation

These tools were selected for speed, simplicity, and suitability for local inference.

⚙️ FastAPI (Backend Framework)
Why FastAPI?
Extremely fast and lightweight

Async support for ML inference

Easy routing and dependency injection

Perfect for serving RAG pipelines

Alternatives Considered
Flask (too slow, no async)

Django (too heavy for ML inference)

Tradeoff
FastAPI requires manual scaling setup for production.

🧩 SentenceTransformer Embeddings (MiniLM‑L6‑v2)
Why MiniLM?
Small and fast

High semantic accuracy

Works well for policy documents

Runs locally without GPU

Alternatives Considered
BERT‑base (too slow)

Instructor‑XL (too heavy)

OpenAI embeddings (requires API cost + internet)

Tradeoff
MiniLM is less accurate than larger transformer models.

🔍 FAISS Vector Store
Why FAISS?
Industry‑standard similarity search

Extremely fast retrieval

Supports large embedding sets

Works offline

Alternatives Considered
ChromaDB (good but slower for large indexes)

Pinecone (requires cloud + cost)

Tradeoff
FAISS requires manual index rebuild when documents change.

✨ FLAN‑T5 (Answer Generation)
Why FLAN‑T5?
Strong instruction‑following

Lightweight enough for local inference

Good for grounded answers

Works well with retrieved context

Alternatives Considered
GPT‑4 / Llama‑3 (too heavy or requires API)

BART‑large (weaker instruction following)

Tradeoff
FLAN‑T5 struggles with ambiguous or multi‑step reasoning questions.

🛠️ AI Code Assistants (Cursor + Copilot)
How They Were Used
Scaffolding project structure

Generating boilerplate FastAPI routes

Creating initial RAG pipeline skeleton

Helping debug template rendering issues

Assisting with documentation formatting

What Was Done Manually
RAG retrieval logic

Prompt engineering

Evaluation methodology

Architecture design

All final documentation

Latency testing

Chunking strategy

Why Use AI Assistants?
Faster prototyping

Reduced boilerplate coding

Improved consistency

Better debugging support

Tradeoff
AI assistants generate scaffolding, but manual refinement is required for correctness and quality.

🧪 Evaluation Tools
Custom script: scripts/evaluate_rag.py

Measures latency, groundedness, relevance, correctness

Used for 20‑query benchmark

✅ Conclusion
The AI tooling choices balance performance, simplicity, and local inference capability. FastAPI, MiniLM, FAISS, and FLAN‑T5 form a lightweight but effective RAG stack, while AI assistants (Cursor + Copilot) accelerated development without replacing manual engineering.

This tooling strategy supports a clean, modular, and efficient RAG application suitable for policy analysis and AI engineering presentations.