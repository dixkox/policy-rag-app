ai-tooling.md
AI Tooling Usage for the Policy RAG Application
1. Overview
This document explains how AI tools were used during the development of the Policy RAG Application, built for the Quantic AI Engineering Project.
AI tooling played a major role in accelerating development, debugging, architecture design, and documentation.

The tools used include:

Microsoft Copilot

Cursor IDE (AI pair programmer)

Gemini 1.5 Pro (code generation + architecture reasoning)

Copilot Chat (debugging + refactoring)

These tools helped produce a clean, functional, reproducible RAG system while maintaining full academic integrity.

2. AI Tools Used
2.1 Microsoft Copilot
Used for:

Explaining TF‑IDF retrieval concepts

Helping design guardrails for invalid questions

Debugging FastAPI routing issues

Rewriting documentation (README, design docs, evaluation)

Generating structured code blocks

Fixing retrieval scoring logic

What worked well:  
Copilot was excellent at:

Producing clean Python code

Explaining errors

Suggesting fixes for retrieval logic

Helping rewrite documentation in a professional format

Limitations:

Sometimes produced overly complex RAG architectures

Needed manual simplification to match project requirements

2.2 Cursor IDE (AI Pair Programmer)
Used for:

Auto‑generating project scaffolding

Creating folder structure

Refactoring Python modules

Debugging import errors

Running automated code actions

What worked well:

Cursor’s “Fix” and “Explain” features helped resolve TF‑IDF vectorization errors

Great for cleaning up old RAG code

Helped rebuild the project after accidental folder deletion

Limitations:

Sometimes suggested LangChain or FAISS even though TF‑IDF was required

Needed manual control to keep the project lightweight

2.3 Gemini 1.5 Pro
Used for:

Designing the architecture

Generating evaluation questions

Writing documentation drafts

Explaining chunking strategies

Suggesting improvements to guardrails

What worked well:

Excellent at generating structured documents

Very strong at architecture reasoning

Helped produce evaluation metrics and question sets

Limitations:

Sometimes produced too advanced RAG designs (semantic embeddings, re‑ranking)

Needed simplification to meet Quantic’s “free-tier” requirement

2.4 Copilot Chat (Debugging Assistant)
Used for:

Fixing FastAPI errors

Explaining CORS issues

Debugging frontend fetch failures

Cleaning GitHub repo

Removing heavy files (venv, dist-info, caches)

What worked well:

Very effective at debugging

Helped clean the repo to <10MB

Ensured reproducibility

Limitations:

Sometimes misinterpreted frontend errors as backend issues

3. How AI Tools Improved Development
3.1 Speed
AI tools reduced development time significantly:

RAG pipeline built in hours instead of days

Documentation generated quickly

Debugging accelerated

3.2 Code Quality
AI tools helped:

Remove redundant code

Improve readability

Add guardrails

Fix retrieval scoring

3.3 Architecture Decisions
AI tools helped justify:

TF‑IDF instead of embeddings

Chunking by headings

Cosine similarity retrieval

Threshold‑based guardrails

3.4 Evaluation
AI tools helped generate:

Evaluation questions

Groundedness checks

Citation accuracy tests

Latency measurement scripts

4. What Didn’t Work Well
4.1 Overly Complex Suggestions
Some tools suggested:

LangChain

FAISS

Pinecone

Semantic embeddings

Multi‑stage re‑ranking

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

6. Conclusion
AI tooling significantly improved:

Development speed

Code quality

Documentation clarity

Debugging efficiency

The final Policy RAG Application is a result of human engineering supported by AI tools, aligned with Quantic’s expectations for responsible AI‑assisted development.