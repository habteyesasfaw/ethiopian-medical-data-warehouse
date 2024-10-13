# test_main.py
from fastapi.testclient import TestClient
from fastapi_app.main import app

client = TestClient(app)
def test_create_detection():
    response = client.post("/detections/", json={
        "image_url": "http://example.com/image.jpg",
        "object_class": "car",
        "confidence_score": 0.98,
        "bounding_box": "50,50,200,200"
    })
    assert response.status_code == 200
    assert response.json()["object_class"] == "car"

def test_read_detection():
    response = client.get("/detections/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
