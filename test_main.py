from fastapi.testclient import TestClient
from main import app


def test_read():
    with TestClient(app) as client:
        response = client.get("/todos")
        assert response.status_code == 200
