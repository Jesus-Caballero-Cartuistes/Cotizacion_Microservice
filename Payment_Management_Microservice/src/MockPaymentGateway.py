from datetime import datetime
from abc import ABC, abstractmethod
from typing import Dict

from Payment_Management_Microservice.src.PaymentGateway import PaymentGateway

class MockPaymentGateway(PaymentGateway):
    def process_payment(self, payment_request: dict) -> bool:
        # Simulación de procesamiento de pago exitoso
        return True
