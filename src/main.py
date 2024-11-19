from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient
from leaf_disease_detector.router import router
import uvicorn
import logging
from config.config import IMAGE_PATH

# Initialize logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Initialize the FastAPI app
app = FastAPI(
    title="Leaf Disease Detection API",
    description="API to predict leaf diseases and provide information about detected diseases.",
    version="1.0.0",
)

# Define CORS origins
origins = ["http://localhost", "http://127.0.0.1:3000"]  # Adjust based on your frontend

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router
app.include_router(router)

@app.on_event("startup")
def on_startup():
    """
    Tasks to run during application startup.
    Example: Make an internal API call to /predict for testing.
    """
    logger.info("Starting application...")
    # Use FastAPI's TestClient for internal testing
    client = TestClient(app)
    test_image_path = IMAGE_PATH
    
    try:
        # Simulate a file upload to the /predict endpoint
        with open(test_image_path, "rb") as image_file:
            response = client.post("/predict", files={"file": ("image.jpg", image_file, "image/jpeg")})
        
        if response.status_code == 200:
            logger.info(f"Startup Test: /predict response: {response.json()}")
        else:
            logger.error(f"Startup Test: /predict failed with status {response.status_code}: {response.json()}")
    except FileNotFoundError:
        logger.error(f"Startup Test: Test image not found at {test_image_path}")
    except Exception as e:
        logger.error(f"Startup Test: Unexpected error: {e}")
    
    logger.info("Startup tasks complete.")

@app.on_event("shutdown")
def on_shutdown():
    """
    Tasks to run during application shutdown.
    Example: Cleanup resources or close connections.
    """
    logger.info("Shutting down application...")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
