import faiss
import numpy as np
import json
from embeddings.embedder import embed_text

# Load jobs
with open("data/jobs.json", "r") as f:
    jobs = json.load(f)

embeddings = [embed_text(job["description"]) for job in jobs]
dim = len(embeddings[0])

index = faiss.IndexFlatL2(dim)
index.add(np.array(embeddings))

def search_vector(query: str, k=3):
    q_vec = embed_text(query)
    D, I = index.search(np.array([q_vec]), k)

    return [jobs[i] for i in I[0]]