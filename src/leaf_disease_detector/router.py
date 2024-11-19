from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from leaf_disease_detector.dependencies import get_disease_details
from leaf_disease_detector.schemas import DiseasePredictionRequest, PredictionResponse
from config.db import get_db_session
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
