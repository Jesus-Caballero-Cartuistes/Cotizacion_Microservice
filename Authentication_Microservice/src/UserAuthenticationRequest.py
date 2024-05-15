from pydantic import BaseModel

class UserAuthenticationRequest(BaseModel):
    identification: int
    expDate: str
    first_name: str
    last_name: str
    cost: int
    start_date: str
    end_date: str
    email: str
    age: int
    benefits: dict
