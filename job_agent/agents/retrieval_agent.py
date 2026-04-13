import requests

MCP_URL = "http://localhost:8000"

def retrieve_jobs(query: str):
    keyword_results = requests.get(
        f"{MCP_URL}/search_jobs", params={"query": query}
    ).json()

    vector_results = requests.get(
        f"{MCP_URL}/vector_search", params={"query": query}
    ).json()

    return keyword_results + vector_results