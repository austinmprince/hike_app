# source vensv/bin/activate
import sys

sys.path.append('../')
from typing import Union
from pydantic import BaseModel, Field, EmailStr
from pymongo import MongoClient
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
import settings

app = FastAPI()

client = MongoClient(settings.mongodb_uri, settings.port)
db = client.Users

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



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




