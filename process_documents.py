from text_extraction import extract_outline_and_chunks
from embeddings import embed_texts, compute_similarity
from utils import build_metadata, build_output_structure

def process_collection(pdf_files, persona, base_dir):
    persona_query = f"{persona['role']}: {persona['job']}"
    
    all_sections = []
    for file in pdf_files:
        path = f"{base_dir}/{file}"
        sections = extract_outline_and_chunks(path)
        for sec in sections:
            sec["document"] = file
        all_sections.extend(sections)

    section_texts = [s["text"] for s in all_sections]
    section_embeddings = embed_texts(section_texts)
    query_embedding = embed_texts([persona_query])[0]

    scored_sections = compute_similarity(section_embeddings, query_embedding, all_sections)

    top_sections = sorted(scored_sections, key=lambda x: x["score"], reverse=True)[:10]

    metadata = build_metadata(pdf_files, persona)
    return build_output_structure(metadata, top_sections)
