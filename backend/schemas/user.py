from typing import Union
from pydantic import BaseModel
from datetime import datetime

class common(BaseModel):
    log_id:int
    operation:str
    createdBy:str
    createdAt:datetime
    user_id:int

class UserBase(common):
    id:int
    username:str
    password:str

class UserCreate(UserBase):
    pass

class UserDelete(UserBase):
    deleted_by:str

class User(UserBase):
    id:int
    
    class config:
        orm_mode=True


