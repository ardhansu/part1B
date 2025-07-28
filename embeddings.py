from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')  # ~80MB

def embed_texts(texts):
    return model.encode(texts, convert_to_numpy=True)

def compute_similarity(embeddings, query_embedding, sections):
    results = []
    for i, emb in enumerate(embeddings):
        sim = float(np.dot(emb, query_embedding) / (np.linalg.norm(emb) * np.linalg.norm(query_embedding)))
        sec = sections[i]
        sec["score"] = sim
        results.append(sec)
    return results
