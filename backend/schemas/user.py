from typing import Union
from pydantic import BaseModel
from datetime import datetime

class common(BaseModel):
    operation:str
    createdBy:str
    createdOn:str
    createdAt:datetime

class UserBase(common):
    id:int
    username:str
    password:str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id:int
    
    class config:
        orm_mode=True


