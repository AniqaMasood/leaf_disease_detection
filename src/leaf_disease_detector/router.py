from fastapi import APIRouter, HTTPException, Depends, File, UploadFile
from sqlalchemy.orm import Session
from leaf_disease_detector.dependencies import get_disease_details
from leaf_disease_detector.leaf_disease_detection import LeafDiseaseDetection
from config.db import get_db_session
import shutil
from pathlib import Path

router = APIRouter()
UPLOAD_DIR = Path("./uploads")  # Directory to store uploaded files
UPLOAD_DIR.mkdir(exist_ok=True)

# Initialize the disease detection model
detector = LeafDiseaseDetection()

@router.post("/predict", response_model=dict)
def predict_disease(file: UploadFile = File(...), db: Session = Depends(get_db_session)):
    """
    Endpoint to predict disease from an uploaded image and fetch disease details.
    """
    # Save the uploaded file
    file_path = UPLOAD_DIR / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run the detection model
    predicted_diseases = detector.predict(str(file_path))
    
    if not predicted_diseases:
        raise HTTPException(status_code=404, detail="No disease detected from the image.")

    disease_details = []
    for disease_name in predicted_diseases:
        # Fetch disease details from the database
        disease_info = get_disease_details(disease_name, db)
        if disease_info:
            disease_details.append(disease_info)

    if not disease_details:
        raise HTTPException(status_code=404, detail="No matching disease details found.")

    return {"detected_diseases": disease_details}
