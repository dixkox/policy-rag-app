from fastapi import APIRouter, UploadFile, File
from app.pdf_utils import extract_text_from_pdf
from app.ai_utils import ask_gemini

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text_from_pdf(content)
    return {"text": text}

@router.post("/ask")
async def ask_question(question: str, text: str):
    answer = ask_gemini(question, text)
    return {"answer": answer}
