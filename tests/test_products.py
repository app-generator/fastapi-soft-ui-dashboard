import pytest
import src.schemas as schemas

from tests.conftest import authorized_client


def test_get_one_product(client, test_products):
    res = client.get(f"/api/products/{test_products[0].id}")
    product = schemas.Product(**res.json())

    assert product.id == test_products[0].id
    assert res.status_code == 200

def test_get_all_products(client, test_products):
    res = client.get("/api/products/")

    def validate(product):
        return schemas.ProductBase(**product)

    products_map = map(validate, res.json())
    products_list = list(products_map)

    assert len(res.json()) == len(test_products)
    assert res.status_code == 200
    

def test_create_product(authorized_client):
    res = authorized_client.post(
        "/api/products/", json={
            "name" : "Product0",
            "description" : "this is the description",
            "price" : 25.44,
            "currency" : "us dollar"
        }
    )
    assert res.status_code == 201


def test_unauthorized_create_product(client):
    res = client.post(
        "/api/products/", json={
            "name" : "Product0",
            "description" : "this is the description",
            "price" : 25.44,
            "currency" : "us dollar"
        }
    )
    assert res.status_code == 401


