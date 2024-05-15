from datetime import datetime
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

    def authenticate_user(self, id_number: int, name: str, last_name:str, expiration_date: str, age:int) -> bool:
        collection = self.db['Users']
        user = collection.find_one({"id_number": id_number})
        if user and user["name"] == name and user["expiration_date"] == expiration_date and user["last_name"] == last_name and self.validate_birthdate(id_number,age):
            return True
        return False
    
    def authenticate_vehicle(self, id_propietary: int, firt_name: str, last_name: str, exp_date: str, plate:str) -> bool:
        collection = self.db['Vehicles']
        user = collection.find_one({"plate": plate})
        if user and user["id_propietary"] == id_propietary and user["first_name"] == firt_name and user["exp_date"] == exp_date and user["last_name"] == last_name:
            return True
        return False
    
    def authenticate_employee(self, user: str, password: str) -> bool:
        collection = self.db['Employees']
        employee = collection.find_one({"user": user})
        if employee and employee["user"] == user and employee["password"] == password:
            return True
        return False
    
    def get_displacement(self, plate: str) -> str:
        collection = self.db['Vehicles']
        vehicle = collection.find_one({"plate": plate})
        if vehicle:
            return vehicle['displacement']
        return None
    
    def validate_birthdate(self, id_number: int, age: int) -> bool:
        collection = self.db['Users']
        user = collection.find_one({"id_number": id_number})
        if user:
            # Obtener la fecha de nacimiento del usuario
            birthdate = user.get("birthdate")
            if birthdate:
                # Calcular la edad del usuario a partir de la fecha de nacimiento
                # Convertir la fecha de nacimiento a un objeto datetime
                birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
                today = datetime.today()
                calculated_age = today.year - birthdate.year - \
                    ((today.month, today.day) < (birthdate.month, birthdate.day))

                # Comparar la edad calculada con la edad proporcionada
                if calculated_age == age:
                    return True
        return False
