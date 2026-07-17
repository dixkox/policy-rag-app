Policy‑RAG‑App
A Retrieval‑Augmented Generation (RAG) application designed to answer policy‑related questions using vector search, document embeddings, and a FastAPI backend. Built as part of the MSSE Artificial Intellingence Engineering Presentation.

🚀 Overview
Policy‑RAG‑App enables users to upload policy documents, convert them into vector embeddings, store them in a vector database, and retrieve relevant chunks when answering questions. The system combines:

Document ingestion

Text chunking

Embedding generation

Vector search

RAG answer synthesis

FastAPI backend

Simple web UI

This project demonstrates how modern AI systems can support policy analysis, compliance, and decision‑making.

🧠 Architecture
System Diagram
Code
User → Web UI → FastAPI → RAG Pipeline → Vector Store → LLM → Final Answer
Components
FastAPI Backend — Hosts API endpoints for ingestion, retrieval, and RAG queries.

Vector Store (ChromaDB / FAISS) — Stores embeddings for fast similarity search.

Embedding Model — Converts text into numerical vectors.

LLM — Synthesizes final answers using retrieved context.

Frontend UI — Simple interface for uploading documents and asking questions.

📁 Project Structure
Code
policy-rag-app/
│
├── app/
│   ├── main.py                 # FastAPI entry point
│   ├── rag_pipeline.py         # RAG orchestration logic
│   ├── embeddings.py           # Embedding model wrapper
│   ├── vectorstore.py          # Vector DB operations
│   ├── models/                 # Pydantic models
│   └── utils/                  # Helper utilities
│
├── data/
│   └── documents/              # Uploaded policy documents
│
├── static/                     # CSS, JS
├── templates/                  # HTML templates
│
├── requirements.txt
├── README.md
└── .gitignore
⚙️ Installation
1. Clone the repository
Code
git clone https://github.com/dixkox/policy-rag-app.git
cd policy-rag-app
2. Create virtual environment
Code
python -m venv venv
.\venv\Scripts\Activate.ps1
3. Install dependencies
Code
pip install -r requirements.txt
▶️ Running the App
Start FastAPI
Code
uvicorn app.main:app --reload
Open your browser
Code
http://127.0.0.1:8000
📚 RAG Pipeline
Upload policy documents

Chunk documents

Generate embeddings

Store embeddings

Ask a question

Retrieve relevant chunks

LLM synthesizes final answer

📊 Evaluation
Evaluation includes:

Retrieval accuracy

Chunk relevance

Answer quality

Manual scoring rubric

Full evaluation is available in:

design-and-evaluation.md

🎥 Demo Video
Code
/demo/policy-rag-app-demo.mp4
🖼️ Screenshots
Code
/screenshots/
📝 License
MIT License.
