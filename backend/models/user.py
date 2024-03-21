from sqlalchemy import Boolean, Integer, String, ForeignKey,Column,DateTime
from datetime import datetime

from sqlalchemy.orm import relationship
from db import Base

class common(Base):
    __tablename__='logtable'
    log_id=Column(Integer, primary_key=True)
    operation=Column(String)
    createdBy=Column(String)
    createdOn=Column(DateTime)
    createdAt=Column(String)

class User(common):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    username=Column(String,unique=True)
    password=Column(String)
    log_id=Column(Integer, ForeignKey(common.log_id))

    
    


    
