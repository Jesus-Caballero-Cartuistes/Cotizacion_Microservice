from fastapi import APIRouter, HTTPException

from Response_Management_Microservice.src.Response import Response
from Response_Management_Microservice.src.MongoDB import *
from Response_Management_Microservice.src.ResponseControllerImpl import *
response_router = APIRouter()
mongoDB = MongoDB()
response_controller = ResponseControllerImpl(mongoDB)

# Endpoint for response management


@response_router.post("/responses/")
async def create_response(response: Response):
    response_controller.create_response(response)
    return {"message": "Respuesta publicada correctamente"}

# Get a response by ID


@response_router.get("/responses/{response_id}")
async def get_responses(response_id: int):
    responses = response_controller.get_responses(response_id)
    if not responses:
        raise HTTPException(status_code=404, detail="Response not found")
    return responses
