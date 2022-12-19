# source vensv/bin/activate
from models.User import UserIn, UserOut
from typing import Union
from pydantic import BaseModel, Field, EmailStr
from pymongo import MongoClient
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.encoders import jsonable_encoder
from passlib.context import CryptContext
from settings import mongodb_uri, port
from datetime import datetime



app = FastAPI()

client = MongoClient(mongodb_uri, port)
users_db = client.Users

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hike/{hike_id}")
def read_items(hike_id: int, q:Union[str, None] = None):
    return {"hike_id": hike_id, "q": q }

@app.post("/hike")
def create_hike():
    return {"hike created!"}

@app.patch("/hike/{hike_id}")
def update_hike(hike_id: int):
    return {"hike_id updated": hike_id}

@app.delete("/hike/{hike_id}")
def delete_hike(hike_id: int):
    return {"deleting hike_id": hike_id}

@app.get("/hikes")
def read_hikes(token:str = Depends(oauth2_scheme)):
    return token

@app.post("/signup", response_model=UserOut)
def signup_user(user: UserIn):
  user_collection = users_db.get_collection('users')

  current_user = user_collection.find_one({"email": user.email})
  if current_user:
    return None
  user.password = pwd_context.hash(user.password)
  user.last_login = datetime.now()
  db_user_obj = jsonable_encoder(user)
  user_collection.insert_one(db_user_obj)
  return user


