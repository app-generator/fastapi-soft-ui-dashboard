import pytest
from src import schemas
from jose import jwt
from src.config import settings
from tests.conftest import test_user

def test_create_user(client):
    res = client.post("api/users/", json={
        "username" : "Testy",
        "email" : "testy@gmail.com",
        "password" : "password123" 
    })

    new_user = schemas.UserOut(**res.json())
    assert new_user.email == 'testy@gmail.com'
    assert res.status_code == 201

def test_login_user(client, test_user):
    res = client.post("/api/auth/login", data={
        "username" : test_user['email'],
        "password" : test_user['password']
    })

    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    
    id = payload.get('user_id')

    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200



