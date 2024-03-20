from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os

SQLALCHEMY_DATABSE_URL='mysql+pymysql://uziP:K@lapana77@localhost:3306/userName'

engine=create_engine(
    SQLALCHEMY_DATABSE_URL,connect_args={'check_same_thread':False},
    echo=True
)
sessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()

def getdb():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()