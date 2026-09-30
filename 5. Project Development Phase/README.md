# LegalEase — AI-Powered Legal Document Generator

## Folder structure
```
LegalEase/
├── ai_core/
│   └── gemini_generator.py   # Gemini prompt + API call
├── frontend/
│   ├── app.py                 # Streamlit UI
│   └── utils.py                # sanitize_text / format_docx / format_pdf / format_html_preview
├── legalEaseAPI/
│   ├── main.py                 # FastAPI app entrypoint
│   └── routes.py               # /generate endpoint + DocumentRequest schema
├── Image/                     # put Logo.png + inverseLogo.png here
├── config.py                   # env vars & shared paths
├── requirements.txt
├── .env.example                # rename to .env and add your key
└── run.sh                      # starts backend + frontend together
```

## Setup (VS Code)

1. Open the `LegalEase` folder in VS Code.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and paste in your Gemini API key
   (get one from https://aistudio.google.com/app/apikey).
5. Drop your logo files into `Image/Logo.png` and `Image/inverseLogo.png`
   (the app still runs fine without them — the logo blocks are wrapped
   in try/except).

## Run it

**Option A — one command:**
```bash
bash run.sh
```

**Option B — two terminals:**
```bash
# Terminal 1 — backend
uvicorn legalEaseAPI.main:app --reload

# Terminal 2 — frontend
streamlit run frontend/app.py
```

Then open http://localhost:8501 in your browser.

## Notes
- The backend must be running before you click "Generate Document" in
  the Streamlit app, since the frontend calls `POST /generate` over HTTP.
- `gemini-1.5-pro` requires a valid Google Generative AI API key with
  billing/quota enabled on your Google account.
