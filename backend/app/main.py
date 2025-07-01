from fastapi import FastAPI

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok", "message": "Service is running"} # Health check endpoint