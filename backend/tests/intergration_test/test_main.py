from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)


def test_healthcheck():
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "message": "Service is running"
    }