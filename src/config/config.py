import os
from dotenv import load_dotenv

load_dotenv()

DISEASE_CLASSES = {
    "Apple Scab Leaf": 0,
    "Apple leaf": 1,
    "Apple rust leaf": 2,
    "Bell_pepper leaf": 3,
    "Bell_pepper leaf spot": 4,
    "Blueberry leaf": 5,
    "Cherry leaf": 6,
    "Corn Gray leaf spot": 7,
    "Corn leaf blight": 8,
    "Corn rust leaf": 9,
    "Peach leaf": 10,
    "Potato leaf": 11,
    "Potato leaf early blight": 12,
    "Potato leaf late blight": 13,
    "Raspberry leaf": 14,
    "Soyabean leaf": 15,
    "Squash Powdery mildew leaf": 16,
    "Strawberry leaf": 17,
    "Tomato Early blight leaf": 18,
    "Tomato Septoria leaf spot": 19,
    "Tomato leaf": 20,
    "Tomato leaf bacterial spot": 21,
    "Tomato leaf late blight": 22,
    "Tomato leaf mosaic virus": 23,
    "Tomato leaf yellow virus": 24,
    "Tomato mold leaf": 25,
    "Tomato two spotted spider mites leaf": 26,
    "grape leaf": 27,
    "grape leaf black rot": 28
}

MODEL_PATH = os.getenv('MODEL_PATH')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
TABLE_NAME = os.getenv('TABLE_NAME')
IMAGE_PATH = os.getenv('IMAGE_PATH')