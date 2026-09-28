"""Central configuration for LegalEase."""
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
# gemini-1.5-pro has been shut down by Google, so the default is a current model.
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-3.5-flash-lite")

API_URL = os.getenv("API_URL", "http://localhost:8000")

LOGO_PATH = BASE_DIR / "Image" / "Logo.png"
WEB_LOGO_PATH = BASE_DIR / "Image" / "inverseLogo.png"
FOOTER_TEXT = "LegalEase Inc. | contact@legalease.com | All Rights Reserved."