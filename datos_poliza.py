from abc import ABC
from pydantic import BaseModel


class DatosPoliza(BaseModel, ABC):
    """
    Clase abstracta para los datos de una póliza.
    """
    tipo_identificacion: str
    identificacion: int
    nombre: str
    apellido: str


class PolizaCarro(DatosPoliza):
    """
    Clase concreta para una póliza de seguro de carro.
    """
    marca: str
    referencia: str
    ano: int
    estado: str
    uso: str


class PolizaMoto(DatosPoliza):
    """
    Clase concreta para una póliza de seguro de moto.
    """
    cilindraje: float


class PolizaVida(DatosPoliza):
    """
    Clase concreta para una póliza de seguro de vida.
    """
    edad: int
    beneficios: dict
    
    
