#
"""

"""
import pytest
from flask_app.flask_app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Powerlifting Coefficient Calculator" in response.data

def test_api_calculate_success(client):
    response = client.post("/api/v1/calculate", json={
        "body_weight": 80,
        "total_lifted": 600,
        "unit": "kg",
        "gender": "male",
        "competition": "CLPL",
        "age": 30
    })
    assert response.status_code == 200
    assert "old_wilks" in response.json

def test_api_calculate_missing_field(client):
    response = client.post("/api/v1/calculate", json={})
    assert response.status_code == 400

if __name__ == "__main__":
    pytest.main()
