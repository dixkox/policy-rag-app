README.md — Policy RAG Application (Quantic AI Engineering Project)
📌 Project Overview
The Policy RAG App is a lightweight Retrieval‑Augmented Generation (RAG) system that answers questions about company policies using:

TF‑IDF vectorization

Cosine similarity retrieval

Chunked policy documents

FastAPI backend

Simple HTML frontend

Guardrails for invalid questions

Citations (file + section heading)

This project fulfills all core requirements of the Quantic AI Engineering Project, including ingestion, indexing, retrieval, evaluation, documentation, and reproducibility.

📁 Repository Structure
Code
policy-rag-app/
│
├── app/
│   ├── main.py                 # FastAPI backend
│   ├── rag_pipeline.py         # TF-IDF ingestion, indexing, retrieval
│
├── data/
│   └── policies/               # Policy .txt files
│
├── frontend/
│   └── index.html              # Simple UI (optional)
│
├── evaluation/
│   └── evaluation_set.md       # Evaluation questions + results
│
├── requirements.txt
├── README.md
├── design-and-evaluation.md
├── ai-tooling.md
└── .gitignore
⚙️ Setup Instructions
1. Clone the repository
Code
git clone https://github.com/dixkox/policy-rag-app.git
cd policy-rag-app
2. Create a virtual environment
Code
python -m venv venv
venv\Scripts\activate         # Windows
source venv/bin/activate      # macOS/Linux
3. Install dependencies
Code
pip install -r requirements.txt
4. Add policy documents
Place your .txt files inside:

Code
data/policies/
Each file should contain headings like:

Code
# PTO Policy
# Code of Conduct
# Security Policy
🚀 Running the Application
Start the FastAPI backend
Run from the project root:

Code
uvicorn app.main:app --reload
Backend will be available at:

Code
http://127.0.0.1:8000
🌐 Start the Frontend (port 5500)
Option 1 — VS Code Live Server (recommended)
Open the project in VS Code

Navigate to frontend/index.html

Right‑click the file

Select “Open with Live Server”

Your browser will automatically open:

Code
http://localhost:5500/
This is your active frontend URL.

Option 2 — Python static server
If you prefer running manually:

Code
cd frontend
python -m http.server 5500
Then open:

Code
http://localhost:5500/
🔌 API Usage
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
  "context": "# PTO Policy\nEmployees accrue PTO...",
  "reason": "Similarity score = 0.312",
  "citation": {
    "file": "pto_policy.txt",
    "section": "PTO Policy"
  }
}
GET /health
Code
http://127.0.0.1:8000/health
Response:

json
{ "status": "ok" }
🧠 RAG Pipeline Summary
Ingestion  
Loads .txt files → splits by headings → cleans text.

Indexing  
TF‑IDF vectorizer → sparse matrix stored in memory.

Retrieval  
Query → TF‑IDF → cosine similarity → best chunk selected.

Guardrails  
If similarity < 0.25, the question is rejected.

Answer Generation  
Returns context + similarity score + citation.

🧪 Evaluation
Full evaluation is documented in:

design-and-evaluation.md

evaluation/evaluation_set.md

Includes:

Groundedness

Citation accuracy

Latency (p50/p95)

30‑question evaluation set

🛠️ AI Tools Used
Documented in:

ai-tooling.md

Tools include:

Microsoft Copilot

Cursor IDE

Gemini 1.5 Pro

🎥 Demo Video Requirements
Your 5–10 minute demo must show:

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

[x] Citations added

[x] Clean GitHub repo

[x] README.md

[x] design-and-evaluation.md

[x] ai-tooling.md

[x] Evaluation set

[x] CI/CD workflow

[ ] Demo video (final step)

[ ] Optional deployment