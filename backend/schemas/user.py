from typing import Union
from pydantic import BaseModel
from datetime import datetime

class common(BaseModel):
    operation:str
    createdBy:datetime
    createdOn:str
    createdAt:datetime

class UserBase(common):
    id=int,
    username=str,
    password=str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id:int
    
    class config:
        orm_mode=True

class ItemBase(common):
    id:int
    item_name:str
    user_id:int

class ItemCreate(ItemBase):
    pass 

class Item(ItemBase):
    id:int
    
    class config:
        orm_mode:True

