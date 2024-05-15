import os
import sys
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..')))
from bson import ObjectId
from pymongo.database import Database
from pymongo.collection import Collection
from pymongo.server_api import ServerApi
from pymongo import MongoClient
from fastapi.testclient import TestClient
import pytest
from Authentication_Microservice.src.MongoDB import MongoDB
from VehicleAuthenticationRequest import AuthenticationRequest
from main import app



# Configuración de MongoDB Atlas para pruebas
TEST_CONNECTION_STRING = "mongodb+srv://nuco112233:nuco123456@cluster0.hm6ek1d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
TEST_DB_NAME = "Test"
TEST_COLLECTION_NAME = "Users"

# Fixture para configurar una base de datos de prueba y obtener una instancia de MongoDB


@pytest.fixture
def test_mongodb():
    client = MongoClient(TEST_CONNECTION_STRING, server_api=ServerApi('1'))
    db = client[TEST_DB_NAME]
    mongodb_instance = MongoDB()  # Crear una instancia de MongoDB
    mongodb_instance.db = db  # Establecer la base de datos en la instancia
    yield mongodb_instance
    client.drop_database(TEST_DB_NAME)

# Prueba unitaria para la autenticación del usuario en MongoDB


def test_authenticate_user(test_mongodb):
    # Insertar un usuario de prueba en la base de datos
    collection = test_mongodb.db[TEST_COLLECTION_NAME]
    collection.insert_one({
        "id_number": 1234567890,
        "name": "John",
        "last_name": "Doe",
        "expiration_date": "31-12-2024"
    })

    # Crear una solicitud de autenticación con datos correctos
    auth_request = AuthenticationRequest(
        id_number=1234567890, name="John", last_name="Doe", expiration_date="31-12-2024")
    assert test_mongodb.authenticate_user(
        auth_request.id_number, auth_request.name, auth_request.last_name, auth_request.expiration_date) == True

    # Crear una solicitud de autenticación con datos incorrectos
    auth_request = AuthenticationRequest(
        id_number=1234567890, name="Jane", last_name="Doe", expiration_date="31-12-2024")
    assert test_mongodb.authenticate_user(
        auth_request.id_number, auth_request.name, auth_request.last_name, auth_request.expiration_date) == False


# Prueba de integración para el endpoint de autenticación en FastAPI
client = TestClient(app)


def test_authentication_endpoint():
    # Caso de prueba con datos correctos
    response = client.post(
        "/auth/authenticate/",
        json={"id_number": 1234567890, "name": "John", "last_name": "Doe",
              "expiration_date": "31-12-2024"}
    )
    assert response.status_code == 200
    assert response.json() == {"authenticated": True}

    # Caso de prueba con datos incorrectos
    response = client.post(
        "/auth/authenticate/",
        json={"id_number": 1234567890, "name": "Doe", "last_name": "Doe",
              "expiration_date": "31-12-2024"}
    )
    assert response.status_code == 401
