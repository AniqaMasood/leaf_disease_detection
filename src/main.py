from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from leaf_disease_detector.router import router  # Adjusted import path
from config.db import get_db_session
from config.config import IMAGE_PATH
from sqlalchemy.ext.asyncio import AsyncSession
from sockets import manager  # Adjusted import path assuming manager is defined in __init__.py or another file in leaf_disease_detector
import asyncio

# Initialize the FastAPI app
app = FastAPI()

# Define CORS origins
origins = ["*"]  # Modify this as needed

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router
app.include_router(router)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Message text was: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# Run database initialization on startup
@app.on_event("startup")
async def on_startup():
    # Perform any initialization (e.g., loading model, initializing DB)
    pass  # Call the function to detect leaf disease

@app.on_event("shutdown")
async def on_shutdown():
    # Perform any cleanup (e.g., releasing resources, closing DB connections)
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)