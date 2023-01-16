from pydantic import BaseModel, Field
from datetime import datetime
from typing import Union

class UserIn(BaseModel):
  username: str = Field(...)
  email: str = Field(...)
  password : str = Field(...)
  last_login: Union[datetime, None]

class UserOut(BaseModel):
  email: Union[str, None]

