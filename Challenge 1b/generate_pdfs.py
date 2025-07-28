from fpdf import FPDF

def make_sample_pdf(filename, sections):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for title, content in sections:
        pdf.set_font("Arial", 'B', size=13)
        pdf.cell(0, 10, title, ln=1)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, content)
        pdf.ln(5)
    pdf.output(filename)

sample_docs = [
    {
        "filename": "sample1_company_analysis.pdf",
        "sections": [
            ("REVENUE TRENDS", 
             "The company's revenue increased by 12% driven by strong market positioning. Further analysis on R&D investments is below."),
            ("R&D INVESTMENTS",
             "Research and development received increased funding this year. The main focus was AI and automation."),
            ("CONCLUSION",
             "The company's market share continues to grow. Future recommendations include further R&D spending."),
        ]
    },
    {
        "filename": "sample2_student_guide.pdf",
        "sections": [
            ("STUDY TIPS", 
             "Effective study habits include consistency and using past exams for practice."),
            ("MARKET ANALYSIS SUMMARY",
             "Markets this year were volatile, influencing both investment and R&D strategies."),
            ("EXAM QUESTIONS",
             "What is market positioning? How does investment affect revenue?"),
        ]
    }
]

if __name__ == "__main__":
    import os
    os.makedirs("sample_pdfs", exist_ok=True)
    for doc in sample_docs:
        path = os.path.join("sample_pdfs", doc["filename"])
        make_sample_pdf(path, doc["sections"])
    print("Sample PDFs created in the 'sample_pdfs' folder.")
