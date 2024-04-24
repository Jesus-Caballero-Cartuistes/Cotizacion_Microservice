from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
from Claims_Management_Microservice.src.Database import Database

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
        self.db = self.client['User_Attention']
        self.collection = self.db['Claims']
        print("¡Conexión exitosa [Claims DB]!")

    def save_claim(self, claim_data : dict):
        return self.collection.insert_one(claim_data)

    def get_claim(self, claim_id):
        claim = self.collection.find_one({'id': claim_id})
        if claim:
            return {"id": claim['id'], "status": claim['status'], "details": claim['details'], "date": claim['date']}
        
