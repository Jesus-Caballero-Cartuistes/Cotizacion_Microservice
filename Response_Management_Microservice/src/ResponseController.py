from abc import ABC, abstractmethod
from pymongo import MongoClient
from pymongo.collection import Collection
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

from Response_Management_Microservice.src.Response import Response


class ResponseController(ABC):
    @abstractmethod
    def create_response(self, response: Response):
        pass

    @abstractmethod
    def get_response(self, response_id: int):
        pass
