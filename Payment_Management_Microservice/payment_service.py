
from datetime import datetime
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from typing import Dict
from Payment_Management_Microservice.src.MockPaymentGateway import MockPaymentGateway
from Payment_Management_Microservice.src.MongoDB import MongoDB
from Payment_Management_Microservice.src.PaymentRequest import PaymentRequest

payment_router = APIRouter()
payment_gateway = MockPaymentGateway()
mongoDB = MongoDB()


@payment_router.get("/")
async def root():
    return {"Microservice": "Payment Management"}

def process_payment(payment_request: PaymentRequest) -> Dict[str, str]:
    if payment_request.amount <= 0:
        raise HTTPException(
            status_code=400, detail="El monto del pago debe ser mayor que cero")

    payment_data = payment_request.model_dump()

    # Procesar el pago utilizando la pasarela de pago
    is_payment_successful = payment_gateway.process_payment(payment_data)

    if is_payment_successful:
        # Guardar el registro del pago en la base de datos
        mongoDB.save_payment_record(payment_data)
        return {"message": "Pago procesado correctamente"}
    else:
        raise HTTPException(
            status_code=500, detail="Error al procesar el pago")

# Endpoint para el procesamiento de pagos
@payment_router.post("/payments/")
async def handle_payment(payment_request: PaymentRequest):
    return process_payment(payment_request)
