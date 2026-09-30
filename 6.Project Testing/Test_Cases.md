# 6. Project Testing — LegalEase

Sample input used for testing: **Freelance Work Contract** — Jane Doe (Service Provider), TechNova Inc. (Client), effective April 15, 2025.

| ID | Test Case | Steps | Expected Result | Status |
|----|-----------|-------|-----------------|--------|
| TC-01 | Backend health check | Open `GET /` | JSON welcome message returned | ☐ Verify |
| TC-02 | Generate document (valid input) | Fill all four fields → *Generate Document* | Success message, document appears in preview | ✅ Pass (see `8.Project Demonstration/screenshots`) |
| TC-03 | Missing input | Leave one field empty → *Generate Document* | Warning: "Please fill in all fields before generating." | ☐ Verify |
| TC-04 | Invalid request body | `POST /generate` without required field | FastAPI/Pydantic returns HTTP 422 | ☐ Verify |
| TC-05 | Backend not running | Stop Uvicorn → *Generate Document* | Error: "Could not reach the backend" | ☐ Verify |
| TC-06 | Missing / invalid API key | Remove `GEMINI_API_KEY` → generate | Readable error, no crash | ☐ Verify |
| TC-07 | Inline editing | Click *Edit Document* → change text | Edited text is used for downloads | ☐ Verify |
| TC-08 | TXT download | Click *Download as .TXT* | `.txt` file with document text | ☐ Verify |
| TC-09 | DOCX download | Click *Download as .DOCX* | Word file with title, Times New Roman body, footer | ✅ Pass (final document screenshot) |
| TC-10 | PDF download | Click *Download as .PDF* | PDF with title, headings, header/footer | ✅ Pass (final document screenshot) |
| TC-11 | Sanitization | Text with smart quotes / em-dashes | Replaced with plain characters | ☐ Verify |
| TC-12 | Missing logo | Remove `Image/Logo.png` | App still runs with text fallback | ☐ Verify |

Mark each **☐ Verify** row as ✅ / ❌ after running it, and add a screenshot for the result.
