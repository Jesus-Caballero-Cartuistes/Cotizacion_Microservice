from pymongo import MongoClient
from pymongo.server_api import ServerApi
from Policy_Management_Microservice.src.Database import Database


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
        self.db = self.client.get_database('Prices')
        print("¡Conexión exitosa [Policy DB]!")
        
    def get_displacement(self, plate: str) -> str:

        collection = self.client.get_database(
            'Authentication').get_collection('Vehicles')
        vehicle = collection.find_one({"plate": plate})
        if vehicle:
            return vehicle['displacement']
        return None

    def get_car_info(self, plate: str) -> dict:
        collection = self.client.get_database(
            'Authentication').get_collection('Vehicles')
        vehicle = collection.find_one({"plate": plate})
        if vehicle:
            return {"reference": vehicle['reference'], "model": vehicle['model'], "year": vehicle['year'], "usage": vehicle['usage']}
        return None
    
    def get_motorcycle_cost(self, displacement: float) -> float:
        self.collection = self.db['Soat']
        data = self.collection.find_one({"tipo": "moto", "cilindrada_min": {
                                   "$lte": displacement}, "cilindrada_max": {"$gte": displacement}})
        if data and 'precio' in data:
            return float(data['precio'])
        else:
            return -1

    def get_life_base_cost(self, age: int) -> float:
        self.collection = self.db['LifeInsurance']
        data = self.collection.find_one(
            {"edad_min": {"$lte": age}, "edad_max": {"$gte": age}})
        if data and 'precio' in data:
            return float(data['precio'])
        else:
            return -1

    def get_life_benefit_cost(self, benefit: str) -> float:
        self.collection = self.db['LifeInsurance']
        document = self.collection.find_one({"beneficio": benefit})
        if document and 'precio' in document:
            return float(document['precio'])
        else:
            return 0

    def get_car_cost(self, model: str, reference: str) -> float:
        self.collection = self.db['CarPrices']
        data = self.collection.find_one(
            {"model": model, "reference": reference})
        if data and 'price' in data:
            return float(data['price'])
        else:
            return 0

    def get_car_year_cost(self, year: int) -> float:
        self.collection = self.db['CarPrices']
        document = self.collection.find_one({str(year): {"$exists": True}})
        if document:
            return float(document[str(year)])
        else:
            return 0

    def get_car_usage_cost(self, usage: str) -> float:
        self.collection = self.db['CarPrices']
        document = self.collection.find_one({usage: {"$exists": True}})
        if document:
            return float(document[usage])
        else:
            return 0


