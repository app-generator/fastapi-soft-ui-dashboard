import pytest

import src.schemas as schemas

def test_get_one_sale(client, test_sales):
    res = client.get(f"/api/sales/{test_sales[0].id}")
    sale = schemas.Sale(**res.json())

    assert sale.id == test_sales[0].id
    assert res.status_code == 200


def test_get_all_sales(client, test_sales):
    res = client.get("/api/sales/")

    def validate(sale):
        return schemas.SaleBase(**sale)

    sales_map = map(validate, res.json())
    sales_list = list(sales_map)

    assert len(res.json()) == len(test_sales)
    assert res.status_code == 200
    

def test_create_sale(authorized_client, test_products):
    res = authorized_client.post(
        "/api/sales/", json={
            "state": "Florida",
            "value" : 100.44,
            "fee" : 60.24,
            "currency" : "us dollar",
            "client" : "Poggly Woggly",
            "product_id": test_products[0].id
        }
    )
    assert res.status_code == 201

def test_unauthorized_create_sale(client, test_products):
    res = client.post(
        "/api/sales/", json={
            "state": "Florida",
            "description": "state is updated",
            "value" : 100.44,
            "fee" : 60.24,
            "currency" : "us dollar",
            "client" : "Poggly Woggly",
            "product_id": test_products[0].id
        }
    )
    assert res.status_code == 401
