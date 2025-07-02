from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok", "message": "Service is running"} # Health check endpoint

from app.DB.session import engine
from app.DB.base import Base

Base.metadata.create_all(bind=engine)
