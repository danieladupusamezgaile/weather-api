from fastapi import FastAPI
from app.core.config import get_settings

settings = get_settings() # load config from .env file using get_settings()

app = FastAPI( # initialize FastAPI app
    title="Weather API",
    description="A FastAPI app with PostgreSQL and external weather API",
    version="1.0"
)

@app.get("/") # test route /
def root():
    return {"message": "Hello World!"}