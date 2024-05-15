from fastapi import APIRouter
from fastapi import HTTPException
from Authentication_Microservice.src.MongoDB import MongoDB
from Authentication_Microservice.src.EmployeeAuthenticationRequest import *
from Authentication_Microservice.src.VehicleAuthenticationRequest import *
from Authentication_Microservice.src.UserAuthenticationRequest import *

mongoDB = MongoDB()
authentication_router = APIRouter()


@authentication_router.get("/")
async def root():
    return {"Microservice": "Authentication"}


@authentication_router.post("/authenticate_moto/")
async def authenticate_moto(request: MotorcycleAuthenticationRequest):
    id_propietary = request.identification
    first_name = request.first_name
    expiration_date = request.expDate
    last_name = request.last_name
    plate = request.plate
    # Suponiendo que mongoDB.authenticate_user devuelve un booleano
    if mongoDB.authenticate_vehicle(id_propietary, first_name, last_name, expiration_date, plate):
        return {"authenticated": True}
    else:
        raise HTTPException(status_code=401, detail="Authentication failed")


@authentication_router.post("/authenticate_car/")
async def authenticate_car(request: CarAuthenticationRequest):
    id_propietary = request.identification
    first_name = request.first_name
    expiration_date = request.expDate
    last_name = request.last_name
    plate = request.plate
    # Suponiendo que mongoDB.authenticate_user devuelve un booleano
    if mongoDB.authenticate_vehicle(id_propietary, first_name, last_name, expiration_date, plate):
        return {"authenticated": True}
    else:
        raise HTTPException(status_code=401, detail="Authentication failed")
    
    
@authentication_router.post("/authenticate_employee/")
async def authenticate_employee(request: EmployeeAuthenticationRequest):
    user = request.user
    password = request.password
    if mongoDB.authenticate_employee(user, password):
        return {"authenticated": True}
    else:
        raise HTTPException(status_code=401, detail="Authentication failed")


@authentication_router.post("/authenticate_user/")
async def authenticate_user(request: UserAuthenticationRequest):
    id_propietary = request.identification
    first_name = request.first_name
    expiration_date = request.expDate
    last_name = request.last_name
    age = request.age
    if mongoDB.authenticate_user(id_propietary, first_name, last_name, expiration_date, age):
        return {"authenticated": True}
    else:
        raise HTTPException(status_code=401, detail="Authentication failed")


@authentication_router.get("/authenticate/{plate}")
async def get_displacement(plate: str):
    displacement = mongoDB.get_displacement(plate)
    if displacement:
        return displacement
    else:
        raise HTTPException(status_code=401, detail="Plate Not Found")
