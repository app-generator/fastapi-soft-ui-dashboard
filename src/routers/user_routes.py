# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List

import src.schemas as schemas
import src.models as models
# import src.oauth2 as oauth2
from src.helpers.database import get_db
from src.helpers.utils import hash


router = APIRouter(
    prefix = "/api/users",
    tags = ['Users']
)

@router.get('/', response_model=List[schemas.UserOut])
async def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()

    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User Was Not Found')

    return users

@router.get('/{id}', response_model=schemas.UserOut)
async def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User Was Not Found')

    return user


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    hashed_passord = hash(user.password)
    user.password  = hashed_passord

    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

