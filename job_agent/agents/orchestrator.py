from agents.resume_agent import process_resume
from agents.retrieval_agent import retrieve_jobs
from agents.ranking_agent import rank_jobs

def run_pipeline(resume_text: str):
    parsed = process_resume(resume_text)

    # Use raw resume for now (can improve later)
    jobs = retrieve_jobs(resume_text)

    ranked = rank_jobs(resume_text, jobs)

    return ranked[:5]