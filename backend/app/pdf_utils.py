from pypdf import PdfReader
from io import BytesIO

def extract_text_from_pdf(content: bytes) -> str:
    reader = PdfReader(BytesIO(content))
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text
