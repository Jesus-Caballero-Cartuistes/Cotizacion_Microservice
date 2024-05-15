from abc import ABC, abstractmethod
from typing import Union
from Policy_Management_Microservice.src.CostController import CostController, CostControllerImpl
from Policy_Management_Microservice.src.Database import Database
from Policy_Management_Microservice.src.Quotation import MotorcycleQuotation, CarQuotation, LifeQuotation


class QuotationMethods(ABC):
    """
    Interface to calculate an insurance quotation.
    """

    @abstractmethod
    def calculate_cost(self) -> Union[int, None]:
        """
        Abstract method to calculate the quotation.
        """
        pass


class MotorcycleQuotationMethods(QuotationMethods):
    """
    Concrete class to calculate motorcycle insurance quotation.
    """

    def __init__(self, cost_controller: CostController):
        self.cost_controller = cost_controller

    def calculate_cost(self, displacement: int) -> Union[int, None]:
        """
        Method to calculate motorcycle insurance quotation.
        """
        # Logic to calculate motorcycle insurance quotation
        return int(self.cost_controller.query_motorcycle_cost(displacement))

    def get_displacement(self, plate: str) -> Union[int, None]:
        """
        Method to calculate motorcycle insurance quotation.
        """
        # Logic to calculate motorcycle insurance quotation
        return int(self.cost_controller.query_motorcycle_displacement(plate))


class CarQuotationMethods(QuotationMethods):
    """
    Concrete class to calculate car insurance quotation.
    """

    def __init__(self, cost_controller: CostController):
        self.cost_controller = cost_controller

    def calculate_cost(self, policy_data: CarQuotation) -> Union[int, None]:
        """
        Method to calculate car insurance quotation.
        """
        # Logic to calculate car insurance quotation
        cost = self.cost_controller.query_car_cost(
            policy_data.model, policy_data.reference)
        cost *= (1 + self.cost_controller.query_additional_car_cost(
            policy_data.year, policy_data.usage))
        return cost

    def get_car_info(self, plate: str) -> Union[dict, None]:
        """
        Method to calculate motorcycle insurance quotation.
        """
        # Logic to calculate motorcycle insurance quotation
        return self.cost_controller.query_car_info(plate)


class LifeQuotationMethods(QuotationMethods):
    """
    Concrete class to calculate life insurance quotation.
    """

    def __init__(self, cost_controller: CostController):
        self.cost_controller = cost_controller

    def calculate_cost(self, policy_data: LifeQuotation) -> Union[int, None]:
        """
        Method to calculate life insurance quotation.
        """
        # Logic to calculate life insurance quotation
        cost = self.cost_controller.query_life_cost(policy_data.age)
        cost *= (1 + self.cost_controller.query_life_cost_benefits(policy_data.benefits))
        return cost
