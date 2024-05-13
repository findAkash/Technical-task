from fastapi import FastAPI
import uvicorn
from config import Config

from api import router as api_router

app = FastAPI()

# Include the API router
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host=Config.HOST, port=Config.PORT) 