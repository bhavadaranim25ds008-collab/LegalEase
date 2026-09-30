# 4. Project Planning Phase — LegalEase

## Approach
The project was split into independent modules so the four team members could work in parallel: UI, API, AI generation and document formatting.

## Work Breakdown
| Phase | Task | Output | Status |
|-------|------|--------|--------|
| Ideation | Problem statement, idea selection | `1. Brainstorming & Ideation` | Done |
| Requirements | Functional / non-functional requirements, tech stack | `2. Requirement Analysis` | Done |
| Design | Architecture, user flow, API design | `3. Project Design Phase` | Done |
| Development | FastAPI backend (`main.py`, `routes.py`) | `legalEaseAPI/` | Done |
| Development | Gemini generator + prompt builder | `ai_core/` | Done |
| Development | Streamlit UI, preview, editing, downloads | `frontend/app.py` | Done |
| Development | Sanitize / DOCX / PDF / HTML utilities | `frontend/utils.py` | Done |
| Testing | Test cases and validation | `6.Project Testing` | Done |
| Documentation | Project documentation PDF | `7.Project Documentation` | Done |
| Demonstration | Screenshots and demo steps | `8.Project Demonstration` | Done |

## Team
Bhavadarani M., Akila P, Devi Sri B, Meenatchi M

## Risks & Mitigation
| Risk | Mitigation |
|------|-----------|
| Missing / invalid Gemini API key | `config.py` warns on start; key kept in `.env` |
| Gemini quota or network failure | Backend converts errors into an HTTP error response; frontend shows the message |
| Special characters break PDF export | `sanitize_text()` replaces incompatible characters |
| Missing logo file | Logo blocks wrapped in try/except |
| AI output may contain errors | Preview + inline editing before download |

## Tools
VS Code, Python virtual environment (`venv`), GitHub, Uvicorn, Streamlit.
