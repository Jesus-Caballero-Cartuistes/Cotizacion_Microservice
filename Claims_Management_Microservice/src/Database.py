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

    @abstractmethod
    def get_claims(self):
        pass
    
    @abstractmethod
    def delete_claim(self, claim_id):
        pass

    @abstractmethod
    def change_status(self, claim_id, status):
        pass