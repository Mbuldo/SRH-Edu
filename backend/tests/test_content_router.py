from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_faqs_endpoint():
    response = client.get("/api/content/faqs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
