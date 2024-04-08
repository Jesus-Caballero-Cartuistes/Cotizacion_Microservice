
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta
from cotizacion import *
from datos_poliza import *

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}


@app.post("/crear_poliza_moto/")
async def crear_poliza_moto(poliza_moto: PolizaMoto):
    # Crear un objeto PolizaMoto con los datos recibidos
    poliza_dict = poliza_moto.model_dump()
    poliza_dict["cotizacion"] = CotizacionMoto(
        poliza_moto).calcular_cotizacion()
    poliza_dict["fecha_inicio"] = datetime.now().date()
    poliza_dict["fecha_final"] = datetime.now().date() + timedelta(days=365)
    return poliza_dict


@app.post("/crear_poliza_carro/")
async def crear_poliza_carro(poliza_carro: PolizaCarro):
    # Crear un objeto PolizaMoto con los datos recibidos
    poliza_dict = poliza_carro.model_dump()
    poliza_dict["cotizacion"] = CotizacionCarro(
        poliza_carro).calcular_cotizacion()
    poliza_dict["fecha_inicio"] = datetime.now().date()
    poliza_dict["fecha_final"] = datetime.now().date() + timedelta(days=365)
    return poliza_dict


@app.post("/crear_poliza_vida/")
async def crear_poliza_vida(poliza_vida: PolizaVida):
    # Crear un objeto PolizaMoto con los datos recibidos
    poliza_dict = poliza_vida.model_dump()
    poliza_dict["cotizacion"] = CotizacionVida(
        poliza_vida).calcular_cotizacion()
    poliza_dict["fecha_inicio"] = datetime.now().date()
    poliza_dict["fecha_final"] = datetime.now().date() + \
        timedelta(days=365)
    return poliza_dict
