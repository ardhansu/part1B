import fitz  

def extract_outline_and_chunks(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        for block in text.split("\n\n"):
            cleaned = block.strip()
            if len(cleaned) > 50:
                sections.append({
                    "page_number": page_num,
                    "section_title": cleaned.split('\n')[0][:60],
                    "text": cleaned
                })
    return sections
