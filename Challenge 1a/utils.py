from langdetect import detect
import fitz  # PyMuPDF

def detect_language_from_pdf_text(text):
    try:
        return detect(text)
    except:
        return "unknown"

def extract_text_from_first_n_pages(pdf_path, n=3):
    doc = fitz.open(pdf_path)
    text = ""
    for i in range(min(n, len(doc))):
        text += doc[i].get_text()
    return text.strip()
