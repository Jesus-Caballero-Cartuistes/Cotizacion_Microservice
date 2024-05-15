from abc import ABC
from pydantic import BaseModel


class VehicleQuotation(BaseModel, ABC):
    """
    Abstract class for policy data.
    """
    plate: str


class CarQuotation(VehicleQuotation):
    """
    Concrete class for car insurance policy.
    """
    reference: str
    model: str
    year: int
    usage: str


class MotorcycleQuotation(VehicleQuotation):
    """
    Concrete class for motorcycle insurance policy.
    """
    displacement: float


class LifeQuotation(BaseModel):
    """
    Concrete class for life insurance policy.
    """
    age: int
    benefits: dict
