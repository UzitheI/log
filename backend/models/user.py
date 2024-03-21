from sqlalchemy import Boolean, Integer, String, ForeignKey,Column,DateTime
from datetime import datetime

from sqlalchemy.orm import relationship
from db import Base

class common(Base):
    __tablename__='logtable'
    log_id=Column(Integer,primary_key=True)
    operation=Column(String(255))
    createdBy=Column(String(344))
    createdAt=Column(DateTime)
    user_id=Column(Integer)

class User(common):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    username=Column(String(233))
    password=Column(String(234))
    log_id=Column(Integer, ForeignKey(common.log_id))

    
    


    
