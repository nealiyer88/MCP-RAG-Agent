# MCP Agentic RAG Sandbox — Project Plan (SAVAGE MODE)

## Overview

This file tracks the **step-by-step execution** of the MCP Agentic RAG Sandbox project.  
**Follow SAVAGE MODE: one step at a time, confirm each before proceeding.**  
Development is Cursor IDE–first, leveraging agentic scaffolding, no feature creep, and zero overengineering.

---

## Sequential Roadmap & Checklist

### 1. Scaffold Project Structure (**DONE**)
- [x] Set up `/agents`, `orchestrator.py`, `requirements.txt`, `README.md`
- [x] Create placeholder files:  
  - [x] `/agents/wikipedia_rag_agent.py`  
  - [x] `/agents/web_search_agent.py`

---

### 2. Implement Wikipedia RAG Agent
- [ ] Build class/function in `wikipedia_rag_agent.py` to:
    - [ ] Take a query as input
    - [ ] Return Wikipedia summary via API
    - [ ] Handle errors and empty results

---

### 3. Implement Web Search Agent
- [ ] Build class/function in `web_search_agent.py` to:
    - [ ] Take a query as input
    - [ ] Return concise web search result (DuckDuckGo/Bing API)
    - [ ] Handle errors and edge cases

---

### 4. Build Orchestrator (LLM Brain)
- [ ] In `orchestrator.py`:
    - [ ] Accept user question as input
    - [ ] Route query to correct agent based on logic (or LLM prompt)
    - [ ] Collect agent result
    - [ ] Return final answer to user

---

### 5. Minimal User Interface (Demo Only)
- [ ] Build CLI or Streamlit input:
    - [ ] Accept user question
    - [ ] Display output from orchestrator/agent

---

### 6. README and Requirements
- [ ] Update `README.md`:
    - [ ] Purpose, savage mode, architecture
    - [ ] Run/demo instructions
- [ ] Complete `requirements.txt` with all dependencies

---

### 7. Final Test and Push
- [ ] Run end-to-end demo (question → orchestrator → agent → answer)
- [ ] Fix any issues, add minimal comments
- [ ] Push to GitHub

---

**SAVAGE MODE RULE:**  
After each step, WAIT for explicit confirmation before moving on.  
No skipping, combining, or scope creep.

---

