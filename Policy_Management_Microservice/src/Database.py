from abc import ABC, abstractmethod


class Database(ABC):
    """
    Abstract class to define a database.
    """
    
    @abstractmethod
    def connect(self):
        """
        Abstract method to connect the database.
        """
        pass

    @abstractmethod
    def get_motorcycle_cost(self, displacement: float) -> float:
        """
        Abstract method to get the cost of motorcycle insurance from the database.
        """
        pass

    @abstractmethod
    def get_life_base_cost(self, age: int) -> float:
        """
        Abstract method to get the base cost of life insurance from the database.
        """
        pass

    @abstractmethod
    def get_life_benefit_cost(self, benefit: str) -> float:
        """
        Abstract method to get the cost of additional benefits in a life insurance from the database.
        """
        pass

    @abstractmethod
    def get_car_cost(self, model: str, reference: str) -> float:
        """
        Abstract method to get the cost of car insurance from the database.
        """
        pass

    @abstractmethod
    def get_car_year_cost(self, year: int) -> float:
        """
        Abstract method to get the additional cost of car insurance based on the year from the database.
        """
        pass

    @abstractmethod
    def get_car_usage_cost(self, usage: str) -> float:
        """
        Abstract method to get the additional cost of car insurance based on the usage from the database.
        """
        pass

    @abstractmethod
    def get_displacement(self, plate: str) -> str:
        pass    


    @abstractmethod
    def get_car_info(self, plate: str) -> dict:
        pass