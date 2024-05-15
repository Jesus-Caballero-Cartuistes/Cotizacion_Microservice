from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError
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

    def save_claim(self, claim_data: dict):
        # Assuming 'id' is the key for claim ID
        claim_id = claim_data.get('id')
        existing_claim = self.collection.find_one({"id": claim_id})
        if existing_claim:
            raise HTTPException(
                status_code=400, detail="Ya existe un reclamo con este ID")
        try:
            self.collection.insert_one(claim_data)
            claim_data.pop('_id', None)
            return claim_data
        except DuplicateKeyError:
            raise HTTPException(
                status_code=400, detail="Ya existe un reclamo con este ID")

    def get_claim(self, claim_id):
        claim = self.collection.find_one({'id': claim_id})
        if claim:
            return {"id": claim['id'], "name": claim['name'], "lastName": claim['lastName'], "email": claim['email'], "status": claim['status'], "details": claim['details'], "date": claim['date']}

    def get_claims(self):
        claims_list = []
        # Obtener todos los reclamos de la colección ordenados por fecha de más viejo a más reciente
        claims = self.collection.find().sort("date", 1)
        for claim in claims:
            claim_info = {
                "id": claim['id'],
                "name": claim['name'],
                "lastName": claim['lastName'],
                "email": claim['email'],
                "status": claim['status'],
                "details": claim['details'],
                "date": claim['date']
            }
            claims_list.append(claim_info)
        return claims_list

    def delete_claim(self, claim_id):
        # Eliminar el reclamo con el ID proporcionado
        result = self.collection.delete_one({"id": claim_id})
        # Verificar si se eliminó correctamente
        return result.deleted_count

    def change_status(self, claim_id, status):
        # Actualizar el estado del reclamo con el ID proporcionado
        result = self.collection.update_one(
            {"id": claim_id}, {"$set": {"status": status}})

        # Verificar si se actualizó correctamente
        if result.modified_count == 1:
            print("Estado del reclamo actualizado exitosamente")
        else:
            print("No se encontró ningún reclamo con el ID proporcionado")
