from fastapi import status, HTTPException, Depends, APIRouter, Response
from helpers.database import get_db
from helpers.utils import hash
from sqlalchemy.orm import Session
from typing import List

import oauth2, models, schemas

router = APIRouter(
    prefix = "/products",
    tags = ['Products']
)

@router.get("/", response_model=List[schemas.Product])
def get_products(db: Session = Depends(get_db)):
    
    products = db.query(models.Product).all()

    if not products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product Was Not Found')

    return products


@router.get("/{id}", response_model=schemas.Product)
def get_product(id: int, db: Session = Depends(get_db)):

    product = db.query(models.Product).filter(models.Product.id == id).first()

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product was not found")

    return product


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Product)
def create_product(product: schemas.ProductBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    new_product = models.Product(**product.dict())

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    product_query = db.query(models.Product).filter(models.Product.id == id)

    product = product_query.first()

    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product was not found")

    product_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.Product)
def update_product(id: int, updated_product: schemas.ProductBase,  db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    product_query = db.query(models.Product).filter(models.Product.id == id)

    product = product_query.first()

    if product == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product was not found")

    product_query.update(updated_product.dict(), synchronize_session=False)

    db.commit()

    return product_query.first()

