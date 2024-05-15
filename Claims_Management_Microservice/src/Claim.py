from datetime import datetime
from pydantic import BaseModel


class Claim(BaseModel):
    id: int
    name: str
    lastName: str
    email: str
    status: str
    details: str