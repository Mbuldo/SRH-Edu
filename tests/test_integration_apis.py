from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_login_success():
    resp = client.post("/api/auth/login", data={"username": "admin", "password": "admin123"})
    assert resp.status_code == 200
    data = resp.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_failure():
    resp = client.post("/api/auth/login", data={"username": "admin", "password": "wrongpass"})
    assert resp.status_code == 401

def test_get_me():
    login = client.post("/api/auth/login", data={"username": "admin", "password": "admin123"})
    token = login.json().get("access_token")
    assert token
    me = client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert me.status_code == 200
    assert me.json()["username"] == "admin"

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_quiz_crud():
    qdata = {
        "question": "Which of these is an effective method of STI prevention?",
        "options": ["Using birth control pills", "Using condoms consistently", "Washing after sex", "Taking vitamins"],
        "correct_answer": 1,
        "explanation": "Using condoms consistently."
    }
    # Create
    c = client.post("/api/quiz/questions", json=qdata)
    assert c.status_code == 200
    qid = c.json()["id"]
    # List
    l = client.get("/api/quiz/questions")
    assert l.status_code == 200
    # Get
    g = client.get(f"/api/quiz/questions")
    assert g.status_code == 200
    # Update
    qdata["question"] = "Capital of Germany?"
    qdata["correct_answer"] = 1
    qdata["explanation"] = "Berlin is the capital of Germany."
    u = client.put(f"/api/quiz/questions/{qid}", json=qdata)
    assert u.status_code == 200
    # Delete
    d = client.delete(f"/api/quiz/questions/{qid}")
    assert d.status_code == 200

def test_quiz_submit():
    allq = client.get("/api/quiz/questions").json()
    if not allq:
        return
    answer = {str(q['id']): q['correct_answer'] for q in allq}
    resp = client.post("/api/quiz/submit", json=answer)
    assert resp.status_code == 200
    assert "score" in resp.json()

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_clinic_crud():
    clinic_data = {
        "name": "Westlands Health Center",
        "address": "WESTLANDS - Waiyaki Way",
        "contact": "020 4452560",
        "operating_hours": "24/7",
        "services": ["testing", "treatment"],
        "is_active": True
    }
    # Create
    resp = client.post("/api/clinics/", json=clinic_data)
    assert resp.status_code == 200
    cid = resp.json()["id"]

    # List
    resp2 = client.get("/api/clinics/")
    assert resp2.status_code == 200

    # Get one
    resp3 = client.get(f"/api/clinics/{cid}")
    assert resp3.status_code == 200

    # Update
    clinic_data["area"] = "Area52"
    up = client.put(f"/api/clinics/{cid}", json=clinic_data)
    assert up.status_code == 200

    # Delete (deactivate)
    d = client.delete(f"/api/clinics/{cid}")
    assert d.status_code == 200

# tests/test_integration_symptoms.py
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_symptom_crud():
    symp_data = {
        "name": "Headache",
        "description": "pain in head",
        "related_conditions": ["fever"],
        "severity_level": 2,
        "seek_care": False
    }
    # Create
    resp = client.post("/api/symptoms/", json=symp_data)
    assert resp.status_code == 200
    sid = resp.json()["id"]
    # List
    resp2 = client.get("/api/symptoms/")
    assert resp2.status_code == 200
    # Get one
    resp3 = client.get(f"/api/symptoms/{sid}")
    assert resp3.status_code == 200
    # Check
    check = client.post("/api/symptoms/check", json=["Headache"])
    assert check.status_code == 200
