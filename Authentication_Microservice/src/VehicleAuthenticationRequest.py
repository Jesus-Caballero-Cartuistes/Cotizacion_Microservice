from abc import ABC
from pydantic import BaseModel


class VehicleAuthenticationRequest(BaseModel, ABC):
    """
    Abstract class for policy data.
    """
    identification: int
    expDate: str
    first_name: str
    last_name: str
    cost: int
    start_date: str
    end_date: str
    email: str
    plate: str


class CarAuthenticationRequest(VehicleAuthenticationRequest):
    """
    Concrete class for car insurance policy.
    """
    reference: str
    model: str
    year: int
    usage: str


class MotorcycleAuthenticationRequest(VehicleAuthenticationRequest):
    """
    Concrete class for motorcycle insurance policy.
    """
    displacement: float
    


class LifeAuthenticationRequest(VehicleAuthenticationRequest):
    """
    Concrete class for life insurance policy.
    """
    age: int
    benefits: dict
