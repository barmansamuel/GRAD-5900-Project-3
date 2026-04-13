import json

def load_jobs():
    with open("data/jobs.json", "r") as f:
        return json.load(f)

def search_jobs(query: str):
    jobs = load_jobs()
    results = []

    for job in jobs:
        if query.lower() in job["description"].lower():
            results.append(job)

    return results