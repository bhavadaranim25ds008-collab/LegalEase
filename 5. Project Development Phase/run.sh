#!/bin/bash
# Starts the FastAPI backend and Streamlit frontend together.
# Usage: bash run.sh

uvicorn legalEaseAPI.main:app --reload --port 8000 &
BACKEND_PID=$!

streamlit run frontend/app.py

kill $BACKEND_PID
