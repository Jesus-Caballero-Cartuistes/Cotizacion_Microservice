from abc import ABC, abstractmethod
from typing import Union
from Policy_Management_Microservice.src.CostController import CostController


class Insurance(ABC):
    """
    Abstract class to define an insurance.
    """

    @abstractmethod
    def get_cost(self) -> Union[float, None]:
        """
        Abstract method to get the insurance cost.
        """
        pass


class MotorcycleInsurance(Insurance):
    """
    Class to define a motorcycle insurance.
    """

    def __init__(self, displacement: float, cost_query: CostController):
        super().__init__()
        self.displacement = displacement
        self.cost_query = cost_query

    def get_cost(self) -> Union[float, None]:
        """
        Method to get the cost of motorcycle insurance.
        """
        # Query the cost of motorcycle insurance from the database, using the displacement as a criterion
        cost = self.cost_query.query_motorcycle_cost(self.displacement)
        if cost is None:
            return -1
        return cost


class LifeInsurance(Insurance):
    """
    Class to define a life insurance.
    """

    def __init__(self, age: int, benefits: dict, cost_query: CostController):
        super().__init__()
        self.age = age
        self.benefits = benefits
        self.cost_query = cost_query

    def get_cost(self) -> float:
        """
        Method to get the cost of life insurance.
        """
        # Query the cost of life insurance from the database, using the age as a criterion
        cost = self.cost_query.query_life_cost(
            self.age) * (1 + self.cost_query.query_life_cost_benefits(self.benefits))
        return cost


class CarInsurance(Insurance):
    """
    Class to define a car insurance.
    """

    def __init__(self, model: str, reference: str, year: int, status: str, usage: str, cost_query: CostController):
        super().__init__()
        self.model = model
        self.reference = reference
        self.year = year
        self.status = status
        self.usage = usage
        self.cost_query = cost_query

    def get_cost(self) -> float:
        """
        Method to get the cost of car insurance.
        """
        # Query the cost of car insurance from the database, using the model as a criterion
        cost = self.cost_query.query_car_cost(self.model, self.reference)
        cost *= (1 + self.cost_query.query_additional_car_cost(self.year,
                 self.status, self.usage))
        return cost
