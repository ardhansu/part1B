## Problem Overview

The Round 1B challenge focuses on building an intelligent document processing system that extracts and prioritizes the most relevant sections and sub-sections from a collection of PDF documents. Relevance is determined based on a given persona and their specific job-to-be-done. The solution must strictly comply with constraints such as offline execution, CPU-only processing, a maximum model size of 1GB, and a total processing time of 60 seconds for 3–5 documents.

---

## Solution Architecture

The proposed system follows a modular and resource-efficient architecture, consisting of the following stages:

### 1. PDF Text Extraction

Each PDF is parsed using `PyMuPDF`, enabling fast and accurate text extraction. The content of each page is divided into paragraph-level blocks using double newline characters as delimiters. Each block is treated as a candidate section, with its first line assumed to be a pseudo-title.

### 2. Section Embedding and Relevance Scoring

A semantic query is formed by combining the persona's role and their job-to-be-done. Embeddings for both the query and each candidate section are generated using the `all-MiniLM-L6-v2` model from Sentence Transformers. This model is compact (~80MB), CPU-efficient, and well-suited for offline execution. Cosine similarity is used to score each section based on its semantic relevance to the query.

### 3. Ranking and Filtering

All candidate sections are ranked by similarity score. The top-ranked sections are selected and included in the final output. Each entry contains the source document name, page number, pseudo-title, and an importance rank indicating relevance.

### 4. Subsection Refinement

The complete paragraph text of each selected section is preserved, allowing for further sub-section analysis. This provides additional context and lays the groundwork for deeper summarization or linking in future iterations.

### 5. Output Generation

The final structured JSON output includes:
- Metadata (input documents, persona, job-to-be-done, and processing timestamp)
- Extracted sections with page number, title, and ranking
- Subsection analysis with refined text and page-level context

The output strictly follows the challenge’s required schema.

---

## Justification for Approach

- **Semantic Matching:** Embedding-based similarity ensures robustness across diverse document types and persona-job combinations.
- **Modularity:** Text extraction, embedding, scoring, and output generation are cleanly separated to ensure maintainability and flexibility.
- **Efficiency:** The pipeline operates well within the provided computational and time constraints, using CPU-only processing.
- **Offline Compatibility:** All dependencies and models are bundled inside the Docker image, ensuring full offline operability.

---

## Future Enhancements

- Incorporation of more advanced persona-aware prompt engineering for improved alignment and section understanding.
- Use of Named Entity Recognition (NER) and keyphrase extraction to enhance sub-section granularity and detail.
- Cross-document linking and abstractive summarization to enable deeper insights and better context synthesis.

