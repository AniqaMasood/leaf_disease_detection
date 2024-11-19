from leaf_disease_detector.leaf_disease_detection import LeafDiseaseDetection
from leaf_disease_detector.router import predict_disease
from fastapi import Depends
from sqlalchemy.orm import Session
from config.db import get_db_session
from leaf_disease_detector.schemas import DiseasePredictionRequest

def main(image_path: str):
    # Initialize the disease detection model
    detector = LeafDiseaseDetection()
    
    # Predict the diseases from the image (assuming predict now returns a list of disease names)
    predicted_diseases = detector.predict(image_path)
    
    if predicted_diseases:
        # Get a database session
        db_session = get_db_session()
        
        try:
            # Loop through each detected disease and fetch details
            for disease_name in predicted_diseases:
                # Create a request object for each disease
                request = DiseasePredictionRequest(disease_name=disease_name)
                
                # Call the API endpoint to get disease details
                disease_details = predict_disease(request, db=db_session)
                
                # Print the details of each detected disease
                print(f"{disease_details}")
        finally:
            db_session.close()  # Ensure the session is closed after all processing
    else:
        print("No disease detected.")
