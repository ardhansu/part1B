def build_metadata(docs, persona):
    return {
        "input_documents": docs,
        "persona": persona["role"],
        "job_to_be_done": persona["job"]
    }

def build_output_structure(metadata, sections):
    extracted = []
    analysis = []

    for rank, s in enumerate(sections, start=1):
        extracted.append({
            "document": s["document"],
            "page_number": s["page_number"],
            "section_title": s["section_title"],
            "importance_rank": rank
        })
        analysis.append({
            "document": s["document"],
            "page_number": s["page_number"],
            "refined_text": s["text"]
        })

    return {
        "metadata": metadata,
        "extracted_sections": extracted,
        "subsection_analysis": analysis
    }
