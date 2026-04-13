from agents.orchestrator import run_pipeline

if __name__ == "__main__":
    print("=== Job Matching Agent ===\n")

    resume_text = input("Paste your resume text:\n")

    results = run_pipeline(resume_text)

    print("\nTop Matches:\n")
    for job in results:
        print(f"{job['title']} at {job['company']}")
        print(f"Score: {job['score']:.2f}")
        print(f"Link: {job['url']}\n")