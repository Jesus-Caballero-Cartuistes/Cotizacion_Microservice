from fastapi import APIRouter, HTTPException, WebSocketDisconnect
from datetime import datetime
from Claims_Management_Microservice.src.ClaimControllerImpl import ClaimControllerImpl
from Claims_Management_Microservice.src.Claim import Claim
from Claims_Management_Microservice.src.MongoDB import MongoDB
from fastapi import WebSocket
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


claim_router = APIRouter()
mongoDB = MongoDB()
claim_controller = ClaimControllerImpl(mongoDB)


@claim_router.get("/")
async def root():
    return {"Microservice": "Claims Management"}

# Lista para mantener las conexiones activas
active_connections = set()


@claim_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # Acepta la conexión WebSocket
    await websocket.accept()
    # Agrega la conexión a la lista de conexiones activas
    active_connections.add(websocket)
    try:
        while True:
            # Espera a que se envíen datos al WebSocket
            data = await websocket.receive_text()
            # Aquí se verifica si es una acción para agregar un nuevo reclamo
            if data == "new_claim":
                # Obtén la lista actualizada de reclamos
                claims = claim_controller.get_claims()
                # Convierte los reclamos a formato JSON
                claims_json = jsonable_encoder(claims)
                # Envía la lista de reclamos a todos los clientes conectados
                for connection in active_connections:
                    await connection.send_json(claims_json)
    except WebSocketDisconnect:
        # Maneja la desconexión del cliente eliminando la conexión de la lista de conexiones activas
        active_connections.remove(websocket)
        
        
@claim_router.post("/claims/")
async def create_claim(claim: Claim):
    claim_data = claim.model_dump()
    claim_data['date'] = datetime.now()
    claim_controller.create_claim(claim_data)
    return claim_data

@claim_router.get("/claims/")
async def get_claims():
    claims = claim_controller.get_claims()
    return claims


@claim_router.get("/claims/{claim_id}")
async def get_claim(claim_id: int):
    claim = claim_controller.get_claim(claim_id)
    if claim:
        return claim
    else:
        raise HTTPException(status_code=404, detail="Claim not found")

@claim_router.delete("/claims/{claim_id}")
async def delete_claim(claim_id: int):
    response = claim_controller.delete_claim(claim_id)
    if response:
        return response
    else:
        raise HTTPException(status_code=404, detail="Claim not found")
    

@claim_router.put("/claims/{claim_id}")
async def change_status(claim_id: int, status:str):
    response = claim_controller.change_status(claim_id, status)
    if response:
        return response
    else:
        raise HTTPException(status_code=404, detail="Claim not found")