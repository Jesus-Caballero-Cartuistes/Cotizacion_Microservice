
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class DatabaseImpl:

    def __init__(self):
        
        uri = "mongodb+srv://nuco112233:nuco123456@cluster0.hm6ek1d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client.get_database('Prices')
        print("¡Conexion Exitosa!")
        

    def obtener_costo_moto(self, cilindrada):
        """
        Método estático para obtener el costo de una moto basado en la cilindrada.
        """
        collection = self.db['Soat']
        data = collection.find_one({"tipo":"moto", "cilindrada_min": {"$lte": cilindrada}, "cilindrada_max": {"$gte": cilindrada}})
        if data is not None and 'precio' in data:
            return float(data['precio'])
        else:
            return -1
        


    def obtener_costo_vida_base(self, edad: int):
        """
        Método estático para obtener el costo de un seguro de vida basado en la edad.
        """
        # Lógica para obtener el costo de un seguro de vida basado en la edad
        collection = self.db['LifeInsurance']
        data = collection.find_one(
            {"edad_min": {"$lte": edad}, "edad_max": {"$gte": edad}})
        return data['precio']



    def obtener_costo_vida_beneficio(self, beneficio: str):
        """
        Método estático para obtener el costo de un seguro de vida basado en el beneficio adicional.
        """
        # Lógica para obtener el costo de un seguro de vida basado en la edad
        collection = self.db['LifeInsurance']
        document = collection.find_one({"beneficio": beneficio})
        if document:
            costo_carro = document['precio']
            return costo_carro
        else:
            return -1


    def obtener_costo_carro(self, marca: str, referencia: str):
        """
        Método estático para obtener el costo de un carro basado en el modelo.
        """
        # Lógica para obtener el costo de un carro basado en el modelo
        collection = self.db['CarPrices']
        data = collection.find_one({"marca": marca, "referencia" : referencia})
        if data is not None and 'precio' in data:
            return float(data['precio'])
        else:
            return -1

    def obtener_costo_carro_ano(self, ano: int):
        """
        Método estático para obtener el costo de un carro basado en el modelo.
        """
        # Lógica para obtener el costo de un carro basado en el modelo
        collection = self.db['CarPrices']
        document = collection.find_one({str(ano): {"$exists": True}})
        if document:
            costo_carro = document[str(ano)]
            return costo_carro
        else:
            return -1
        
    def obtener_costo_carro_estado(self, estado: str):
        """
        Método estático para obtener el costo de un carro basado en el modelo.
        """
        # Lógica para obtener el costo de un carro basado en el modelo
        collection = self.db['CarPrices']
        document = collection.find_one({estado: {"$exists": True}})
        if document:
            costo_carro = document[estado]
            return costo_carro
        else:
            return -1
        
    def obtener_costo_carro_uso(self, uso: str):
        """
        Método estático para obtener el costo de un carro basado en el modelo.
        """
        # Lógica para obtener el costo de un carro basado en el modelo
        collection = self.db['CarPrices']
        document = collection.find_one({uso: {"$exists": True}})
        if document:
            costo_carro = document[uso]
            return costo_carro
        else:
            return -1
