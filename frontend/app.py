import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import requests
import streamlit as st

from ai_core.generator import (
    format_docx,
    format_html_preview,
    format_pdf,
    sanitize_text,
)
from config import API_URL

IMG_DIR = ROOT / "Image"

st.set_page_config(page_title="LegalEase", page_icon="⚖️", layout="centered")

for key, default in {
    "generated_text": "",
    "doc_type": "",
    "terms": "",
    "show_edit": False,
}.items():
    st.session_state.setdefault(key, default)

if st.session_state.show_edit and "edit_area" in st.session_state:
    st.session_state.generated_text = st.session_state.edit_area


def toggle_edit():
    st.session_state.show_edit = not st.session_state.show_edit
    if st.session_state.show_edit:
        st.session_state.edit_area = st.session_state.generated_text


def safe_export(func, *args):
    try:
        return func(*args)
    except Exception as e:
        st.error(f"Export failed: {e}")
        return b""


def get_logo_path():
    """Dark logo for light theme, white logo for dark theme."""
    try:
        is_dark = st.context.theme.type == "dark"
    except Exception:
        is_dark = False
    return IMG_DIR / ("inverseLogo.png" if is_dark else "Logo.png")


# ---------------- Header / Logo ----------------
logo_path = get_logo_path()
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if logo_path.exists():
        st.image(str(logo_path), width="stretch")
    else:
        st.markdown("<h1 style='text-align:center;'>LegalEase</h1>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>AI Legal Document Generator</h2>",
            unsafe_allow_html=True)

# ---------------- Inputs ----------------
document_type = st.text_input("Document Type (Ex: Agreement, Contract, NDA)")
parties = st.text_area("Parties Involved")
terms = st.text_area("Terms & Conditions (Use semicolons for bullet points)")
dates = st.text_input("Effective Date")

if st.button("Generate Document"):
    if not all(v.strip() for v in (document_type, parties, terms, dates)):
        st.warning("Please fill in all four fields.")
    else:
        with st.spinner("Drafting your document..."):
            try:
                response = requests.post(
                    f"{API_URL}/generate",
                    json={
                        "document_type": document_type,
                        "parties": parties,
                        "terms": terms,
                        "dates": dates,
                    },
                    timeout=180,
                )
                if response.status_code == 200:
                    st.session_state.generated_text = sanitize_text(response.json()["document"])
                    st.session_state.doc_type = document_type.strip()
                    st.session_state.terms = terms
                    st.session_state.show_edit = False
                    st.success("✅ Document Generated Successfully!")
                else:
                    try:
                        detail = response.json().get("detail", response.text)
                    except ValueError:
                        detail = response.text
                    st.error(f"Backend error ({response.status_code}): {detail}")
            except requests.exceptions.ConnectionError:
                st.error(f"Cannot reach the backend at {API_URL}. Is uvicorn running?")
            except requests.exceptions.Timeout:
                st.error("The request timed out. Please try again.")

# ---------------- Output ----------------
if st.session_state.generated_text:
    text = st.session_state.generated_text
    doc_type = st.session_state.doc_type or "Legal Document"

    styled_html = format_html_preview(text)
    st.markdown(
        "<div style='background:#0f172a;color:#cbd5e1;padding:18px 22px;"
        "border-radius:10px;border:1px solid #1e293b;max-height:380px;"
        f"overflow-y:auto;font-size:0.95rem;'>{styled_html}</div>",
        unsafe_allow_html=True,
    )

    st.button("✏️ Click to Edit Document", on_click=toggle_edit)
    if st.session_state.show_edit:
        st.text_area("Edit Document Below:", key="edit_area", height=300)
        st.caption("Press Ctrl+Enter to apply your changes.")

    file_base = re.sub(r"[^a-z0-9]+", "_", doc_type.lower()).strip("_") or "document"

    st.download_button(
        "📄 Download as .TXT",
        data=text,
        file_name=f"{file_base}.txt",
        mime="text/plain",
    )
    st.download_button(
        "📝 Download as .DOCX",
        data=safe_export(format_docx, text, doc_type, st.session_state.terms),
        file_name=f"{file_base}.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
    st.download_button(
        "📕 Download as .PDF",
        data=safe_export(format_pdf, text, doc_type, st.session_state.terms),
        file_name=f"{file_base}.pdf",
        mime="application/pdf",
    )
else:
    st.info("Click 'Generate Document' to start")