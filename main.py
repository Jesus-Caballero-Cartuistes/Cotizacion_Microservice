from fastapi import FastAPI

from Authentication_Microservice.authentication_service import authentication_router
from Claims_Management_Microservice.claim_service import claim_router
from Policy_Management_Microservice.policy_service import policy_router
from Response_Management_Microservice.response_service import response_router
from Payment_Management_Microservice.payment_service import payment_router

app = FastAPI()

# Agregar routers al app principal
app.include_router(authentication_router, prefix="/auth",
                   tags=["Authentication Microservice"])
app.include_router(policy_router, prefix="/policy",
                   tags=["Policy Management Microservice"])
app.include_router(claim_router, prefix="/claim",
                   tags=["Claims Management Microservice"])
app.include_router(response_router, prefix="/response",
                   tags=["Response Management Microservice"])
app.include_router(payment_router, prefix="/payment",
                   tags=["Payment Management Microservice"])


@app.get("/")
async def root():
    return {"Microservices": ["Authentication", "Claims Management", "Policy Management", "Response Management0", "Payment Management"]}
