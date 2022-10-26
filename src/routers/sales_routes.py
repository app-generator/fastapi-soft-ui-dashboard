# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from fastapi import status, HTTPException, Depends, APIRouter, Response
from typing import List
from sqlalchemy.orm import Session

import src.schemas as schemas
import src.models as models
import src.oauth2 as oauth2
from src.helpers.database import get_db
from src.helpers.utils import hash


router = APIRouter(
    prefix = "/api/sales",
    tags = ['Sales']
)

@router.get("/", response_model=List[schemas.Sale])
async def get_sales(db: Session = Depends(get_db)):
    
    sales = db.query(models.Sale).all()

    if not sales:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sale Was Not Found")

    return sales


@router.get("/{id}", response_model=schemas.Sale)
async def get_sale(id: int, db: Session = Depends(get_db)):

    sale = db.query(models.Sale).filter(models.Sale.id == id).first()

    if not sale:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sale was not found")

    return sale


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Sale)
async def create_sale(sale: schemas.SaleBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    new_sale = models.Sale(**sale.dict())

    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)

    return new_sale


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_sale(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    sale_query = db.query(models.Sale).filter(models.Sale.id == id)

    sale = sale_query.first()

    if sale == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sale was not found")

    sale_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.Sale)
async def update_sale(id: int, updated_sale: schemas.SaleBase,  db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    sale_query = db.query(models.Sale).filter(models.Sale.id == id)

    sale = sale_query.first()


    if sale == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sale was not found")


    sale_query.update(updated_sale.dict(), synchronize_session=False)

    db.commit()

    return sale_query.first()
