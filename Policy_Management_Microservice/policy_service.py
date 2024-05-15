
from fastapi import APIRouter, HTTPException
from datetime import datetime, timedelta
from Policy_Management_Microservice.src.MongoDB import MongoDB
from Policy_Management_Microservice.src.QuotationMethods import *
from Policy_Management_Microservice.src.Quotation import *

policy_router = APIRouter()
mongoDB = MongoDB()
cost_controller = CostControllerImpl(mongoDB)


@policy_router.get("/")
async def root():
    return {"Microservice": "Quotation Management"}


@policy_router.get("/create_motorcycle_policy/{plate}")
async def create_motorcycle_policy(plate: str):
    # Create a MotorcyclePolicy object with the received data
    quotation_dict = {}
    quotation_dict["plate"] = plate
    displacement = cost_controller.query_motorcycle_displacement(plate)
    quotation_dict["displacement"] = displacement
    quotation_dict["cost"] = MotorcycleQuotationMethods(
        cost_controller).calculate_cost(displacement)
    quotation_dict["start_date"] = datetime.now().date()
    quotation_dict["end_date"] = datetime.now().date() + timedelta(days=365)
    if not displacement:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return quotation_dict


@policy_router.get("/create_car_policy/{plate}")
async def create_car_policy(plate: str):
    # Create a CarPolicy object with the received data
    quotation_dict = {}
    quotation_dict["plate"] = plate
    vehicle = CarQuotationMethods(cost_controller).get_car_info(plate)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    quotation_dict["reference"] = vehicle["reference"]
    quotation_dict["model"] = vehicle["model"]
    quotation_dict["year"] = vehicle["year"]
    quotation_dict["usage"] = vehicle["usage"]
    carPolicy = CarQuotation(
        plate=plate, reference=vehicle["reference"], model=vehicle["model"], year=vehicle["year"], usage=vehicle["usage"])
    quotation_dict["cost"] = CarQuotationMethods(
        cost_controller).calculate_cost(carPolicy)
    quotation_dict["start_date"] = datetime.now().date()
    quotation_dict["end_date"] = datetime.now().date() + timedelta(days=365)
    return quotation_dict


@policy_router.post("/create_life_policy/")
async def create_life_policy(life_quotation : LifeQuotation):
    # Create a LifePolicy dict with the received data
    quotation_dict = life_quotation.model_dump()
    quotation_dict["cost"] = LifeQuotationMethods(
        cost_controller).calculate_cost(life_quotation)
    quotation_dict["start_date"] = datetime.now().date()
    quotation_dict["end_date"] = datetime.now().date() + timedelta(days=365)
    return quotation_dict
