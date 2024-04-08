from abc import ABC, abstractmethod

from database_implementation import DatabaseImpl


class ConsultaCostoSeguro(ABC):
    """
    Interfaz para consultar el costo del seguro en la base de datos.
    """

    @abstractmethod
    def consultar_costo_moto(self, cilindrada: float) -> float:
        """
        Método abstracto para consultar el costo del seguro de moto en la base de datos.
        """
        pass

    @abstractmethod
    def consultar_costo_vida(self, edad: int) -> float:
        """
        Método abstracto para consultar el costo del seguro de vida en la base de datos.
        """
        pass
    
    @abstractmethod
    def consultar_costo_vida_beneficios(self, beneficios: dict) -> float:
        """
        Método abstracto para consultar el costo del beneficio adicional en un seguro de vida.
        """
        pass
    
    @abstractmethod
    def consultar_costo_carro(self, modelo: str, referencia: str) -> float:
        """
        Método abstracto para consultar el costo del seguro de carro en la base de datos.
        """
        pass

    @abstractmethod
    def consultar_costo_carro_adicional(self, ano: int, estado: str, uso: str):
        """
        Método para consultar el costo adicional del seguro de carro en la base de datos.
        """
        pass
    
    


class ConsultaCostoSeguroDB(ConsultaCostoSeguro):
    """
    Implementación de la consulta del costo del seguro en la base de datos.
    """

    def __init__(self, database_impl: DatabaseImpl):
        self.database_impl = database_impl

    def consultar_costo_moto(self, cilindrada: float) -> float:
        """
        Método para consultar el costo del seguro de moto en la base de datos.
        """
        return self.database_impl.obtener_costo_moto(cilindrada)

    def consultar_costo_vida(self, edad: int) -> float:
        """
        Método para consultar el costo del seguro de vida en la base de datos.
        """
        return self.database_impl.obtener_costo_vida_base(edad)

    def consultar_costo_vida_beneficios(self, beneficios: dict) -> float:
        """
        Método para consultar el costo adicional del seguro de vida en la base de datos.
        """
        multiplicador_total_beneficios = 0
        for beneficio, estado in beneficios.items():  # Utiliza items() para iterar sobre el diccionario
            if estado:
                multiplicador_beneficio = self.database_impl.obtener_costo_vida_beneficio(
                    beneficio)
                multiplicador_total_beneficios += multiplicador_beneficio
        return multiplicador_total_beneficios

    def consultar_costo_carro(self, modelo: str, referencia:str) -> float:
        """
        Método para consultar el costo del seguro de carro en la base de datos.
        """
        return self.database_impl.obtener_costo_carro(modelo, referencia)

    def consultar_costo_carro_adicional(self, ano: int, estado: str, uso:str) -> float:
        """
        Método para consultar el costo adicional del seguro de carro en la base de datos.
        """
        multiplicador_total_beneficios = self.database_impl.obtener_costo_carro_ano(ano)
        multiplicador_total_beneficios += self.database_impl.obtener_costo_carro_estado(estado)
        multiplicador_total_beneficios += self.database_impl.obtener_costo_carro_uso(uso)
        return multiplicador_total_beneficios
