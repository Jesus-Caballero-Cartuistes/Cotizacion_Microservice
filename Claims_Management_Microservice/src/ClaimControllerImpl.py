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
        self.db.save_claim(claim_data)

    def get_claims(self):
        return self.db.get_claims()
    
    def get_claim(self, claim_id: int):
        return self.db.get_claim(claim_id)
    
    def delete_claim(self, claim_id: int):
        return self.db.delete_claim(claim_id)
    
    def change_status(self, claim_id: int, status:str):
        return self.db.change_status(claim_id, status)
