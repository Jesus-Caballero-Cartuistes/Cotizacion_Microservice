from abc import ABC, abstractmethod
from pymongo import MongoClient
from pymongo.collection import Collection
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

from Response_Management_Microservice.src.Response import Response


class Database(ABC):

    @abstractmethod
    def connect(self):
        """
        Abstract method to connect the database.
        """
        pass

    @abstractmethod
    def save_response(self, response: Response):
        pass

    @abstractmethod
    def get_responses_by_id(self, response_id: int) -> dict:
        pass
