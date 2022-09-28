from helpers.database import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    def __str__(self):
        return f"""
        id: {self.id}
        email: {self.email}
        username: {self.username}
        """

# products - id, name, description, price, currency
# sales - id, product_id, state, value, fee, currency, client

# from server.

# class Product(Base):
    # pass

    