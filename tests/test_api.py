"""API tests with FastAPI TestClient."""
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_latest_returns_json():
    r = client.get("/latest")
    assert r.status_code == 200
    assert "markdown" in r.json()


def test_push_updates_latest():
    r = client.post("/push", json={"markdown": "# hello"})
    assert r.status_code == 200
    assert client.get("/latest").json()["markdown"] == "# hello"
