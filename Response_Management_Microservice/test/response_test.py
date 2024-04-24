
import os
import sys

from fastapi import HTTPException
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..')))
from main import app
from fastapi.testclient import TestClient
from unittest.mock import Mock
import pytest
from Response_Management_Microservice.response_service import *
from Response_Management_Microservice.src.MongoDB import MongoDB
from Response_Management_Microservice.src.Response import Response


client = TestClient(app)

# Test para crear una respuesta

def test_create_response():
    mongoDB.collection = mongoDB.db['Test']
    response = client.post(
        "/response/responses/",
        json={
            "id": 1,
            "status": "pending",
            "claim_description": "Faulty product received",
            "manager_response": "Investigating the issue"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Respuesta publicada correctamente"}

# Test para obtener una respuesta por su ID


def test_get_response():
    # Primero, creamos una respuesta de ejemplo
    mongoDB.collection = mongoDB.db['Test']
    create_response = client.post(
        "/response/responses/",
        json={
            "id": 1,
            "status": "pending",
            "claim_description": "Faulty product received",
            "manager_response": "Investigating the issue"
        }
    )
    assert create_response.status_code == 200
    # Luego, intentamos obtener la respuesta recién creada
    response = client.get("/response/responses/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["claim_description"] == "Faulty product received"

# Test para manejar el caso cuando la respuesta no existe


def test_get_nonexistent_response():
    mongoDB.collection = mongoDB.db['Test']
    response = client.get("/response/responses/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Response not found"
