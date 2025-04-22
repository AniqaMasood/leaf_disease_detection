from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from sqlalchemy.orm import Session
from leaf_disease_detector.dependencies import get_disease_details
from leaf_disease_detector.leaf_disease_detection import LeafDiseaseDetection
from leaf_disease_detector.schemas import DiseasePredictionRequest, PredictionResponse
from config.db import get_db_session
import os

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
def predict_disease(request: DiseasePredictionRequest, db: Session = Depends(get_db_session)):
    """
    Endpoint to fetch disease details based on the provided disease name.
    """
    disease_name = request.disease_name  # The disease name sent in the request
    # Fetch the disease details from the database
    disease_info = get_disease_details(disease_name, db)

    if not disease_info:
        raise HTTPException(status_code=404, detail=f"Disease details not found for {disease_name}")

    return disease_info

@router.post("/predict_image", response_model=PredictionResponse)
async def predict_image(image: UploadFile = File(...), db: Session = Depends(get_db_session)):
    """
    Endpoint to predict disease based on the provided image.
    """
    detector = LeafDiseaseDetection()

    # Save the uploaded image to a directory
    image_path = f"input_image/{image.filename}"
    with open(image_path, "wb") as buffer:
        buffer.write(await image.read())

    # Predict the disease from the image
    disease_name = detector.predict(image_path)

    # Fetch the disease details from the database
    disease_info = get_disease_details(disease_name, db)

    if not disease_info:
        raise HTTPException(status_code=404, detail=f"Disease details not found for {disease_name}")

    return {'diseases' : disease_info}
