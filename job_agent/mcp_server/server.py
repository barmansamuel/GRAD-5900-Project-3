from fastapi import FastAPI
from mcp_server.tools.scraper import search_jobs
from mcp_server.tools.vector_search import search_vector

app = FastAPI()

@app.get("/search_jobs")
def search(query: str):
    return search_jobs(query)

@app.get("/vector_search")
def vector(query: str):
    return search_vector(query)