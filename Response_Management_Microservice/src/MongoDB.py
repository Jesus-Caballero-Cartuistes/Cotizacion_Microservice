from pymongo.server_api import ServerApi
from pymongo import MongoClient
from abc import ABC, abstractmethod
from pymongo import MongoClient
from pymongo.collection import Collection
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from datetime import datetime

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
        response_dict['response_date'] = datetime.now()
        self.collection.insert_one(response_dict)

    def get_responses_by_id(self, response_id: int):
        responses_list = []
        responses = self.collection.find({"id": response_id})
        for response in responses:
            response_info = {"id": response['id'], "name": response['name'], "lastName": response['lastName'], "email": response['email'], "status": response['status'],
                             "claim_description": response['claim_description'], "manager_response": response['manager_response'], "response_date": response['response_date']}
            responses_list.append(response_info)
        return responses_list
