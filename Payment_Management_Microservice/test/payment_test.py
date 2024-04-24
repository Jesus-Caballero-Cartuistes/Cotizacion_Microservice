from fastapi import HTTPException
import pytest
from fastapi.testclient import TestClient
import os
import sys
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..')))
from Payment_Management_Microservice.payment_service import process_payment
from main import app
from Payment_Management_Microservice.src.PaymentRequest import PaymentRequest
from Payment_Management_Microservice.payment_service import mongoDB


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def cleanup_database():
    yield
    # Limpiar la colección de reclamaciones después de cada prueba
    mongoDB.db['Test'].delete_many({})

def test_valid_payment(client):
    payment_data = {
        "quote_id": "12345",
        "billing_info": {"name": "John Doe", "address": "123 Main St"},
        "payment_method": "credit_card",
        "amount": 100.0,
        "currency": "USD",
        "payment_date": "2024-04-24T12:00:00",
        "payment_status": "pending"
    }
    mongoDB.collection = mongoDB.db['Test']
    response = client.post("/payment/payments/", json=payment_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Pago procesado correctamente"}


def test_invalid_payment_amount(client):
    payment_data = {
        "quote_id": "12345",
        "billing_info": {"name": "John Doe", "address": "123 Main St"},
        "payment_method": "credit_card",
        "amount": -100.0,  # Invalid negative amount
        "currency": "USD",
        "payment_date": "2024-04-24T12:00:00",
        "payment_status": "pending"
    }
    mongoDB.collection = mongoDB.db['Test']
    response = client.post("/payment/payments/", json=payment_data)
    assert response.status_code == 400

def test_integration_payment_processing_successful():
    payment_data = PaymentRequest(
        quote_id="12345",
        billing_info={"name": "John Doe", "address": "123 Main St"},
        payment_method="credit_card",
        amount=100.0,
        currency="USD",
        payment_date="2024-04-24T12:00:00",
        payment_status="pending"
    )
    response = process_payment(payment_data)
    assert response == {"message": "Pago procesado correctamente"}


def test_integration_payment_processing_failed():
    payment_data = PaymentRequest(
        quote_id="12345",
        billing_info={"name": "John Doe", "address": "123 Main St"},
        payment_method="credit_card",
        amount=-1000.0,  # Amount causing failure
        currency="USD",
        payment_date="2024-04-24T12:00:00",
        payment_status="pending"
    )
    with pytest.raises(HTTPException):
        process_payment(payment_data)
