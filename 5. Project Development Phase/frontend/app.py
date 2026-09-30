"""
frontend/app.py

Streamlit UI for LegalEase. Collects document details, calls the FastAPI
backend to generate content via Gemini, previews it, and offers
.txt / .docx / .pdf downloads.

Run with (from project root):
    streamlit run frontend/app.py
(Make sure the FastAPI backend is running first: uvicorn legalEaseAPI.main:app --reload)
"""

import sys
from pathlib import Path

# Allow imports from project root when run via `streamlit run frontend/app.py`
sys.path.append(str(Path(__file__).resolve().parent.parent))

import requests
import streamlit as st

from config import WEB_LOGO_PATH, BACKEND_URL
from frontend.utils import sanitize_text, format_docx, format_pdf, format_html_preview

st.set_page_config(page_title="LegalEase", layout="centered")

# --- Header ---------------------------------------------------------------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image(WEB_LOGO_PATH, use_container_width=True)
    except Exception:
        st.markdown("### ⚖️ LegalEase")

st.markdown(
    "<h2 style='text-align: center;'>AI Legal Document Generator</h2>",
    unsafe_allow_html=True,
)

# --- Inputs -----------------------------------------------------------
document_type = st.text_input("Document Type (Ex: Agreement, Contract, NDA)")
parties = st.text_area("Parties Involved")
terms = st.text_area("Terms & Conditions (Use semicolons for bullet points)")
dates = st.text_input("Effective Date")

if "generated_text" not in st.session_state:
    st.session_state.generated_text = ""
if "show_edit" not in st.session_state:
    st.session_state.show_edit = False

# --- Generate ---------------------------------------------------------
if st.button("Generate Document"):
    if not all([document_type, parties, terms, dates]):
        st.warning("Please fill in all fields before generating.")
    else:
        with st.spinner("Generating document with Gemini..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/generate",
                    json={
                        "document_type": document_type,
                        "parties": parties,
                        "terms": terms,
                        "dates": dates,
                    },
                    timeout=60,
                )
                response.raise_for_status()
                st.session_state.generated_text = sanitize_text(response.json()["document"])
                st.success("✅ Document Generated Successfully!")
            except requests.exceptions.RequestException as exc:
                st.error(f"Could not reach the backend: {exc}")

# --- Preview + Edit + Download --------------------------------------------
if st.session_state.generated_text:
    generated_text = st.session_state.generated_text

    styled_html = format_html_preview(generated_text)
    st.markdown(
        f"<div style='background:#111418; padding:20px; border-radius:8px; "
        f"max-height:400px; overflow-y:auto;'>{styled_html}</div>",
        unsafe_allow_html=True,
    )

    if st.button("✏️ Click to Edit Document"):
        st.session_state.show_edit = not st.session_state.show_edit

    if st.session_state.show_edit:
        edited_text = st.text_area(
            "Edit Document Below:", generated_text, height=300
        )
        st.session_state.generated_text = edited_text
        generated_text = edited_text

    file_stub = document_type.replace(" ", "_").lower() or "document"

    st.download_button(
        "📄 Download as .TXT",
        data=generated_text,
        file_name=f"{file_stub}.txt",
        mime="text/plain",
    )
    st.download_button(
        "📝 Download as .DOCX",
        data=format_docx(generated_text, document_type),
        file_name=f"{file_stub}.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
    st.download_button(
        "📕 Download as .PDF",
        data=format_pdf(generated_text, document_type),
        file_name=f"{file_stub}.pdf",
        mime="application/pdf",
    )
else:
    st.info("Click 'Generate Document' to start")
