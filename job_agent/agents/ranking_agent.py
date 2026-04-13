from embeddings.embedder import embed_text
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def rank_jobs(resume_text: str, jobs: list):
    resume_vec = embed_text(resume_text)

    scored = []
    for job in jobs:
        job_vec = embed_text(job["description"])
        score = cosine_similarity(resume_vec, job_vec)
        job["score"] = float(score)
        scored.append(job)

    return sorted(scored, key=lambda x: x["score"], reverse=True)