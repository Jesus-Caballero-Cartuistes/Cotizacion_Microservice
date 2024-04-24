from abc import ABC, abstractmethod

class Database(ABC):
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def authenticate_user(self, id_number: str, name: str, expiration_date: str) -> bool:
        pass
