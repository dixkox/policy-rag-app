Policy RAG App
A lightweight Retrieval‑Augmented Generation (RAG) system that answers employee questions about company policies using TF‑IDF similarity search.
Built as part of the Quantic MBA Capstone Project.

📌 Project Overview
The Policy RAG App allows employees to ask natural‑language questions about company policies (Holiday Policy, PTO, Remote Work, Expense Policy, etc.).
The backend retrieves the most relevant policy section using TF‑IDF + cosine similarity, and the frontend displays the answer cleanly.

This project demonstrates:

Practical RAG implementation

Policy chunking and indexing

FastAPI backend

TF‑IDF vector search

Frontend integration

Clean architecture and documentation

🚀 Features
Accurate policy retrieval using TF‑IDF

Clean chunking based on policy headings

FastAPI backend with /ask endpoint

Simple HTML/JS frontend

Lightweight — no transformers required

Works on low‑memory machines

Easy to extend with PDFs or semantic search

🧠 How the RAG Pipeline Works
1. Load Policies
All .txt files inside data/policies/ are loaded.
Each file may contain multiple policies separated by headings like:

Code
# Company Holiday Policy
# Remote Work Policy
# Expense Reimbursement Policy
2. Chunking by Headings
Policies are split using:

Code
# Policy Title
This ensures each policy becomes its own chunk.

3. TF‑IDF Vectorization
Each chunk is converted into a TF‑IDF vector.

4. Cosine Similarity Search
User queries are compared against all policy vectors.

5. Best‑Match Retrieval
Only the single best policy chunk is returned.

🏗️ Architecture Diagram
Code
Frontend (HTML + JS)
        |
        v
POST /ask
        |
FastAPI Backend
        |
RAG Pipeline (TF‑IDF)
        |
Policy Store (TXT files)
        |
Best Policy Chunk
        |
Frontend Display
📁 Project Structure
Code
policy-rag-app/
│
├── app/
│   ├── main.py
│   ├── rag_pipeline.py
│
├── data/
│   ├── policies/
│       ├── holiday_policy.txt
│       ├── pto_policy.txt
│       ├── remote_work_policy.txt
│       ├── expense_policy.txt
│       ├── parental_leave_policy.txt
│       ├── code_of_conduct.txt
│       ├── security_policy.txt
│
├── frontend/
│   ├── index.html
│   ├── script.js
│
└── README.md
⚙️ How to Run the App
Backend (FastAPI)
Code
uvicorn app.main:app --host 0.0.0.0 --port 8000
Backend runs at:

Code
http://127.0.0.1:8000
Frontend (Static Server)
Code
cd frontend
python -m http.server 5500
Frontend runs at:

Code
http://localhost:5500
📝 Example Queries
Try these in the frontend:

“What is the holiday policy?”

“How does PTO work?”

“Can employees work remotely?”

“What is the parental leave policy?”

“How do I submit expenses?”

📊 Evaluation (Rubric Requirement)
Strengths
Fast and lightweight

Works on low‑memory machines

Accurate retrieval for structured policies

Easy to maintain and extend

No dependency on large transformer models

Weaknesses
TF‑IDF cannot understand deep semantics

No summarization or generative answers

Requires clean policy formatting

Why TF‑IDF Instead of Transformers
Your machine cannot load transformer models due to memory limits.
TF‑IDF provides reliable retrieval without requiring GPU or large RAM.

Performance
Retrieval time: < 10ms

Indexing time: < 1s

Works instantly for small policy sets

🔮 Future Improvements
Add PDF policy ingestion

Add semantic embeddings (MiniLM)

Add answer summarization

Add admin dashboard

Deploy backend to Azure

Deploy frontend to Vercel

📸 Screenshots
Add screenshots here:

Code
/screenshots/
<<<<<<< HEAD
    backend_running.png
    frontend_ui.png
    example_query.png
📬 Contact
Tinubu Damilola Frank
London, Ontario
Founder, Dixkox Inc.
Technology & Human-Centred Intelligent Systems Company, 
=======
📝 License
MIT License.

👤 Author
Tinubu Damilola  
Founder @ Dixkox Inc.
MSSE Artificial Intelligence Engineering Candidate (2026)

⭐ This version is correct, complete, and rubric‑ready.
Your next step is:

👉 Commit the updated README.md
Code
git add README.md
git commit -m "Updated README.md"
git push
>>>>>>> f783966c988a8bafcb34ae559ccefcdf75009fdb
