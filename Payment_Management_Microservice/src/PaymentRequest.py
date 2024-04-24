from datetime import datetime
from pydantic import BaseModel

class PaymentRequest(BaseModel):
    quote_id: str  # Identificador de la cotización
    billing_info: dict  # Información de facturación
    payment_method: str  # Método de pago
    amount: float  # Monto total a pagar
    currency: str  # Moneda del pago
    payment_date: datetime  # Fecha y hora del pago
    payment_status: str  # Estado del pago
