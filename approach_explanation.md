Problem Overview
The Round 1B challenge focuses on building an intelligent document processing system that extracts and prioritizes relevant sections and sub-sections from a collection of PDFs. The relevance is determined based on a provided persona and their specific job-to-be-done. The system must adhere to strict constraints, including offline-only execution, CPU usage, and a maximum model size of 1GB, with a processing time limit of 60 seconds for 3–5 documents.

Solution Architecture
The solution follows a modular, resource-efficient architecture, comprising the following key stages:

PDF Text Extraction
Each document is processed using PyMuPDF to extract text from each page. Page content is split into paragraph-level blocks using double newlines. Each block is treated as a candidate section, with the first line used as a pseudo-title.

Section Embedding and Scoring
The persona’s role and job-to-be-done are combined into a single query string. Semantic embeddings for both the query and the candidate sections are generated using the all-MiniLM-L6-v2 model from Sentence Transformers, which is compact (~80MB), fast, and CPU-friendly. Cosine similarity is used to score each section based on its relevance to the query.

Ranking and Filtering
Sections are sorted by their similarity scores. The top-ranked sections are selected for output, with each entry including the source document name, page number, title, and importance rank.

Subsection Refinement
Each selected section includes the full paragraph text, providing contextual information for detailed analysis and future enhancements.

Output Generation
A structured JSON output is generated with metadata, extracted sections, and detailed sub-section analysis, adhering strictly to the challenge format.

Justification for Approach
Semantic Matching: Embedding-based similarity ensures generalization across diverse document types and personas.

Modularity: Components for text extraction, embedding, scoring, and output are isolated, enabling future extension or replacement.

Efficiency: The entire pipeline executes within the specified resource and time constraints on a CPU-based environment.

Offline Compatibility: All models and dependencies are bundled in the Docker image, ensuring fully offline functionality.

Future Enhancements
More advanced persona-contextual prompt engineering for better alignment.

Integration of NER and keyphrase extraction to improve sub-section granularity.

Cross-document linking or summarization for richer insight generation.

