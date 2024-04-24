from datetime import datetime
from abc import ABC, abstractmethod
from typing import Dict

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, payment_request: dict) -> bool:
        pass
