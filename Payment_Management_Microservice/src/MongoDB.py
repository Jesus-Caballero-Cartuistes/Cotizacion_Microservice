from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
from abc import ABC, abstractmethod
from typing import Dict

from Payment_Management_Microservice.src.Database import Database


class MongoDB(Database):
    def __init__(self):
        self.client = None
        self.uri = None
        self.db = None
        self.collection = None
        self.connect()

    def connect(self):
        self.uri = "mongodb+srv://nuco112233:nuco123456@cluster0.hm6ek1d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        self.db = self.client['Financial_Records']
        self.collection = self.db['Payments']
        print("¡Conexión exitosa [Payment DB]!")

    def save_payment_record(self, payment_data: dict) -> None:
        self.collection.insert_one(payment_data)
