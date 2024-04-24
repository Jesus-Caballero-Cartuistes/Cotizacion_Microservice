from abc import ABC, abstractmethod
from typing import Union
from ConsultaCostoSeguro import *
from DatosPoliza import *
from Seguro import *


class Cotizacion(ABC):
    """
    Interfaz para calcular una cotización de seguro.
    """

    @abstractmethod
    def calcular_cotizacion(self) -> Union[int, None]:
        """
        Método abstracto para calcular la cotización.
        """
        pass


class CotizacionMoto(Cotizacion):
    """
    Clase concreta para calcular la cotización de seguro de moto.
    """

    def __init__(self, datos_poliza: PolizaMoto):
        self.datos_poliza = datos_poliza

    def calcular_cotizacion(self) -> Union[int, None]:
        """
        Método para calcular la cotización de seguro de moto.
        """
        # Lógica para calcular la cotización de seguro de moto
        consulta_costo=ConsultaCostoSeguroDB(DatabaseImpl())
        seguroMoto = SeguroMoto(self.datos_poliza.cilindraje, consulta_costo)
        return int(seguroMoto.obtener_costo())



class CotizacionCarro(Cotizacion):
    """
    Clase concreta para calcular la cotización de seguro de carro.
    """

    def __init__(self, datos_poliza: PolizaCarro):
        self.datos_poliza = datos_poliza

    def calcular_cotizacion(self) -> Union[int, None]:
        """
        Método para calcular la cotización de seguro de carro.
        """
        # Lógica para calcular la cotización de seguro de carro
        consulta_seguro = ConsultaCostoSeguroDB(DatabaseImpl())
        seguro = SeguroCarro(self.datos_poliza.marca, self.datos_poliza.referencia,
                             self.datos_poliza.ano, self.datos_poliza.estado, self.datos_poliza.uso, consulta_seguro)
        return int(seguro.obtener_costo())


class CotizacionVida(Cotizacion):
    """
    Clase concreta para calcular la cotización de seguro de vida.
    """

    def __init__(self, datos_poliza: PolizaVida):
        self.datos_poliza = datos_poliza

    def calcular_cotizacion(self) -> Union[int, None]:
        """
        Método para calcular la cotización de seguro de vida.
        """
        # Lógica para calcular la cotización de seguro de vida
        consulta_seguro = ConsultaCostoSeguroDB(DatabaseImpl())
        seguro = SeguroVida(self.datos_poliza.edad, self.datos_poliza.beneficios, consulta_seguro)
        return int(seguro.obtener_costo())
