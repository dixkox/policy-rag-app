# Policy RAG Application — Quantic AI Engineering Project

## 📌 Project Overview
The Policy‑RAG‑App is a lightweight Retrieval‑Augmented Generation (RAG) system that answers questions about company policies using a fully deterministic classical NLP pipeline. It fulfills all core requirements of the Quantic AI Engineering Project, including ingestion, indexing, retrieval, evaluation, documentation, and reproducibility.

The system includes:

- TF‑IDF vectorization (scikit‑learn)
- Cosine similarity retrieval
- Heading‑based chunking
- FastAPI backend
- Simple HTML frontend
- Guardrails for invalid questions
- Citations (file + section heading)
- Full evaluation across 16 policies

This project is designed for clarity, reproducibility, and ease of debugging.

---

## 📁 Repository Structure

policy-rag-app/
│
├── app/
│   ├── main.py                 # FastAPI backend
│   ├── rag_pipeline.py         # TF-IDF ingestion, indexing, retrieval
│
├── data/
│   ├── policies/               # Policy .txt files (used by RAG)
│   └── raw/                    # Markdown versions of policies
│
├── scripts/
│   └── generate_policies.py    # Auto-generates missing .txt and .md policies
│
├── frontend/
│   └── index.html              # Simple UI
│
├── evaluation/
│   └── evaluation_set.md       # 50 evaluation questions + results
│
├── requirements.txt
├── README.md
├── design-and-evaluation.md
├── ai-tooling.md
└── .gitignore

Code

---

## 📚 Policy Dataset (16 Policies)

The system includes a complete set of **16 company policies**, stored in both `.txt` and `.md` formats:

- PTO Policy  
- Remote Work Policy  
- Holiday Policy  
- Expense Policy  
- Parental Leave Policy  
- Code of Conduct  
- Security Policy  
- Travel Policy  
- IT Usage Policy  
- Anti‑Harassment Policy  
- Attendance Policy  
- Benefits Policy  
- Reimbursement Policy  
- Data Protection Policy  
- HR General Policy  
- Workplace Behavior Policy  

### Automatic Policy Generation
Missing policies can be generated automatically:

python scripts/generate_policies.py

Code

This script creates both `.txt` (used by RAG) and `.md` (human‑readable) versions.

---

## ⚙️ Setup Instructions

### 1. Clone the repository
git clone https://github.com/dixkox/policy-rag-app.git
cd policy-rag-app

Code

### 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate         # Windows
source venv/bin/activate      # macOS/Linux

Code

### 3. Install dependencies
pip install -r requirements.txt

Code

### 4. Ensure policy documents exist
Place `.txt` files inside:

data/policies/

Code

Each file must contain a heading like:

PTO Policy
Code of Conduct
Security Policy
Code

Or generate all missing policies automatically:

python scripts/generate_policies.py

Code

---

## 🚀 Running the Application

### Start the FastAPI backend
uvicorn app.main:app --reload

Code

Backend will be available at:

http://127.0.0.1:8000

Code

---

## 🌐 Start the Frontend (port 5500)

### Option 1 — VS Code Live Server (recommended)
- Open the project in VS Code  
- Navigate to `frontend/index.html`  
- Right‑click → **Open with Live Server**  

Your browser will open:

http://localhost:5500/

Code

### Option 2 — Python static server
cd frontend
python -m http.server 5500

Code

Open:

http://localhost:5500/

Code

---

## 🔌 API Usage

### POST /ask
Request:
```json
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
If similarity < 0.25 → return “Invalid question”.

Answer Generation
Returns:

Retrieved context

Similarity score

Citation (file + section)

🧪 Evaluation
Full evaluation is documented in:

design-and-evaluation.md

evaluation/evaluation_set.md

Includes:

Groundedness

Relevance

Correctness

Citation accuracy

Latency (p50/p95)

50‑question evaluation set across 16 policies

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

[x] 16‑policy dataset

[x] Automatic policy generation script

[x] Citations added

[x] Clean GitHub repo

[x] README.md updated

[x] design-and-evaluation.md updated

[x] ai-tooling.md updated

[x] Evaluation set (50 questions)

[x] CI/CD workflow

[ ] Demo video (final step)

[ ] Optional deployment