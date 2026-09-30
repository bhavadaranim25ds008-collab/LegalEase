"""
frontend/utils.py

Core formatting utilities used by the Streamlit UI to turn raw
AI-generated text into clean, branded, downloadable documents.
"""

import io
import re

from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from fpdf import FPDF

from config import WEB_LOGO_PATH


def sanitize_text(text: str) -> str:
    """Removes special characters and typographic quotes for clean formatting."""
    replacements = {
        "\u2018": "'", "\u2019": "'",
        "\u201c": '"', "\u201d": '"',
        "\u2013": "-", "\u2014": "-",
        "\u2026": "...",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    # Collapse excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _split_terms(terms_block: str) -> list[str]:
    """Splits a semicolon-separated terms string into a clean list."""
    return [t.strip() for t in terms_block.split(";") if t.strip()]


def format_docx(text: str, doc_type: str) -> bytes:
    """
    Builds a formatted Word document: logo header, Times New Roman body,
    a terms table (if semicolon-separated terms are detected), and a footer.
    Returns the .docx file as bytes, ready for st.download_button.
    """
    document = Document()

    # Set default font
    style = document.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(11)

    # Logo header
    try:
        document.add_picture(WEB_LOGO_PATH, width=Inches(1.5))
        document.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    except Exception:
        pass  # logo optional if file missing

    # Title
    title = document.add_heading(doc_type or "Legal Document", level=1)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Body — split on double newlines into paragraphs
    for block in sanitize_text(text).split("\n\n"):
        block = block.strip()
        if not block:
            continue
        if block.startswith("#"):
            document.add_heading(block.lstrip("#").strip(), level=2)
        else:
            document.add_paragraph(block)

    document.add_paragraph()  # spacer
    document.add_paragraph("─" * 40).alignment = WD_ALIGN_PARAGRAPH.CENTER

    footer_p = document.add_paragraph("LegalEase Inc. | contact@legalease.com | All Rights Reserved.")
    footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    buffer = io.BytesIO()
    document.save(buffer)
    buffer.seek(0)
    return buffer.getvalue()


class _BrandedPDF(FPDF):
    def header(self):
        try:
            self.image(WEB_LOGO_PATH, x=90, y=8, w=30)
            self.ln(20)
        except Exception:
            self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, "LegalEase Inc. | contact@legalease.com | All Rights Reserved.", align="C")


def format_pdf(text: str, doc_type: str) -> bytes:
    """
    Builds a branded PDF with a centered logo header and footer on every
    page. Returns the PDF as bytes, ready for st.download_button.
    """
    pdf = _BrandedPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.multi_cell(0, 10, doc_type or "Legal Document", align="C")
    pdf.ln(4)

    pdf.set_font("Helvetica", size=11)
    for block in sanitize_text(text).split("\n\n"):
        block = block.strip()
        if not block:
            continue
        if block.startswith("#"):
            pdf.set_font("Helvetica", "B", 13)
            pdf.multi_cell(0, 8, block.lstrip("#").strip())
            pdf.set_font("Helvetica", size=11)
        else:
            pdf.multi_cell(0, 7, block)
        pdf.ln(2)

    # fpdf2 returns a bytearray from output(dest="S")
    return bytes(pdf.output(dest="S"))


def format_html_preview(text: str) -> str:
    """Converts generated text into stylized HTML blocks for inline display."""
    clean = sanitize_text(text)
    html_blocks = []
    for block in clean.split("\n\n"):
        block = block.strip()
        if not block:
            continue
        if block.startswith("#"):
            html_blocks.append(f"<h3 style='color:#e8e8e8;'>{block.lstrip('#').strip()}</h3>")
        else:
            block_html = block.replace("\n", "<br>")
            html_blocks.append(f"<p style='color:#d0d0d0; line-height:1.6;'>{block_html}</p>")
    return "".join(html_blocks)
