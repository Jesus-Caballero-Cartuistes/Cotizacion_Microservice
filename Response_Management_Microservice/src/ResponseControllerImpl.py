
from fastapi import FastAPI, HTTPException

from Response_Management_Microservice.src.Database import Database
from Response_Management_Microservice.src.Response import Response
from Response_Management_Microservice.src.ResponseController import ResponseController


class ResponseControllerImpl(ResponseController):
    def __init__(self, database: Database):
        self.database = database

    def create_response(self, response: Response):
        self.database.save_response(response)

    def get_response(self, response_id: int):
        response = self.database.get_response_by_id(response_id)
        if not response:
            return None 
        return response
