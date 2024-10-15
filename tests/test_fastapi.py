from fastapi.testclient import TestClient
from fastapi_app.main import app  # Ensure this path is correct

client = TestClient(app)

def test_create_object_detection():
    data = {
        "xmin_value": 0.1,
        "ymin": 0.2,
        "xmax_value": 0.9,
        "ymax": 0.8,
        "confidence": 0.99,
        "class_value": 1,
        "name": "string",
        "image": "string"
    }
    # response = client.post("/object-detection/", json=data)
    # assert response.status_code == 200
    # assert response.json()["name"] == "string"

# def test_get_object_detections():
#     response = client.get("/object-detection/")
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)
