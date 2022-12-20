# source vensv/bin/activate
from models.User import UserIn, UserOut
from models.Hike import Hike
from typing import Union
from pydantic import BaseModel, Field, EmailStr
from pymongo import MongoClient
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder
from passlib.context import CryptContext
from settings import mongodb_uri, port, secret_key, algorithm, access_token_expire_minutes
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = MongoClient(mongodb_uri, port)
users_coll = client.Users.get_collection('users')
hike_coll = client.Hikes.get_collection('hikes')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/hike/{hike_id}")
def read_items(hike_id):
  return {"hike_id": hike_id, "q": q }

@app.post("/hike")
def create_hike(hike: Hike):
  
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
  current_user = users_coll.find_one({"email": user.email})
  if current_user:
    return current_user
  user.password = pwd_context.hash(user.password)
  user.last_login = datetime.now()
  db_user_obj = jsonable_encoder(user)
  users_coll.insert_one(db_user_obj)
  return user

@app.post("token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
  current_user = users_coll.find_one({form_data.email})
  if not current_user:
    raise HTTPException(status_code=400, detail="User not found in DB")
  hashed_password = pwd_context.hash(form_data.password)
  if not hashed_password == current_user.password:
    raise HTTPException(status_code=400, detail="Password is not correct")

  return {"access_token": "", "token_type": "bearer" }

def get_current_user(token: str = Depends(OAuth2PasswordBearer)):
  # user = decode_token(token)
  if not user:
    raise HTTPException(status_code=400, detail="User does not exist")
  return user

@app.get("/signup")
def dummy_func():
  print("signingup")


def _authenticate(email: str, password: str) -> UserOut:
  curr_user = _get_user(email)
  if not curr_user or not _validate_password(password, curr_user.password):
    return False
  return curr_user
 

def _validate_password(plan_password, hashed_password):
  return pwd_context.hash(plan_password) == hashed_password

def _get_user(email) -> UserIn:
  curr_user = users_coll.find_one({"email": email})
  return curr_user


