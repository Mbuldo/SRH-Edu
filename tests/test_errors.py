# tests/test_errors.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_invalid_endpoint_404():
    response = client.get("/unknownpath")
    assert response.status_code == 404
