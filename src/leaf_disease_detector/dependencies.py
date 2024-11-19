from sqlalchemy.orm import Session
from models import Disease  # Assuming the model for the disease is in `models.py`

def get_disease_details(disease_name: str, db: Session):
    """
    Fetch the disease details from the database based on the disease name.
    """
    disease = db.query(Disease).filter(Disease.DiseaseName == disease_name).first()

    if disease is None:
        return None  # Disease not found in the database

    # Return the disease details, such as symptoms, treatment, etc.
    return {
        "disease_name": disease.DiseaseName,
        "symptoms": disease.Symptoms,
        "prevention": disease.Prevention,
        "treatment": disease.Treatment
    }
