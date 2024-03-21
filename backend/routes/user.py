from fastapi import APIRouter, status, Depends,HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserDelete
from models.user import User, common
from db import getdb
from datetime import datetime

router = APIRouter()

def log_operation(db: Session, operation: str, created_by: str, user_id: int):

    log_entry = common(
        operation=operation,
        createdBy=created_by,
        createdAt=datetime.now(),
        user_id=user_id
    )
    db.add(log_entry)
    db.commit()

@router.post('/createUser', response_model=UserCreate, status_code=status.HTTP_202_ACCEPTED)
def create_user(req: UserCreate, db: Session = Depends(getdb)):
    new_user = User(username=req.username, password=req.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    log_operation(db, operation='User Created', created_by=req.createdBy, user_id=new_user.id)
    return new_user

@router.put('/updateUser/{user_id}', response_model=UserCreate, status_code=status.HTTP_200_OK)
def update_user(user_id: int, req: UserCreate, db: Session = Depends(getdb)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user.username = req.username
    user.password = req.password
    db.commit()
    log_operation(db, operation='User Updated', created_by=req.createdBy, user_id=user_id)
    return user

@router.delete('/deleteUser/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int,req:UserDelete, db: Session = Depends(getdb)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(user)
    db.commit()
    log_operation(db, operation='User Deleted', created_by=req.deleted_by, user_id=user_id)
    return None
