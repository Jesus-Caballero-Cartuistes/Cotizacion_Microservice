from abc import ABC, abstractmethod


class ClaimController(ABC):
    @abstractmethod
    def create_claim(self, claim: dict):
        pass

    @abstractmethod
    def get_claim(self, claim_id: int):
        pass
