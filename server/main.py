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
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

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
pwd_context = CryptContext(schemes=["bcrypt"])



def get_current_user(token: str = Depends(oauth2_scheme)):
  not_valid_exception = HTTPException(status_code=401, detail="User is not allowed to see this data")
  try:
    payload = jwt.decode(token, secret_key, algorithm)
    username = payload.get('sub')
    if not username:
      raise not_valid_exception
  except JWTError:
    raise not_valid_exception
  user = _get_user(username)
  if not user:
    raise not_valid_exception
  return user

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.get("/hike/{hike_id}", response_model=Hike)
def get_hike_details(hike_id: int, user:UserIn = Depends(get_current_user)):
  hike = hike_coll.find_one({"hike_id": hike_id})
  if not hike:
    raise HTTPException(status_code=400, detail="Hike not found in DB")
  return hike

@app.post("/hike", response_model=Hike)
def create_hike(hike: Hike, user:UserIn = Depends(get_current_user)):
  hike.username = user.username
  db_hike = jsonable_encoder(hike)
  try:
    hike_coll.insert_one(db_hike)
    return hike
  except Exception as e:
    raise HTTPException(status_code=500, detail="Hike could not be inserted into DB")

@app.patch("/hike/{hike_id}")
def update_hike(hike_id: int):
  return {"hike_id updated": hike_id}

@app.delete("/hike/{hike_id}")
def delete_hike(hike_id: int):
  return {"deleting hike_id": hike_id}

@app.get("/hikes/{username}")
def read_hikes(username: str, user:UserIn = Depends(get_current_user)):
  hikes = hike_coll.find({"username": username})
  if not hikes:
    return None
  return hikes

@app.post("/signup", response_model=UserOut)
def signup_user(user: UserIn):
  current_user = users_coll.find_one({"username": user.username})
  if current_user:
    return current_user
  user.password = pwd_context.hash(user.password)
  user.last_login = datetime.now()
  db_user_obj = jsonable_encoder(user)
  try:
    users_coll.insert_one(db_user_obj)
    return user
  except Exception as e:
    raise HTTPException(status_code=500, detail="User could not be inserted into DB correctly")

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
  user = _authenticate(form_data.username, form_data.password)
  if not user:
    raise HTTPException(status_code=400, detail="User not found in DB")
  print(access_token_expire_minutes)

  access_token_expires = timedelta(minutes=int(access_token_expire_minutes))
  token = create_access_token({"sub": user.username}, expires_delta=access_token_expires)
  return {"access_token": token, "token_type": "bearer" }



@app.get("/users/me", response_model=UserOut)
def read_users_me(current_user: UserOut = Depends(get_current_user)):
  return current_user

def _authenticate(username: str, password: str) -> UserOut:
  curr_user = _get_user(username)
  if not curr_user or not _validate_password(password, curr_user.password):
    return False
  return curr_user
 

def _validate_password(plan_password, hashed_password):
  pwd_context.verify(plan_password, hashed_password)
  return pwd_context.verify(plan_password,hashed_password)

def _get_user(username: str):
  curr_user = users_coll.find_one({"username": username})
  if not curr_user:
    return None
  return UserIn(**curr_user)

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
  print(data, expires_delta)
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.now + timedelta(minutes=15)
  to_encode.update({'exp': expire})
  encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
  return encoded_jwt
  



# if __name__ == "__main__":
#   uvicorn.run(app, host="0.0.0.0", port=8000)






