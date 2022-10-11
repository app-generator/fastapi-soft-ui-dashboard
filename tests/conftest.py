import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src import models
from src.app import app as root_app
from src.helpers.database import Base, get_db
from src.oauth2 import create_access_token


SQLITE_DATABASE_URL = 'sqlite:///./sql_app_test.db'

engine = create_engine(SQLITE_DATABASE_URL, connect_args={'check_same_thread': False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

client = TestClient(root_app)

@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()


    root_app.dependency_overrides[get_db] = override_get_db
    yield TestClient(root_app)

@pytest.fixture
def test_user(client):
    user_data = {
        "username" : "toasty",
        "email" : "toasty@gmail.com",
        "password" : "password123" 
    }

    res = client.post("/api/users/", json=user_data)

    assert res.status_code == 201

    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

@pytest.fixture
def token(test_user):
    return create_access_token({
        "user_id" : test_user.get('id'),
    })


@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client

@pytest.fixture
def test_products(session):
    products_data = [
        {
            "name" : "Product0",
            "description" : "this is a yellow product",
            "price" : 25.00,
            "currency" : "us dollar"  
        },
        {
            "name" : "Product1",
            "description" : "this is a red product",
            "price" : 55.99,
            "currency" : "us dollar"  
        },
        {
            "name" : "Product2",
            "description" : "this is a yellow product",
            "price" : 105.99,
            "currency" : "us dollar"  
        },   
    ]

    def create_product_model(product):
        return models.Product(**product)

    products_map = map(create_product_model, products_data)
    products = list(products_map)

    session.add_all(products)
    session.commit()

    products = session.query(models.Product).all()

    return products


@pytest.fixture
def test_sales(session, test_products):
    sales_data = [
        {
            "state": "Wisconsin",
            "value" : 100.44,
            "fee" : 60.24,
            "currency" : "us dollar",
            "client" : "Poggly Woggly",
            "product_id": test_products[0].id
        },
        {
            "state": "Florida",
            "value" : 90.12,
            "fee" : 69.99,
            "currency" : "us dollar",
            "client" : "Poggly Woggly",
            "product_id": test_products[1].id
        },
        {
            "state": "Florida",
            "value" : 290.44,
            "fee" : 10.24,
            "currency" : "us dollar",
            "client" : "Christopher Jones",
            "product_id": test_products[1].id
        },   
    ]

    def create_sale_model(sale):
        return models.Sale(**sale)

    sales_map = map(create_sale_model, sales_data)
    sales = list(sales_map)

    session.add_all(sales)
    session.commit()

    sales = session.query(models.Product).all()

    return sales