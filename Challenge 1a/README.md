
# Challenge 1a: PDF Processing Solution

## Overview
This repository presents a **complete solution** for Challenge 1a of the Adobe India Hackathon 2025. The goal is to extract structured table-of-content (TOC) data from PDF files and output this information in a standardized JSON format. The solution is **Dockerized**, CPU-efficient, and conforms to the challenge’s constraints.

---

## 🚀 Features
- Fully automated PDF TOC extraction
- Outputs structured JSON conforming to a schema
- Lightweight and fast (under 10 seconds for 50 pages)
- No internet dependency at runtime
- Dockerized for easy deployment

---

## 📁 Repository Structure

```
Challenge_1a/
├── sample_dataset/
│   ├── outputs/               # JSON output files
│   ├── pdfs/                  # Input PDF files
│   └── schema/
│       └── output_schema.json
├── process_pdfs.py            # PDF processing script
├── extract_toc.py             # TOC extraction logic
├── utils.py                   # Language detection and text utilities
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Container setup
└── README.md                  # Project documentation
```

---

## 📦 Dependencies

Install these Python packages inside your Docker container:
```
PyMuPDF==1.23.20  
langdetect==1.0.9
```

These are already listed in the `requirements.txt` file.

---

## 🐳 Docker Setup

### Build Command
```bash
docker build --platform linux/amd64 -t pdf-processor .
```

### Run Command
```bash
docker run --rm \
  -v $(pwd)/sample_dataset/pdfs:/app/input:ro \
  -v $(pwd)/sample_dataset/outputs:/app/output \
  --network none \
  pdf-processor
```

---

## 🧠 How It Works

### `process_pdfs.py` [📄 Main Script]
- Reads PDFs from `/app/input`
- For each `.pdf`, extracts headings and TOC using `extract_toc_from_pdf`
- Removes language metadata
- Saves output as `filename.json` in `/app/output`

### `extract_toc.py` [🧠 Core Logic]
- Uses PyMuPDF to parse PDF pages
- Heuristically determines heading levels (`H1`, `H2`, `H3`) based on font sizes
- Cleans and filters lines
- Detects language (optional) and builds a structured TOC

### `utils.py` [🔧 Utilities]
- Extracts text from the first few pages
- Detects document language (not used in final output but available)

---

## 📤 Output Format

Each output `.json` follows the schema defined in:
```
sample_dataset/schema/output_schema.json
```

### Example
```json
{
  "title": "Sample PDF Title",
  "outline": [
    {
      "level": "H1",
      "text": "Introduction",
      "page": 1
    },
    {
      "level": "H2",
      "text": "Subsection A",
      "page": 2
    }
  ]
}
```

---

## 🧪 Testing Strategy

### Local Testing
```bash
docker build --platform linux/amd64 -t pdf-processor .
docker run --rm \
  -v $(pwd)/sample_dataset/pdfs:/app/input:ro \
  -v $(pwd)/sample_dataset/outputs:/app/output \
  --network none \
  pdf-processor
```

### Validation Checklist
- ✅ All `.pdf` files processed automatically
- ✅ Output `.json` files generated per input
- ✅ Output matches `output_schema.json`
- ✅ Processing time within 10 seconds for 50-page PDFs
- ✅ No internet access required during runtime
- ✅ Memory usage ≤ 16GB
- ✅ Architecture: AMD64 compliant

---

## ⚠️ Challenge Constraints Recap

| Constraint              | Value                          |
|-------------------------|-------------------------------|
| Execution Time          | ≤ 10s for 50-page PDFs        |
| Model Size              | ≤ 200MB (none used here)      |
| CPU Architecture        | AMD64 only (no ARM)           |
| Internet Access         | Disabled at runtime           |
| Max CPU & RAM           | 8 CPUs, 16 GB RAM             |
| Input Directory         | `/app/input` (read-only)      |
| Output Format           | JSON matching given schema    |

---

## 📌 Notes
- This is a working **reference implementation**.
- You are encouraged to build upon it, optimize the logic, and extend support for tables, images, or layout-aware TOC extraction.
- Language detection is included in the intermediate logic for extensibility, though it’s excluded in the final JSON.

---

## 📬 Contact
For any queries or contributions, feel free to raise an issue or pull request in this repository.

---

> **Disclaimer**: This is a sample submission. Participants must ensure originality and comply with Adobe Hackathon guidelines.

---

## 🧩 Approach

This solution follows a rule-based, lightweight methodology for extracting structured outlines (Table of Contents) from PDF documents:

### 1. **PDF Parsing with PyMuPDF**
- Utilizes the `fitz` module (PyMuPDF) for accessing page-level data including text blocks, fonts, and coordinates.
- Extracts text using `"dict"` mode to retain structural granularity (like font size per span).

### 2. **Heading Detection Logic**
- Assigns TOC levels (`H1`, `H2`, `H3`) based on average font size:
  - Font size > 16 → H1
  - Font size > 13 → H2
  - Font size > 11 → H3
- Filters out lines with low confidence (e.g., too short or containing only symbols).

### 3. **TOC Construction**
- Iterates through each page and line in the PDF.
- Cleans and verifies each text line.
- Constructs a nested TOC-like `outline` list with heading level, text, page number, and language.

### 4. **Language Detection**
- `langdetect` is used to optionally capture the language of each heading (useful for multilingual PDFs).
- For the final output, the language field is stripped to adhere to the required JSON schema.

### 5. **Output Serialization**
- Outputs the final structured TOC in JSON format.
- Each file is saved as `filename.json` matching the input `filename.pdf`.

### 6. **Containerization with Docker**
- The code is wrapped inside a Docker container.
- Uses a minimal Python base image and disables networking to conform to the hackathon runtime constraints.

This approach provides a fast, robust, and extensible foundation that satisfies all the challenge constraints while offering room for future enhancements such as:
- Hierarchical TOC tree construction
- Table and image parsing
- PDF layout analysis and semantic sectioning
