from fastapi import APIRouter, status, Depends,HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from models.user import User,common
from db import sessionLocal,engine, getdb
from pydantic import BaseModel
router=APIRouter()

@router.post('/createUser',response_model=UserCreate,status_code=status.HTTP_202_ACCEPTED)
def create_user(req:UserCreate,db:Session=Depends(getdb)):
    users=User(
        operation='User Created',
        createdBy=req.createdBy,
        createdOn=req.createdOn,
        createdAt=req.createdAt,
        id=req.id,
        username=req.username,
        password=req.password
    )
    logtable=common(
        operation='User Created',
        createdBy=req.createdBy,
        createdOn=req.createdOn,
        createdAt=req.createdAt
    )
    db.add(logtable)
    db.add(users)
    db.commit()
    db.refresh()

    return User


