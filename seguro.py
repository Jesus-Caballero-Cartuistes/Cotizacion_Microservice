from abc import ABC, abstractmethod
from typing import Union
from ConsultaCostoSeguro import *


class Seguro(ABC):
    """
    Clase abstracta para definir un seguro.
    """

    @abstractmethod
    def obtener_costo(self) -> Union[float, None]:
        """
        Método abstracto para obtener el costo del seguro.
        """
        pass


class SeguroMoto(Seguro):
    """
    Clase para definir un seguro de moto.
    """

    def __init__(self, cilindrada: float, consulta_costo: ConsultaCostoSeguro):
        super().__init__()
        self.cilindrada = cilindrada
        self.consulta_costo = consulta_costo

    def obtener_costo(self) -> Union[float, None]:
        """
        Método para obtener el costo del seguro de moto.
        """
        # Consultar el costo del seguro de moto en la base de datos, utilizando la cilindrada como criterio
        costo = self.consulta_costo.consultar_costo_moto(self.cilindrada)
        if costo is None:
            return -1
        return costo


class SeguroVida(Seguro):
    """
    Clase para definir un seguro de vida.
    """

    def __init__(self, edad: int, beneficios: dict, consulta_costo: ConsultaCostoSeguro):
        super().__init__()
        self.edad = edad
        self.beneficios = beneficios
        self.consulta_costo = consulta_costo

    def obtener_costo(self) -> float:
        """
        Método para obtener el costo del seguro de vida.
        """
        # Consultar el costo del seguro de vida en la base de datos, utilizando la edad como criterio
        costo = self.consulta_costo.consultar_costo_vida(
            self.edad) * (1 + self.consulta_costo.consultar_costo_vida_beneficios(self.beneficios))
        return costo


class SeguroCarro(Seguro):
    """
    Clase para definir un seguro de carro.
    """

    def __init__(self, modelo: str, referencia: str, ano: int, estado: str, uso: str, consulta_costo: ConsultaCostoSeguro):
        super().__init__()
        self.modelo = modelo
        self.referencia = referencia
        self.ano = ano
        self.estado = estado
        self.uso = uso
        self.consulta_costo = consulta_costo

    def obtener_costo(self) -> float:
        """
        Método para obtener el costo del seguro de carro.
        """
        # Consultar el costo del seguro de carro en la base de datos, utilizando el modelo como criterio
        costo = self.consulta_costo.consultar_costo_carro(self.modelo, self.referencia)
        costo *= (1 + self.consulta_costo.consultar_costo_carro_adicional(self.ano,
                  self.estado, self.uso))
        return costo
