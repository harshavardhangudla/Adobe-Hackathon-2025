## Approach Explanation

My solution extracts relevant sections from documents based on persona needs and outputs a structured JSON:

1. **PDF Parsing**: Each document is processed with PyPDF2. Text is extracted page-wise.
2. **Section Extraction**: Text is split by capitalized lines, treating these as section headers for a simple, domain-agnostic parsing.
3. **Relevance Scoring**: Each section receives a score by counting occurrences of keywords (derived from the job and persona description).
4. **Section Ranking**: Sections are ranked by their scores, ensuring the most relevant appear first.
5. **Sub-section Selection**: For each top section, the sentence with the highest keyword density is chosen as the most relevant sub-section.
6. **Output**: Results, including document name, page, section, rank, and sub-section texts, are written to a JSON file as per challenge requirements.

This method is lightweight, generic, and can adapt keywords/topics to various personas and jobs-to-be-done.
