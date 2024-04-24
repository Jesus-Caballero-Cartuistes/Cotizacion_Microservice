from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from main import app
import os
import sys
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..')))
import pytest
from datetime import datetime
from fastapi import HTTPException
from Claims_Management_Microservice.src.ClaimControllerImpl import ClaimControllerImpl
from Claims_Management_Microservice.src.Claim import Claim
from Claims_Management_Microservice.src.MongoDB import MongoDB
from Claims_Management_Microservice.claim_service import mongoDB

@pytest.fixture
def mock_mongodb():
    class MockDatabase:
        def __init__(self):
            self.claims = {}

        def save_claim(self, claim_data):
            claim_id = len(self.claims) + 1
            claim_data['id'] = claim_id
            self.claims[claim_id] = claim_data
            return claim_id

        def get_claim(self, claim_id):
            return self.claims.get(claim_id)

    return MockDatabase()


def test_create_claim(mock_mongodb):
    claim_data = {
        "status": "pending",
        "details": "Lorem ipsum dolor sit amet",
        "date": datetime.now()
    }
    claim_controller = ClaimControllerImpl(mock_mongodb)
    claim_id = claim_controller.create_claim(claim_data)
    assert claim_id == 1  # Assuming it's the first claim


def test_get_claim(mock_mongodb):
    mock_mongodb.claims = {
        1: {
            "id": 1,
            "status": "pending",
            "details": "Lorem ipsum dolor sit amet",
            "date": datetime.now()
        }
    }
    claim_controller = ClaimControllerImpl(mock_mongodb)
    claim = claim_controller.get_claim(1)
    assert claim["id"] == 1
    assert claim["status"] == "pending"


def test_get_claim_not_found(mock_mongodb):
    claim_controller = ClaimControllerImpl(mock_mongodb)
    claim = claim_controller.get_claim(2)
    assert claim is None


client = TestClient(app)


@pytest.fixture
def claim_data():
    return {
        "id": 1,
        "status": "pending",
        "details": "This is a test claim",
        "date": "2024-04-24T01:52:39.012000"
    }


@pytest.fixture(autouse=True)
def cleanup_database():
    yield
    # Limpiar la colección de reclamaciones después de cada prueba
    mongoDB.db['Test'].delete_many({})


def test_create_claim(claim_data):
    mongoDB.collection = mongoDB.db['Test']
    response = client.post("/claim/claims/", json=claim_data)
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["status"] == claim_data["status"]
    assert response.json()["details"] == claim_data["details"]


def test_get_claim(claim_data):
    mongoDB.collection = mongoDB.db['Test']
    response = client.post("/claim/claims/", json=claim_data)
    assert response.status_code == 200
    response = client.get("/claim/claims/1")
    assert response.status_code == 200
    assert response.json()["id"] == claim_data["id"]
    assert response.json()["status"] == claim_data["status"]
    assert response.json()["details"] == claim_data["details"]
    assert response.json()["date"] == claim_data["date"]


def test_get_nonexistent_claim():
    mongoDB.collection = mongoDB.db['Test']
    response = client.get("/claim/claims/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Claim not found"
