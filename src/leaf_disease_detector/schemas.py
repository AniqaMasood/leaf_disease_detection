from pydantic import BaseModel
from typing import Optional

# Request model to accept disease name from the client
class DiseasePredictionRequest(BaseModel):
    disease_name: str  # The disease name provided by the user in the request

# Response model for the disease details
class PredictionResponse(BaseModel):
    disease_name: str
    symptoms: str
    prevention: str
    treatment: str

    class Config:
        orm_mode = True  # Tells Pydantic to treat ORM models as dictionaries for easy serialization
