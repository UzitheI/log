from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
load_dotenv()

SQLALCHEMY_DATABSE_URL= f"mysql+pymysql://uziP:Kalpana77!@localhost:3306/user_schema"

engine=create_engine(
    SQLALCHEMY_DATABSE_URL,
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