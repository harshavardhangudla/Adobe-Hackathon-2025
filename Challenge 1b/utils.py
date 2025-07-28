import PyPDF2

def extract_text_by_page(pdf_path):
    text_by_page = []
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text_by_page.append(page.extract_text())
    return text_by_page

def extract_sections(text_by_page):
    # Naive approach: split text by lines with capitalized lines as section titles
    sections = []
    for page_num, page_text in enumerate(text_by_page):
        lines = page_text.split('\n') if page_text else []
        current_section = None
        for line in lines:
            if line.isupper() and len(line.split()) < 10:
                # Likely a section header
                if current_section:
                    sections.append(current_section)
                current_section = {
                    'title': line.strip(),
                    'page': page_num + 1,
                    'content': ''
                }
            elif current_section:
                current_section['content'] += line + ' '
        if current_section:
            sections.append(current_section)
    return sections

def keyword_score(section_text, keywords):
    score = 0
    for kw in keywords:
        score += section_text.lower().count(kw.lower())
    return score
