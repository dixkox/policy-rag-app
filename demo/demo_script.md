# Demo Script – Policy‑RAG‑App

## 1. Introduction
Hello, my name is Tinubu, and this is my demo of the Policy‑RAG‑App, a lightweight retrieval system built using FastAPI, TF‑IDF, and cosine similarity.

## 2. System Overview
The app uses heading‑based chunking, TF‑IDF vectorization, and cosine similarity to retrieve grounded policy answers. There is no LLM generation.

## 3. Running the Backend
I start the backend using:
uvicorn app.main:app --reload

## 4. Frontend Demo
I open index.html and ask questions such as:
- “How should employees request PTO?”
- “Do unused PTO hours roll over?”
- “What must employees do to maintain information security?”

The app retrieves the correct policy chunk and displays it.

## 5. Evaluation
I show eval_results.json and explain accuracy, groundedness, and latency.

## 6. Architecture
I show the TF‑IDF architecture diagram.

## 7. Conclusion
This completes the demo of the Policy‑RAG‑App.
