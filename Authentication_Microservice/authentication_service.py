from fastapi import APIRouter
from fastapi import HTTPException
from Authentication_Microservice.src.AuthenticationRequest import AuthenticationRequest
from Authentication_Microservice.src.MongoDB import MongoDB

authentication_router = APIRouter()




# Endpoint para la autenticación
@authentication_router.post("/authenticate/")
async def authenticate_user(request: AuthenticationRequest):
    mongo_db = MongoDB()
    id_number = request.id_number
    name = request.name
    expiration_date = request.expiration_date
    last_name = request.last_name
    if mongo_db.authenticate_user(id_number, name, last_name, expiration_date):
        return {"authenticated": True}
    else:
        raise HTTPException(status_code=401, detail="Authentication failed")
