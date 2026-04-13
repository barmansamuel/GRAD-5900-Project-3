from models.ollama_client import call_llm

def process_resume(text: str):
    prompt = f"""
    Extract:
    - skills
    - job titles
    - seniority level

    Resume:
    {text}

    Return clean JSON.
    """
    return call_llm(prompt)