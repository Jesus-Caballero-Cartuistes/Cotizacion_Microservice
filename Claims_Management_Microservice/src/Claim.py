from datetime import datetime
from pydantic import BaseModel

class Claim(BaseModel):
    id: int
    status: str
    details: str
    date: datetime