# GRAD-5900-Project-3
# Job Matching Multi-Agent System (Local, Free)

## Features
- Local LLM via Ollama
- Multi-agent pipeline
- MCP-style API server
- FAISS vector search
- Resume → job matching

## Setup

### 1. Install dependencies
python -m venv venv
pip install -r requirements.txt

### 2. Start Ollama
Install Ollama and run:
ollama run llama3

### 3. Start MCP server
uvicorn mcp_server.server:app --reload

### 4. Run app
python app.py

## Future Improvements
- Real job scraping (Playwright)
- Better resume parsing
- LangGraph orchestration
- UI (Streamlit)
