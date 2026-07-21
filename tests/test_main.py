from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "DevOps API is running"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_sum_numbers():
    response = client.get("/sum/2/3")
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_sum_rejects_non_integer():
    response = client.get("/sum/dos/3")
    assert response.status_code == 422
