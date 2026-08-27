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

## Final Submission Write‑Up

Policy‑RAG‑App  

(Quantic MSSE AI Engineering Project) 

Name – Tinubu Damilola 

Demo Video Share Link - 27.08.2026_07.53.38_REC 

Google Drive Link - https://drive.google.com/drive/folders/1mcUa6uRahipogZRuYv27NYqDSH0mDMpC?usp=sharing 

Github Link - https://github.com/dixkox/policy-rag-app/tree/master 

 

1. Project Overview 

The Policy‑RAG‑App is a fully functional Retrieval Augmented Generation (RAG) system designed to answer questions about company policies using a deterministic, zero‑cost architecture. The system uses TF‑IDF vectorization, cosine similarity retrieval, heading‑based chunking, and strict guardrails to ensure grounded, accurate, and reproducible answers. 

The project includes: 

A FastAPI backend 

A simple HTML/JS frontend 

A 16‑policy synthetic dataset 

A deterministic RAG pipeline 

A 50‑question evaluation set 

Full documentation (README, design‑and‑evaluation, AI tooling) 

A demo video showing the system running locally 

Deployment is optional and not required for grading; therefore, the system runs locally for the demonstration no deployment 

2. Architecture Summary 

 

The system follows a classical RAG pipeline: 

Ingestion 

Loads .txt policy files from data/policies/ 

Splits documents into chunks using section headings (# Heading) 

Cleans and normalizes text 

Indexing 

Builds a TF‑IDF sparse matrix using scikit‑learn 

Stores vectors in memory for fast lookup 

Retrieval 

Converts user query into TF‑IDF vector 

Computes cosine similarity against all policy chunks 

Selects the highest‑scoring chunk 

Guardrails 

If similarity score < 0.25, the system rejects the question 

Prevents hallucinations and ensures grounded answers 

Answer Generation 

Returns: 

The retrieved policy chunk 

A similarity score 

A citation (filename + section heading) 

Frontend 

Simple HTML interface 

Sends POST requests to /ask 

Displays answer, context, and citation 

3. Policy Dataset (16 Policies) 

The system includes a complete synthetic policy corpus: 

PTO Policy 

Remote Work Policy 

Holiday Policy 

Expense Policy 

Parental Leave Policy 

Code of Conduct 

Security Policy 

Travel Policy 

IT Usage Policy 

Anti‑Harassment Policy 

Attendance Policy 

Benefits Policy 

Reimbursement Policy 

Data Protection Policy 

HR General Policy 

Workplace Behavior Policy 

Each policy exists in: 

.txt format for ingestion 

.md format for human readability 

A script (generate_policies.py) automatically generates missing policies. 

4. Evaluation Summary (50 Questions) 

Metrics Evaluated 

Groundedness 

Relevance 

Correctness 

Citation Accuracy 

Latency (p50/p95) 

Results 

Metric 

Score 

Groundedness 

88% 

Relevance 

86% 

Correctness 

90% 

Citation Accuracy 

90% 

Latency p50 

~720 ms 

Latency p95 

~1380 ms 

 

 

Observations 

TF‑IDF performs strongly for structured policy text 

Guardrails prevent hallucinations effectively 

Latency is well within acceptable limits 

Errors mainly occur with ambiguous or multi‑policy questions 

5. AI Tooling Usage 

AI tools were used responsibly to accelerate development: 

Microsoft Copilot 

Debugging FastAPI 

Improving documentation 

Refining RAG logic 

Cursor IDE 

Project scaffolding 

Code refactoring 

Automated fixes 

Gemini 1.5 Pro 

Architecture reasoning 

Policy text generation 

Evaluation question generation 

Copilot Chat 

Debugging 

Repo cleanup 

Error explanations 

All engineering decisions, integration, and evaluation were performed manually. No copyrighted or proprietary policy documents were used. 

 

6. Demo Video Summary 

The demo video shows: 

My face + ID 

The FastAPI backend running locally 

The frontend answering policy questions 

Guardrails rejecting invalid questions 

Retrieval with citations 

Architecture explanation 

Evaluation results 

GitHub repository walkthrough 

This satisfies all Quantic demo requirements. 

7. GitHub Repository 

Full source code is available at: 

https://github.com/dixkox/policy-rag-app (Maste Default) 

The repository includes: 

Backend 

Frontend 

16‑policy dataset 

Evaluation set 

Documentation 

Policy generation script 

Everything is reproducible and runs locally without deployment. 

8. Conclusion 

The Policy‑RAG‑App meets all Quantic AI Engineering Project requirements: 

Deterministic RAG pipeline 

TF‑IDF ingestion + indexing 

Cosine similarity retrieval 

Guardrails 

FastAPI backend 

Frontend UI 

16‑policy dataset 

50‑question evaluation 

Full documentation 

Demo video 

The system is lightweight, reproducible, academically honest, and fully functional. 

 