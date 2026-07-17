System Architecture
This document explains how the Policy‑RAG‑App processes user questions using Retrieval‑Augmented Generation (RAG). It includes the system diagram, component breakdown, data flow, and tooling justification.

🧠 High‑Level Overview
Policy‑RAG‑App is a Retrieval‑Augmented Generation system that combines:

A FastAPI backend

A vector store for document embeddings

A retrieval module for similarity search

A generation module for answer synthesis

A simple web UI for user interaction

The system retrieves relevant policy text and uses an LLM to generate grounded answers.

🔧 Component Breakdown
1. Web UI (Frontend)
HTML templates rendered via FastAPI

Sends user questions to /ask

Displays final answers

2. FastAPI Backend
Hosts REST endpoints

Orchestrates retrieval + generation

Handles document ingestion and embedding

3. Retrieval Module
Loads FAISS vector store

Uses MiniLM embeddings

Performs similarity search

Returns top‑k relevant chunks

4. Generation Module
Builds prompts

Tokenizes input

Calls FLAN‑T5 model

Produces final answer

5. Vector Store
FAISS index stored in vectorstore.faiss

Metadata stored in vectorstore.pkl

Enables fast similarity search

6. Embedding Model
all-MiniLM-L6-v2

Converts text chunks into dense vectors

🔄 Data Flow
Step‑by‑step pipeline
User submits a question

Frontend sends POST request to /ask

FastAPI calls retrieval module

Retrieval module loads FAISS index

Embeddings model computes similarity

Top‑k chunks returned to backend

Backend builds prompt

Generation module calls FLAN‑T5

Model generates answer tokens

Tokens decoded into final answer

JSON response returned to frontend

Frontend displays answer to user

📚 RAG Pipeline Architecture
1. Document Ingestion
PDF/text files uploaded

Cleaned and chunked

2. Embedding Generation
Each chunk embedded using MiniLM

3. Vector Storage
Stored in FAISS index

4. Retrieval
Similarity search returns relevant chunks

5. Answer Generation
Prompt = user question + retrieved context

FLAN‑T5 generates grounded answer

🧩 System Diagram
mermaid
flowchart TD
    U[User / Web UI] -->|Question| FE[Frontend / templates/chat.html]
    FE -->|POST /ask| API[FastAPI Backend / app.routes]
    API -->|calls| RET[Retrieval module / app.rag.retrieval.get_context]
    RET -->|loads| VS[FAISS vectorstore / vectorstore.faiss + vectorstore.pkl]
    RET -->|uses| EMB[Embeddings model / all-MiniLM-L6-v2]
    RET -->|returns context| API
    API -->|calls| GEN[Generation module / app.rag.answer.generate_answer]
    GEN --> TOK[Tokenizer and prompt builder]
    TOK --> MODEL[FLAN-T5-base model]
    MODEL -->|generated tokens| TOK
    TOK -->|decoded answer| API
    API -->|JSON answer| FE
    FE -->|Final answer| U
⚙️ Tooling Justification
FastAPI
Lightweight

Async support

Easy routing

Perfect for ML inference APIs

FAISS
Industry‑standard vector search

Extremely fast similarity search

Supports large embedding sets

MiniLM Embeddings
Small

Fast

High accuracy for semantic search

FLAN‑T5
Strong instruction‑following

Good for grounded answers

Lightweight enough for local inference

⚖️ Tradeoffs
Component	Strength	Tradeoff
FAISS	Fast retrieval	Requires manual index management
MiniLM	Lightweight embeddings	Less accurate than larger models
FLAN‑T5	Fast inference	Not as strong as GPT‑4 or Llama‑3
FastAPI	Simple and fast	Requires manual scaling setup


✅ Conclusion
This architecture provides a clean, efficient, and modular RAG system suitable for policy analysis and AI engineering presentations. It balances performance, simplicity, and clarity while demonstrating real‑world retrieval‑augmented generation.