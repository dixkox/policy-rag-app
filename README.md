A Retrieval‑Augmented Generation (RAG) application that answers questions about company policies using TF‑IDF retrieval, similarity scoring, and guardrails. Built for the Quantic AI Engineering Project.

📌 Project Overview
The Policy RAG App is a lightweight Retrieval‑Augmented Generation system that allows users to ask questions about company policies and receive grounded, context‑based answers.
It uses:

TF‑IDF vectorization

Cosine similarity retrieval

Chunked policy documents

A FastAPI backend

A simple frontend UI

Guardrails to reject irrelevant questions

This project satisfies the core requirements of the Quantic AI Engineering assignment.

📁 Repository Structure
Code
policy-rag-app/
│
├── app/
│   ├── main.py                 # FastAPI application
│   ├── rag_pipeline.py         # TF-IDF ingestion, indexing, retrieval
│   └── __init__.py
│
├── data/
│   └── policies/               # Policy .txt files (your corpus)
│
├── frontend/
│   └── index.html              # Simple UI (if included)
│
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── design-and-evaluation.md    # Architecture + evaluation
├── ai-tooling.md               # AI tools used
└── .gitignore                  # Prevents heavy files from entering repo
⚙️ Setup Instructions
1. Clone the repository
Code
git clone <your-repo-url>
cd policy-rag-app
2. Create a virtual environment
Code
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
3. Install dependencies
Code
pip install -r requirements.txt
4. Add policy documents
Place your .txt policy files inside:

Code
data/policies/
Each file should contain headings like:

Code
# Code of Conduct
# PTO Policy
# Security Policy
The system automatically chunks by headings.

🚀 Running the Application
Start the FastAPI server:
Code
uvicorn app.main:app --reload
Visit the frontend (if included):
Code
http://127.0.0.1:8000
API Endpoint:
POST /ask
Request:

json
{
  "question": "What is the PTO policy?"
}
Response:

json
{
  "answer": "Here is the relevant policy information...",
  "context": "...",
  "reason": "Similarity score = 0.312"
}
🧠 How the RAG Pipeline Works
1. Ingestion
Loads .txt policy files

Splits them into chunks using headings

Cleans text

2. Indexing
TF‑IDF vectorizer

Cosine similarity matrix

Stored in memory (lightweight)

3. Retrieval
Query → TF‑IDF vector

Cosine similarity against all chunks

Best match selected

Threshold applied (rejects irrelevant queries)

4. Guardrails
If similarity < 0.25:

Code
Invalid question. No relevant policy found.
5. Answer Generation
A rule‑based generator formats the answer and includes:

Retrieved context

Query

Similarity score

(Optional) Citation

🧪 Evaluation
Evaluation details are in design-and-evaluation.md, including:

Groundedness

Citation accuracy

Latency (p50/p95)

Evaluation question set (15–30 items)

🛠️ AI Tools Used
Documented in ai-tooling.md, including:

Microsoft Copilot

Cursor IDE

Gemini 1.5 Pro (for code generation)

Automated debugging assistance

🌐 Deployment (Optional)
You may deploy using:

Render

Railway

HuggingFace Spaces

Docker + any cloud provider

Deployment instructions (if used) are in deployed.md.

🎥 Demo Video Requirements
Your submission must include a 5–10 minute demo showing:

App running

Architecture explanation

Evaluation results

Your ID

All group members present

✔️ Submission Checklist
[x] RAG pipeline implemented

[x] TF‑IDF ingestion + indexing

[x] Retrieval + guardrails

[x] FastAPI backend

[x] Clean GitHub repo

[ ] README.md (this file)

[ ] design-and-evaluation.md

[ ] ai-tooling.md

[ ] Evaluation set

[ ] Demo video

[ ] Optional deployment

[ ] CI/CD workflow

