from pymongo import MongoClient
from pymongo.server_api import ServerApi
from Authentication_Microservice.src.Database import Database


class MongoDB(Database):

    def __init__(self):
        self.client = None
        self.uri = None
        self.db = None
        self.connect()

    def connect(self):
        self.uri = "mongodb+srv://nuco112233:nuco123456@cluster0.hm6ek1d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        self.db = self.client.get_database('Authentication')
        print("¡Conexión exitosa [Authentication DB]!")

    def authenticate_user(self, id_number: int, name: str, last_name:str, expiration_date: str) -> bool:
        collection = self.db['Users']
        user = collection.find_one({"id_number": id_number})
        if user and user["name"] == name and user["expiration_date"] == expiration_date and user["last_name"] == last_name:
            return True
        return False
