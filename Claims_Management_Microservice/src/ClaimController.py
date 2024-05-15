from abc import ABC, abstractmethod


class ClaimController(ABC):
    @abstractmethod
    def create_claim(self, claim: dict):
        pass

    @abstractmethod
    def get_claim(self, claim_id: int):
        pass
    
    @abstractmethod
    def get_claims(self):
        pass
    
    @abstractmethod
    def delete_claim(self, claim_id: int):
        pass
    
    @abstractmethod
    def change_status(self, claim_id: int, status:str):
        pass
