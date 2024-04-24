from abc import ABC, abstractmethod
from typing import Union
from Policy_Management_Microservice.src.CostController import CostController, CostControllerImpl
from Policy_Management_Microservice.src.Database import Database
from Policy_Management_Microservice.src.Policy import MotorcyclePolicy, CarPolicy, LifePolicy
from Policy_Management_Microservice.src.Insurance import MotorcycleInsurance, CarInsurance, LifeInsurance


class Quotation(ABC):
    """
    Interface to calculate an insurance quotation.
    """

    @abstractmethod
    def calculate(self) -> Union[int, None]:
        """
        Abstract method to calculate the quotation.
        """
        pass


class MotorcycleQuotation(Quotation):
    """
    Concrete class to calculate motorcycle insurance quotation.
    """

    def __init__(self, cost_controller: CostController):
        self.cost_controller = cost_controller

    def calculate(self, policy_data: MotorcyclePolicy) -> Union[int, None]:
        """
        Method to calculate motorcycle insurance quotation.
        """
        # Logic to calculate motorcycle insurance quotation
        return int(self.cost_controller.query_motorcycle_cost(policy_data.displacement))


class CarQuotation(Quotation):
    """
    Concrete class to calculate car insurance quotation.
    """

    def __init__(self, cost_controller: CostController):
        self.cost_controller = cost_controller

    def calculate(self, policy_data: CarPolicy) -> Union[int, None]:
        """
        Method to calculate car insurance quotation.
        """
        # Logic to calculate car insurance quotation
        cost = self.cost_controller.query_car_cost(
            policy_data.model, policy_data.reference)
        cost *= (1 + self.cost_controller.query_additional_car_cost(policy_data.year,
                 policy_data.status, policy_data.usage))
        return cost


class LifeQuotation(Quotation):
    """
    Concrete class to calculate life insurance quotation.
    """

    def __init__(self, cost_controller: CostController):
        self.cost_controller = cost_controller

    def calculate(self, policy_data: LifePolicy) -> Union[int, None]:
        """
        Method to calculate life insurance quotation.
        """
        # Logic to calculate life insurance quotation
        cost = self.cost_controller.query_life_cost(policy_data.age)
        cost *= (1 + self.cost_controller.query_life_cost_benefits(policy_data.benefits))
        return cost
