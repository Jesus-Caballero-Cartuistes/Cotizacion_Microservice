from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def save_claim(self, claim_data):
        pass

    @abstractmethod
    def get_claim(self, claim_id):
        pass