from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_invalid_endpoint_404():
    response = client.get("/unknownpath")
    assert response.status_code == 404
