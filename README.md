# LegalEase — AI-Powered Legal Document Generator

LegalEase is an AI-powered legal document generator built with **Python, Streamlit, FastAPI and Gemini 1.5 Pro**. The user enters the document type, parties, terms and effective date, and gets a structured legal document that can be previewed, edited and downloaded as **TXT, DOCX or PDF**.

## Team
| Name | Email |
|------|-------|
| Bhavadarani M. | bhava.darani.m.25ds008@gmail.com |
| Akila P | akila.p.25ds002@gmail.com |
| Devi Sri B | devi.sri.b25ds010@gmail.com |
| Meenatchi M | meenatchi.m.25ds023@gmail.com |

## Repository Structure
```
LegalEase/
├── 1. Brainstorming & Ideation/     # problem statement, ideas, objective
├── 2. Requirement Analysis/         # functional / non-functional requirements, tech stack
├── 3. Project Design Phase/         # architecture, user flow, API design
├── 4. Project Planning Phase/       # work breakdown, risks
├── 5. Project Development Phase/    # source code (ai_core, frontend, legalEaseAPI ...)
├── 6.Project Testing/               # test cases
├── 7.Project Documentation/         # full project documentation (PDF)
├── 8.Project Demonstration/         # run steps, screenshots, demo
└── README.md
```

## Quick Start
```bash
cd "5. Project Development Phase"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# rename .env.example to .env and add GEMINI_API_KEY
uvicorn legalEaseAPI.main:app --reload      # terminal 1
streamlit run frontend/app.py               # terminal 2
```
Open http://localhost:8501

## Workflow
`USER INPUT → STREAMLIT → FASTAPI → PYDANTIC VALIDATION → GEMINI 1.5 PRO → GENERATED LEGAL DOCUMENT → PREVIEW / EDIT → TXT / DOCX / PDF`

> Generated documents are drafts and should be reviewed by a legal professional before use.
