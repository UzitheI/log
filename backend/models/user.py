from sqlalchemy import Boolean, Integer, String, ForeignKey,Column,DateTime
from datetime import datetime

from sqlalchemy.orm import relationship
from db import Base

class common(Base):
    __tablename__='logtable'
    operation=Column(String)
    createdBy=Column(DateTime)
    createdOn=Column(String)
    createdAt=Column(DateTime)

class User(common):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    username=Column(String,unique=True)
    password=Column(String)

class Item(common):
    
    __tablename__='items'
    id=Column(Integer,primary_key=True)
    item_name=str
    user_id=Column(Integer,ForeignKey('users.id'))
    users=relationship('Item',back_populates='items')
    
    


    
