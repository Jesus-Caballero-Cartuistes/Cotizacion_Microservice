
from fastapi import APIRouter
from datetime import datetime, timedelta
from Policy_Management_Microservice.src.MongoDB import MongoDB
from Policy_Management_Microservice.src.Quotation import *
from Policy_Management_Microservice.src.Policy import *

policy_router = APIRouter()
mongoDB = MongoDB()
cost_controller = CostControllerImpl(mongoDB)


@policy_router.get("/")
async def root():
    return {"Microservice": "Quotation Management"}


@policy_router.post("/create_motorcycle_policy/")
async def create_motorcycle_policy(moto_insurance: MotorcyclePolicy):
    # Create a MotorcyclePolicy object with the received data
    policy_dict = moto_insurance.model_dump()
    policy_dict["cost"] = MotorcycleQuotation(
        cost_controller).calculate(moto_insurance)
    policy_dict["start_date"] = datetime.now().date()
    policy_dict["end_date"] = datetime.now().date() + timedelta(days=365)
    return policy_dict


@policy_router.post("/create_car_policy/")
async def create_car_policy(car_insurance: CarPolicy):
    # Create a CarPolicy object with the received data
    policy_dict = car_insurance.model_dump()
    policy_dict["cost"] = CarQuotation(
        cost_controller).calculate(car_insurance)
    policy_dict["start_date"] = datetime.now().date()
    policy_dict["end_date"] = datetime.now().date() + timedelta(days=365)
    return policy_dict


@policy_router.post("/create_life_policy/")
async def create_life_policy(life_insurance: LifePolicy):
    # Create a LifePolicy object with the received data
    policy_dict = life_insurance.model_dump()
    policy_dict["cost"] = LifeQuotation(
        cost_controller).calculate(life_insurance)
    policy_dict["start_date"] = datetime.now().date()
    policy_dict["end_date"] = datetime.now().date() + timedelta(days=365)
    return policy_dict
