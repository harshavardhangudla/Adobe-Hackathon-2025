import os
import json
from datetime import datetime
from utils import extract_text_by_page, extract_sections, keyword_score

# --- Config ---
PDF_FOLDER = './sample_pdfs/'
PDF_FILES = [os.path.join(PDF_FOLDER, f) for f in os.listdir(PDF_FOLDER) if f.endswith('.pdf')]
PERSONA = "Investment Analyst"
JOB = "Analyze revenue trends, R&D investments, and market positioning strategies"
KEYWORDS = ["revenue", "R&D", "research", "investment", "market positioning", "market"]

# --- Output structure ---
output = {
    "metadata": {
        "input_documents": [os.path.basename(f) for f in PDF_FILES],
        "persona": PERSONA,
        "job_to_be_done": JOB,
        "processing_timestamp": datetime.now().isoformat()
    },
    "extracted_sections": [],
    "subsection_analysis": []
}

for pdf_file in PDF_FILES:
    pages = extract_text_by_page(pdf_file)
    sections = extract_sections(pages)
    for sec in sections:
        score = keyword_score(sec['content'], KEYWORDS)
        if score > 0:
            output['extracted_sections'].append({
                "document": os.path.basename(pdf_file),
                "page_number": sec['page'],
                "section_title": sec['title'],
                "importance_rank": score
            })
            # Simple sub-section: sentence with most keyword hits
            sentences = sec['content'].split('.')
            best_sent = max(sentences, key=lambda s: keyword_score(s, KEYWORDS), default='')
            output['subsection_analysis'].append({
                "document": os.path.basename(pdf_file),
                "refined_text": best_sent.strip(),
                "page_number": sec['page']
            })

# Sort by importance_rank
output['extracted_sections'] = sorted(output['extracted_sections'], key=lambda d: -d['importance_rank'])

with open('challenge1b_output.json', 'w') as f:
    json.dump(output, f, indent=2)
print('Done! Output saved to challenge1b_output.json')
