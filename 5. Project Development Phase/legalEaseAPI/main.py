"""
legalEaseAPI/main.py

FastAPI application entrypoint. Run with:
    uvicorn legalEaseAPI.main:app --reload
from the project root.
"""

from fastapi import FastAPI

from legalEaseAPI.routes import router

app = FastAPI(title="LegalEase - AI Legal Document Generator")

# Include API routes
app.include_router(router)


# Root endpoint (health check)
@app.get("/")
def home():
    return {"message": "Welcome to LegalEase AI Legal Document Generator API"}


# Run FastAPI if executed directly
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
