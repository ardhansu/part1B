import os
import json
from datetime import datetime
from process_documents import process_collection

INPUT_DIR = "/app/input"
OUTPUT_DIR = "/app/output"

persona = {
    "role": "PhD Researcher in Computational Biology",
    "job": "Prepare a literature review focusing on methodologies, datasets, and performance benchmarks"
}

def main():
    pdf_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".pdf")]
    if not pdf_files:
        print("No PDFs found in input.")
        return

    result = process_collection(pdf_files, persona, INPUT_DIR)

    timestamp = datetime.utcnow().isoformat() + "Z"
    result["metadata"]["timestamp"] = timestamp

    with open(os.path.join(OUTPUT_DIR, "output.json"), "w") as f:
        json.dump(result, f, indent=2)
    print("✅ Output written to output/output.json")

if __name__ == "__main__":
    main()
