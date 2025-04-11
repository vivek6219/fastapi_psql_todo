from fastapi.testclient import TestClient
from main import app


data = {"id" : 1,
        "title": "do stuff",
        "completed": False}

def test_get_todos():
    with TestClient(app) as client:
        response = client.get("/todos")
        assert response.status_code == 200

def test_enter_todos():
    with TestClient(app) as client:
        response = client.post("/enter_todo", json=data)
        assert response.status_code == 201 or response.status_code == 200