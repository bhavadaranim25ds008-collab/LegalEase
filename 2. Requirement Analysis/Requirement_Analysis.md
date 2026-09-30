# 2. Requirement Analysis — LegalEase

## Functional Requirements
| ID | Requirement |
|----|-------------|
| FR-1 | User can enter Document Type, Parties Involved, Terms & Conditions and Effective Date |
| FR-2 | Frontend sends the inputs to the backend using `POST /generate` |
| FR-3 | Backend validates the request (Pydantic `DocumentRequest`) |
| FR-4 | Backend calls Gemini 1.5 Pro with a structured prompt and returns the text in the `document` field |
| FR-5 | Generated text is sanitized (typographic characters replaced, extra blank lines collapsed) |
| FR-6 | User can preview the generated document and edit it inline |
| FR-7 | User can download the document as TXT, DOCX and PDF |
| FR-8 | Errors (missing fields, backend unreachable, generation failure) are shown to the user |

## Non-Functional Requirements
| Area | Requirement |
|------|-------------|
| Usability | Single-page form, no login, four inputs only |
| Modularity | UI, API, AI logic and formatting utilities are separate modules |
| Configuration | API key and model name loaded from `.env`, never hard-coded |
| Reliability | App still runs if the logo image is missing |
| Performance | Frontend request timeout of 60 seconds for AI generation |

## Inputs / Outputs
| Input | Description |
|-------|-------------|
| `document_type` | Type of legal document (e.g. Freelance Work Contract, NDA) |
| `parties` | Parties involved |
| `terms` | Terms and conditions (semicolon-separated for bullets) |
| `dates` | Effective date |

**Output:** JSON `{ "document": "<generated text>" }` → preview / edit → TXT / DOCX / PDF.

## Technical Stack
| Layer | Technology |
|-------|-----------|
| Language | Python |
| Frontend | Streamlit |
| Backend | FastAPI + Uvicorn |
| Validation | Pydantic |
| AI model | Gemini 1.5 Pro (`google-generativeai`) |
| Export | python-docx (DOCX), fpdf2 (PDF), Pillow (images) |
| Others | Requests (HTTP), python-dotenv (config) |

## Python Dependencies (`requirements.txt`)
`fastapi`, `uvicorn[standard]`, `streamlit`, `python-docx`, `fpdf2`, `Pillow`, `requests`, `google-generativeai`, `python-dotenv`, `pydantic`

## Constraints / Assumptions
- A valid Gemini API key with quota is required.
- The FastAPI backend must be running before the user clicks *Generate Document*.
- Generated documents are drafts and need legal review.
