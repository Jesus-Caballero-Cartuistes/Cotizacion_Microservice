from abc import ABC, abstractmethod
from pymongo import MongoClient
from pymongo.collection import Collection
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException


class Response(BaseModel):
    id: int
    name: str
    lastName: str
    email: str
    status: str
    claim_description: str
    manager_response: str
