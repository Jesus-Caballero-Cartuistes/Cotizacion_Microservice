from abc import ABC, abstractmethod
from pymongo import MongoClient
from datetime import datetime
from pydantic import BaseModel
from Claims_Management_Microservice.src.Database import Database
from Claims_Management_Microservice.src.ClaimController import ClaimController


class ClaimControllerImpl(ClaimController):
    def __init__(self, database: Database):
        self.db = database

    def create_claim(self, claim_data: dict):
        return self.db.save_claim(claim_data)

    def get_claim(self, claim_id: int):
        return self.db.get_claim(claim_id)
