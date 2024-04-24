from pydantic import BaseModel

class AuthenticationRequest(BaseModel):
    id_number: int
    name: str
    last_name: str
    expiration_date: str