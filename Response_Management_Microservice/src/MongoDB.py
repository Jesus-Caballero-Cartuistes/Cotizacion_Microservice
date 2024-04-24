from pymongo.server_api import ServerApi
from pymongo import MongoClient
from abc import ABC, abstractmethod
from pymongo import MongoClient
from pymongo.collection import Collection
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

from Response_Management_Microservice.src.Database import Database
from Response_Management_Microservice.src.Response import Response


class MongoDB(Database):
    
    
    def __init__(self):
        self.client = None
        self.db = None
        self.collection = None
        self.connect()
        
    def connect(self):
            uri = "mongodb+srv://nuco112233:nuco123456@cluster0.hm6ek1d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
            self.client = MongoClient(uri, server_api=ServerApi('1'))
            self.db = self.client.get_database('User_Attention')
            self.collection = self.db['Responses']
            print("¡Conexión exitosa [Response DB]!")
            
    def save_response(self, response: Response):
        response_dict = response.model_dump()
        self.collection.insert_one(response_dict)
        

    def get_response_by_id(self, response_id: int) -> Response:
        data = self.collection.find_one({"id": response_id})
        if data:
            return {"id": data['id'], "status": data['status'],
                         "claim_description": data['claim_description'], "manager_response": data['manager_response']}

