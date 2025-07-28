import fitz  # PyMuPDF
from langdetect import detect, DetectorFactory
import re

DetectorFactory.seed = 0  # Ensure consistent language detection

def is_heading(text, font_size):
    if font_size > 16:
        return "H1"
    elif font_size > 13:
        return "H2"
    elif font_size > 11:
        return "H3"
    return None

def clean_text(text):
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    if len(text) < 3 or re.match(r'^[\W_]+$', text):
        return None
    return text

def detect_language_safe(text):
    try:
        return detect(text)
    except:
        return "unknown"

def extract_toc_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    title = doc.metadata.get("title", "") or doc[0].get_text().split("\n")[0]

    outline = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                line_text = " ".join([span["text"] for span in line["spans"]]).strip()
                if not line_text:
                    continue
                span_font_sizes = [span["size"] for span in line["spans"]]
                avg_font_size = sum(span_font_sizes) / len(span_font_sizes)

                level = is_heading(line_text, avg_font_size)
                cleaned = clean_text(line_text)

                if level and cleaned:
                    outline.append({
                        "level": level,
                        "text": cleaned,
                        "page": page_num + 1,
                        "language": detect_language_safe(cleaned)
                    })

    if not outline:
        return None

    return {
        "title": title.strip(),
        "outline": outline
    }
