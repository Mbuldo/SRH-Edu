from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_faqs_endpoint():
    response = client.get("/faqs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_content_resources():
    response = client.get("/resources?category=education")
    assert response.status_code == 200
    data = response.json()
    assert "resources" in data or isinstance(data, list)
