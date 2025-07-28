import os
import json
from pathlib import Path
from extract_toc import extract_toc_from_pdf

def process_pdfs():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_files = list(input_dir.glob("*.pdf"))

    for pdf_file in pdf_files:
        try:
            toc_data = extract_toc_from_pdf(pdf_file)
            output_file = output_dir / f"{pdf_file.stem}.json"

            # Strip "language" fields if present
            clean_outline = [
                {
                    "level": item["level"],
                    "text": item["text"],
                    "page": item["page"]
                }
                for item in toc_data["outline"]
            ]

            final_output = {
                "title": toc_data["title"],
                "outline": clean_outline
            }

            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(final_output, f, indent=2, ensure_ascii=False)

            print(f"✅ Processed: {pdf_file.name}")

        except Exception as e:
            print(f"❌ Failed: {pdf_file.name} - {e}")

if __name__ == "__main__":
    print("📄 Starting PDF processing...")
    process_pdfs()
    print("✅ All PDFs processed.")
