from datetime import datetime
from abc import ABC, abstractmethod
from typing import Dict

class Database(ABC):
    
    @abstractmethod
    def connect():
        pass
    
    @abstractmethod
    def save_payment_record(self, payment_data: dict) -> None:
        pass
