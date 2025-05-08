from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from typing import Dict, Any, List
import io
import time
import logging
import numpy as np
from PIL import Image
from app.core.model import predict_image

router = APIRouter(prefix="/api", tags=["classification"])
logger = logging.getLogger(__name__)

@router.post("/classify", response_model=Dict[str, Any])
async def classify_image(file: UploadFile = File(...)):
    """
    Classify an uploaded image using MobileNet model
    
    Returns:
        Dict with classification results
    """
    start_time = time.time()
    
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    try:
        # Read image file
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        # Get predictions
        predictions = predict_image(image)
        
        # Get total processing time
        processing_time = round(time.time() - start_time, 3)
        
        # Return prediction response
        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "predictions": predictions,
            "processing_time": processing_time
        }
    
    except Exception as e:
        logger.error(f"Error classifying image: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")