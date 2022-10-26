# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from src.helpers.database import Base

from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    currency = Column(String, nullable=False)

class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, nullable=False)
    state = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    fee = Column(Float, nullable=False)
    currency = Column(String, nullable=False)
    client = Column(String, nullable=False)
    
    product_id = Column(String, ForeignKey("products.id", ondelete="CASCADE"))
    product = relationship("Product")
    