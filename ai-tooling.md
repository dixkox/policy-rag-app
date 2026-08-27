ai-tooling.md
AI Tooling Usage for the Policy RAG Application (Quantic AI Engineering Project)
1. Overview
This document explains how AI tools were used during the development of the Policy RAG Application, built for the Quantic AI Engineering Project.
AI tooling accelerated development, debugging, architecture design, policy generation, and documentation while maintaining full academic integrity.

The tools used include:

Microsoft Copilot

Cursor IDE (AI pair programmer)

Gemini 1.5 Pro

Copilot Chat

These tools helped produce a clean, functional, reproducible RAG system with a complete 16‑policy dataset, 50‑question evaluation, and automated policy generation scripts.

2. AI Tools Used
2.1 Microsoft Copilot
Used for:

Explaining TF‑IDF retrieval and cosine similarity

Designing guardrails for invalid questions

Debugging FastAPI routing and JSON responses

Rewriting documentation (README, design docs, evaluation)

Generating structured Python code

Helping create the 16‑policy dataset

Improving the evaluation scoring templates

What worked well:

Produced clean, readable Python code

Excellent at explaining errors and suggesting fixes

Strong at rewriting documentation professionally

Helped refine the RAG pipeline logic

Limitations:

Sometimes suggested overly complex architectures (FAISS, embeddings)

Needed simplification to meet Quantic’s “free‑tier” requirement

2.2 Cursor IDE (AI Pair Programmer)
Used for:

Auto‑generating project scaffolding

Creating folder structure (app/, data/, scripts/)

Refactoring Python modules

Debugging import errors and path issues

Running automated code actions

Rebuilding the project after accidental folder deletion

Assisting with the policy‑generation script

What worked well:

“Fix” and “Explain” features resolved TF‑IDF vectorization errors

Cleaned up old RAG code

Helped maintain consistent formatting across modules

Limitations:

Sometimes suggested LangChain or FAISS (not allowed for this project)

Needed manual control to keep the system lightweight

2.3 Gemini 1.5 Pro
Used for:

Designing the initial architecture

Generating evaluation questions (expanded to 50)

Writing documentation drafts

Explaining chunking strategies

Suggesting improvements to guardrails

Helping design the 16‑policy dataset

What worked well:

Excellent at generating structured documents

Strong architecture reasoning

Helped produce evaluation metrics and question sets

Useful for policy text generation

Limitations:

Sometimes produced advanced RAG designs (semantic embeddings, reranking)

Needed simplification to meet Quantic’s “zero‑cost” requirement

2.4 Copilot Chat (Debugging Assistant)
Used for:

Fixing FastAPI errors

Explaining CORS issues

Debugging frontend fetch failures

Cleaning GitHub repo

Removing heavy files (venv, dist‑info, caches)

Helping validate the ingestion of all 16 policies

What worked well:

Very effective at debugging

Helped reduce repo size to <10MB

Ensured reproducibility and clean structure

Limitations:

Occasionally misinterpreted frontend errors as backend issues

3. How AI Tools Improved Development
3.1 Speed
AI tools significantly reduced development time:

RAG pipeline built in hours instead of days

16‑policy dataset generated quickly

Documentation produced rapidly

Debugging accelerated

3.2 Code Quality
AI tools helped:

Remove redundant code

Improve readability

Add guardrails

Fix retrieval scoring

Maintain consistent formatting

3.3 Architecture Decisions
AI tools helped justify:

TF‑IDF instead of embeddings

Chunking by headings

Cosine similarity retrieval

Threshold‑based guardrails

Deterministic, zero‑cost design

3.4 Evaluation
AI tools helped generate:

50 evaluation questions

Groundedness checks

Citation accuracy tests

Latency measurement scripts

Evaluation templates

4. What Didn’t Work Well
4.1 Overly Complex Suggestions
Some tools suggested:

LangChain

FAISS

Pinecone

Semantic embeddings

Multi‑stage reranking

These were beyond the scope of the project and had to be simplified.

4.2 Ambiguous Debugging
AI sometimes misdiagnosed:

Frontend errors

Browser extension issues

CORS failures

Manual debugging was still required.

4.3 Documentation Drift
AI occasionally generated documentation that didn’t match the final architecture, requiring manual alignment.

5. Academic Integrity Statement
AI tools were used as assistants, not as replacements for engineering work.
All architectural decisions, debugging, evaluation, and integration were performed manually, with AI providing guidance, drafts, and suggestions.

No external copyrighted code or proprietary policy documents were used.
All policy documents were synthetically generated for this project.

6. Conclusion
AI tooling significantly improved:

Development speed

Code quality

Documentation clarity

Debugging efficiency

Dataset generation

Evaluation completeness

The final Policy RAG Application is a result of human engineering supported by AI tools, aligned with Quantic’s expectations for responsible AI‑assisted development.