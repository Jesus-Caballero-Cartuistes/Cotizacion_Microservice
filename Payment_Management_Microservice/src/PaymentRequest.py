from abc import ABC
from datetime import datetime
from pydantic import BaseModel

class PaymentRequest(BaseModel, ABC):
    quote_id: str  # Identificador de la cotización
    insuranceType: str
    insurance_start_date: str #inicio de vigencia del seguro
    insurance_end_date: str #fin de videncia del seguro 
    payment_method: str  # Método de pago
    amount: float  # Monto total a pagar
    currency: str  # Moneda del pago
    payment_date: datetime  # Fecha y hora del pago
    
class MotoPaymentRequest(PaymentRequest):
    plate: str  # placa del vehiculo


class CarPaymentRequest(PaymentRequest):
    plate: str  # placa del vehiculo

class MotoPaymentRequest(PaymentRequest):
    plate: str  # placa del vehiculo


class LifePaymentRequest(PaymentRequest):
    user_id: int  # placa del vehiculo
    benefits: dict 
