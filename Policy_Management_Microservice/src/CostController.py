from abc import ABC, abstractmethod
from Policy_Management_Microservice.src.MongoDB import MongoDB


class CostController(ABC):
    """
    Interface for querying insurance cost from the database.
    """

    @abstractmethod
    def query_motorcycle_cost(self, displacement: float) -> float:
        """
        Abstract method to query motorcycle insurance cost from the database.
        """
        pass

    @abstractmethod
    def query_life_cost(self, age: int) -> float:
        """
        Abstract method to query life insurance cost from the database.
        """
        pass

    @abstractmethod
    def query_life_cost_benefits(self, benefits: dict) -> float:
        """
        Abstract method to query additional benefits cost in a life insurance from the database.
        """
        pass

    @abstractmethod
    def query_car_cost(self, model: str, reference: str) -> float:
        """
        Abstract method to query car insurance cost from the database.
        """
        pass

    @abstractmethod
    def query_additional_car_cost(self, year: int, status: str, usage: str) -> float:
        """
        Abstract method to query additional cost of car insurance from the database.
        """
        pass


class CostControllerImpl(CostController):
    """
    Implementation of querying insurance cost from the database.
    """

    def __init__(self, database_impl: MongoDB):
        self.database_impl = database_impl

    def query_motorcycle_cost(self, displacement: float) -> float:
        """
        Method to query motorcycle insurance cost from the database.
        """
        return self.database_impl.get_motorcycle_cost(displacement)

    def query_life_cost(self, age: int) -> float:
        """
        Method to query life insurance cost from the database.
        """
        return self.database_impl.get_life_base_cost(age)

    def query_life_cost_benefits(self, benefits: dict) -> float:
        """
        Method to query additional benefits cost in a life insurance from the database.
        """
        total_benefits_multiplier = 0
        for benefit, state in benefits.items():
            if state:
                benefit_multiplier = self.database_impl.get_life_benefit_cost(
                    benefit)
                total_benefits_multiplier += benefit_multiplier
        return total_benefits_multiplier

    def query_car_cost(self, model: str, reference: str) -> float:
        """
        Method to query car insurance cost from the database.
        """
        return self.database_impl.get_car_cost(model, reference)

    def query_additional_car_cost(self, year: int, status: str, usage: str) -> float:
        """
        Method to query additional cost of car insurance from the database.
        """
        total_additional_multiplier = self.database_impl.get_car_year_cost(
            year)
        total_additional_multiplier += self.database_impl.get_car_status_cost(
            status)
        total_additional_multiplier += self.database_impl.get_car_usage_cost(
            usage)
        return total_additional_multiplier
