from pydantic import BaseModel, Field
from datetime import datetime

class Hike(BaseModel):
    hike_name: str = Field(...)
    date: datetime = Field(...)
    region: str = "Not specified"