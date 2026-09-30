"""
config.py
Central place for environment variables and shared paths used across
the FastAPI backend and the Streamlit frontend.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load variables from .env into the environment
load_dotenv()

# --- API keys -----------------------------------------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# --- Model settings -------------------------------------------------------
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-1.5-pro")

# --- Paths ------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "Image"

WEB_LOGO_PATH = str(IMAGE_DIR / "Logo.png")
INVERSE_LOGO_PATH = str(IMAGE_DIR / "inverseLogo.png")

# --- Backend URL (used by the Streamlit frontend) ------------------------
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

if not GEMINI_API_KEY:
    # Don't crash on import (e.g. during testing) — just warn.
    print("[config] WARNING: GEMINI_API_KEY is not set. Add it to your .env file.")
