from models.ollama_client import call_llm

def parse_resume(text: str):
    prompt = f"""
    Extract skills, job titles, and experience level from this resume:

    {text}

    Return JSON with keys: skills, titles, experience_level
    """
    return call_llm(prompt)