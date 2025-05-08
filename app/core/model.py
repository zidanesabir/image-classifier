import tensorflow as tf
from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input, decode_predictions
import numpy as np
from PIL import Image
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Global model variable
model = None

def load_model():
    """
    Load the MobileNet model
    """
    global model
    try:
        # Load pre-trained MobileNet model
        model = MobileNet(weights='imagenet')
        logger.info("MobileNet model loaded successfully")
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        raise RuntimeError(f"Failed to load MobileNet model: {str(e)}")

def preprocess_image(image):
    """
    Preprocess image for MobileNet
    
    Args:
        image: PIL Image
    
    Returns:
        Preprocessed image as numpy array
    """
    # Resize to MobileNet input size
    image = image.resize((224, 224))
    
    # Convert to array and preprocess
    img_array = np.array(image)
    
    # Handle grayscale images by converting to RGB
    if len(img_array.shape) == 2:
        img_array = np.stack((img_array,) * 3, axis=-1)
    
    # Ensure we have 3 channels (RGB)
    if img_array.shape[-1] == 4:
        # Convert RGBA to RGB
        img_array = img_array[..., :3]
    
    # Expand dimensions and preprocess
    img_array = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array)

def predict_image(image):
    """
    Make predictions on an image
    
    Args:
        image: PIL Image
    
    Returns:
        List of top predictions with classes and probabilities
    """
    global model
    
    if model is None:
        load_model()
    
    try:
        # Preprocess the image
        processed_image = preprocess_image(image)
        
        # Make prediction
        predictions = model.predict(processed_image)
        
        # Decode and format predictions
        decoded = decode_predictions(predictions, top=5)[0]
        
        # Format results
        results = [
            {
                "class_id": imagenet_id,  # Fixed: using imagenet_id from decoded predictions
                "class_name": class_name,
                "probability": float(score)
            }
            for imagenet_id, class_name, score in decoded  # Fixed: unpacking all three values
        ]
        
        return results
    
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise RuntimeError(f"Failed to make prediction: {str(e)}")