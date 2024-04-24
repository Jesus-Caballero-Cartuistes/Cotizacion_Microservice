from abc import ABC
from pydantic import BaseModel


class Policy(BaseModel, ABC):
    """
    Abstract class for policy data.
    """
    identification_type: str
    identification: int
    first_name: str
    last_name: str


class CarPolicy(Policy):
    """
    Concrete class for car insurance policy.
    """
    reference: str
    model: str
    year: int
    status: str
    usage: str


class MotorcyclePolicy(Policy):
    """
    Concrete class for motorcycle insurance policy.
    """
    displacement: float


class LifePolicy(Policy):
    """
    Concrete class for life insurance policy.
    """
    age: int
    benefits: dict
