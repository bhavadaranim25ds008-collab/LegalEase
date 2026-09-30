"""
ai_core/gemini_generator.py

Wraps the Google Generative AI SDK to turn structured user input
(document_type, parties, terms, dates) into a formatted legal document
using the gemini-1.5-pro model.
"""

import google.generativeai as genai

from config import GEMINI_API_KEY, GEMINI_MODEL_NAME

# Configure the SDK once at import time
genai.configure(api_key=GEMINI_API_KEY)


class GeminiDocumentGenerator:
    """Generates legal document text from structured inputs via Gemini."""

    def __init__(self, model_name: str = GEMINI_MODEL_NAME):
        self.model = genai.GenerativeModel(model_name)

    def _build_prompt(self, document_type: str, parties: str, terms: str, dates: str) -> str:
        return (
            f"Generate a comprehensive legal document titled '{document_type}'\n"
            f"Involved parties: {parties}\n"
            f"Effective Date: {dates}\n"
            f"Terms and conditions: {terms}\n"
            f"Ensure formal legal structure with multiple sections and legal clauses. "
            f"Use clear numbered headings (1. Services, 2. Term and Termination, etc.) "
            f"and standard legal boilerplate (confidentiality, governing law, signatures) "
            f"where appropriate."
        )

    def generate_document(self, document_type: str, parties: str, terms: str, dates: str) -> str:
        """
        Calls Gemini with a structured prompt and returns the generated
        legal document as plain text.
        """
        prompt = self._build_prompt(document_type, parties, terms, dates)
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as exc:  # noqa: BLE001
            # Surface a readable error rather than an unhandled exception
            raise RuntimeError(f"Gemini generation failed: {exc}") from exc
