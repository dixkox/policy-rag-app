# Demo Steps – Policy‑RAG‑App

## 1. Install dependencies
pip install -r requirements.txt

## 2. Start the backend
uvicorn app.main:app --reload

## 3. Open the frontend
Open frontend/index.html in a browser.

## 4. Ask a question
Type a question such as:
- “How should employees request PTO?”
- “What must employees do to maintain information security?”

## 5. View the answer
The retrieved policy chunk appears in the UI.

## 6. View evaluation results
Open evaluation/eval_results.json to see accuracy and latency metrics.

## 7. View architecture
Open screenshots/architecture_diagram.png.
