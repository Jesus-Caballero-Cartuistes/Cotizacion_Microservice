from fastapi import APIRouter, HTTPException
from datetime import datetime
from Claims_Management_Microservice.src.ClaimControllerImpl import ClaimControllerImpl
from Claims_Management_Microservice.src.Claim import Claim
from Claims_Management_Microservice.src.MongoDB import MongoDB

claim_router = APIRouter()
mongoDB = MongoDB()
claim_controller = ClaimControllerImpl(mongoDB)


@claim_router.get("/")
async def root():
    return {"Microservice": "Claims Management"}


@claim_router.post("/claims/")
async def create_claim(claim: Claim):
    claim_data = claim.model_dump()
    claim_data['date'] = datetime.now()
    claim_id = claim_controller.create_claim(claim_data)
    return {"id": str(claim_id), **claim.model_dump()}


@claim_router.get("/claims/{claim_id}")
async def get_claim(claim_id: int):
    claim = claim_controller.get_claim(claim_id)
    if claim:
        return claim
    else:
        raise HTTPException(status_code=404, detail="Claim not found")
