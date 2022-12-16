from pydantic import BaseModel, Field
from typing import Union

class User(BaseModel):
    username: str = Field(...)
    email: str = Field(...)
    full_name: Union[str, None] = None

class UserInDB(User):
    hashed_password:str
