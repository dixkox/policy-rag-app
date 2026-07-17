# Policy‑RAG‑App

A Retrieval‑Augmented Generation (RAG) application designed to answer policy‑related questions using vector search, document embeddings, and a FastAPI backend. Built as part of the Quantic Executive MBA Capstone Project.

---

## 🚀 Overview

Policy‑RAG‑App allows users to upload policy documents, convert them into vector embeddings, store them in a vector database, and retrieve relevant chunks when answering questions. The system combines:

- Document ingestion
- Chunking
- Embedding generation
- Vector search
- RAG answer synthesis
- FastAPI backend
- Simple web UI

---

## 🧠 Architecture


### Components

- **FastAPI Backend** — Handles ingestion, retrieval, and RAG queries.
- **Vector Store (ChromaDB / FAISS)** — Stores embeddings for fast similarity search.
- **Embedding Model** — Converts text into numerical vectors.
- **LLM** — Generates final answers using retrieved context.
- **Frontend UI** — Simple interface for asking questions and viewing results.

---

## 📁 Project Structure


---

## ⚙️ Installation

### 1. Clone the repository


### 2. Create virtual environment


### 3. Install dependencies


---

## ▶️ Running the App


Open your browser:


---

## 📚 RAG Pipeline

1. **Upload policy documents**
2. **Chunk documents into segments**
3. **Generate embeddings**
4. **Store embeddings in vector database**
5. **User asks a question**
6. **Retrieve top‑k relevant chunks**
7. **LLM synthesizes final answer**

---

## 📊 Evaluation

The evaluation includes:

- Retrieval accuracy
- Chunk relevance
- Answer quality
- Manual scoring rubric
- Example policy questions

Full evaluation is available in:

- `design-and-evaluation.md`

---

## 🎥 Demo Video

The demo video is located in:


---

## 📝 License

MIT License.

---

## 👤 Author

**Tinubu Damilola**  
Founder & Systems Architect, Dixkox Inc.  
Quantic Executive MBA Candidate (2026)
