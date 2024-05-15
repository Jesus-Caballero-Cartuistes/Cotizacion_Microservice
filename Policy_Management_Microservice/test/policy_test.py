from Policy_Management_Microservice.src.Quotation import CarQuotation, MotorcycleQuotation, LifeQuotation
from Policy_Management_Microservice.src.QuotationMethods import MotorcycleQuotationMethods, CarQuotationMethods, LifeQuotationMethods
from Policy_Management_Microservice.policy_service import mongoDB
from main import app
from datetime import datetime, timedelta
from fastapi import FastAPI
from httpx import AsyncClient
import pytest
from fastapi.testclient import TestClient
import os
import sys
from fastapi import HTTPException
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..')))

# Importa tus definiciones de política y el enrutador aquí


@pytest.fixture
def test_client():
    return TestClient(app)


def test_create_motorcycle_policy(test_client):
    """
    Prueba la creación de una póliza de motocicleta.
    """
    moto_data = {
        "identification_type": "DNI",
        "identification": 12345678,
        "first_name": "John",
        "last_name": "Doe",
        "displacement": 150.0
    }
    response = test_client.post(
        "/policy/create_motorcycle_policy/", json=moto_data)
    assert response.status_code == 200
    policy = response.json()
    assert "identification" in policy
    assert policy["cost"] == 308500
    assert policy["start_date"] == datetime.now().strftime('%Y-%m-%d')
    assert policy["end_date"] == (datetime.now() + timedelta(days=365)).strftime(
        '%Y-%m-%d')


def test_create_car_policy(test_client):
    """
    Prueba la creación de una póliza de automóvil.
    """
    car_data = {
        "identification_type": "DNI",
        "identification": 12345678,
        "first_name": "John",
        "last_name": "Doe",
        "reference": "ABC123",
        "model": "Toyota",
        "year": 2022,
        "status": "Active",
        "usage": "Personal"
    }
    response = test_client.post("/policy/create_car_policy/", json=car_data)
    assert response.status_code == 200
    policy = response.json()
    assert "identification" in policy
    assert policy["cost"] == 0
    assert policy["start_date"] == datetime.now().strftime('%Y-%m-%d')
    assert policy["end_date"] == (datetime.now() + timedelta(days=365)).strftime(
        '%Y-%m-%d')


def test_create_life_policy(test_client):
    """
    Prueba la creación de una póliza de vida.
    """
    life_data = {
        "identification_type": "DNI",
        "identification": 12345678,
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "benefits": {"coverage": 100000, "duration": 20}
    }
    response = test_client.post("/policy/create_life_policy/", json=life_data)
    assert response.status_code == 200
    policy = response.json()
    assert "identification" in policy
    assert policy["cost"] == 50000
    assert policy["start_date"] == datetime.now().strftime('%Y-%m-%d')
    assert policy["end_date"] == (datetime.now() + timedelta(days=365)).strftime(
        '%Y-%m-%d')
