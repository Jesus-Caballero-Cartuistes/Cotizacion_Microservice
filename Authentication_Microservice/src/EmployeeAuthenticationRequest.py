from pydantic import BaseModel


class EmployeeAuthenticationRequest(BaseModel):
    user: str
    password: str

