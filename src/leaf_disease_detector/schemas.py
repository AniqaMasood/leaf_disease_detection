from pydantic import BaseModel
from typing import Optional, List

# Request model to accept disease name from the client
class DiseasePredictionRequest(BaseModel):
    disease_name: str  # The disease name provided by the user in the request

# Response model for the disease details
class DiseaseDetails(BaseModel):
    disease_name: str
    symptoms: str
    prevention: str
    treatment: str

class PredictionResponse(BaseModel):
    diseases: List[DiseaseDetails]

    class Config:
        orm_mode = True  # Tells Pydantic to treat ORM models as dictionaries for easy serialization
