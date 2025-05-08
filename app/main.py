from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
import uvicorn
import os
import logging

from app.api import endpoints
from app.core import model

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Image Classifier",
    description="An AI-powered image classification service using MobileNet",
    version="1.0.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include API router
app.include_router(endpoints.router)

# Templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Render the main page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.on_event("startup")
async def startup_event():
    """Load ML model on startup"""
    logger.info("Loading MobileNet model...")
    model.load_model()
    logger.info("MobileNet model loaded successfully!")

if __name__ == "__main__":
    # For local development
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)