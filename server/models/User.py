from pydantic import BaseModel, Field
from datetime import datetime
from typing import Union

class UserIn(BaseModel):
    email: str = Field(...)
    password : str = Field(...)
    last_login: Union[datetime, None] = None
    #full_name: Union[str, None] = None

class UserOut(BaseModel):
  email: str = Field(...)

