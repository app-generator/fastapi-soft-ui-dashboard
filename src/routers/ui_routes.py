# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from fastapi import APIRouter, Request, Depends, status, Response, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
import http3

from sqlalchemy.orm import Session
from src.helpers.database import get_db

from src import app
import src.oauth2 as oauth2
from src.config import Settings
from src import models, schemas


router = APIRouter(
    tags = ['User Interface']
)

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "../templates"))


@router.get("/", status_code=status.HTTP_200_OK)
@oauth2.auth_required
def home(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("home/index.html", {"request" : request})


@router.get("/login", status_code=status.HTTP_200_OK)
async def signin(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("accounts/login.html", {"request" : request})


@router.post("/login", status_code=status.HTTP_200_OK)
async def signin(request: Request):
    form = await request.form()
    form = form._dict
    form.pop('login')
    
    base_url = request.base_url
    login_url = app.auth_router.url_path_for('login')
    request_url = base_url.__str__() + login_url.__str__()[1:]

    http3client = http3.AsyncClient()
    response = await http3client.post(request_url, data=form)

    if (response.status_code==200):
        data = response.json()
        token = data['access_token']

        redirect = RedirectResponse(url=router.url_path_for('home'))
        redirect.status_code = 302
        redirect.set_cookie('Authorization', f'Bearer {token}')
        return redirect

    if (response.status_code==500):
        msg = 'Issue with the Server'

    get_users_url = app.user_router.url_path_for('get_users')
    users_request_url = base_url.__str__() + get_users_url.__str__()[1:]
    http3client2 = http3.AsyncClient()
    test_response = await http3client2.get(users_request_url)
    test_users = test_response.json()
    msg = 'Wrong User or Password'
    for test_user in test_users:
        print (test_user)
        if form['username']==test_user['email']:
            msg = 'Password is Wrong'
        
    return TEMPLATES.TemplateResponse("accounts/login.html", {"request" : request, "msg" : msg})


@router.get("/register", status_code=status.HTTP_200_OK)
async def register(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("accounts/register.html", {"request" : request})


@router.post("/register", status_code=status.HTTP_200_OK)
async def register(request: Request, response_model=HTMLResponse):
    form = await request.form()
    form = form._dict
    form.pop('register')

    #validates the form data
    new_user = models.User(**form)

    base_url = request.base_url
    create_user_url = app.user_router.url_path_for('create_user')
    request_url = base_url.__str__() + create_user_url.__str__()[1:]
    http3client = http3.AsyncClient()
    response = await http3client.post(request_url, json=form)

    if (response.status_code==201):
        redirect = RedirectResponse(url=router.url_path_for('signin'))
        # default redirect is 307, which maintains the reused 'POST' indictation, 302 changes it to 'GET'
        redirect.status_code = 302
        return redirect

    msg = 'Something Went Wrong'
    if (response.status_code==500):
        msg = 'Issue with the Server'

    get_users_url = app.user_router.url_path_for('get_users')
    users_request_url = base_url.__str__() + get_users_url.__str__()[1:]
    http3client2 = http3.AsyncClient()
    test_response = await http3client2.get(users_request_url)
    test_users = test_response.json()
    for test_user in test_users:
        if new_user.email==test_user['email']:
            msg = 'Email Already Registered'
        if new_user.username == test_user['username']:
            msg = 'Username Already Registered '

    return TEMPLATES.TemplateResponse("accounts/register.html", {"request" : request, "msg" : msg })

@router.get('/tables', status_code=status.HTTP_200_OK)
@oauth2.auth_required
def tables(request: Request):
    return TEMPLATES.TemplateResponse("home/tables.html", {"request" : request})


@router.get('/billing', status_code=status.HTTP_200_OK)
@oauth2.auth_required
def billing(request: Request):
    return TEMPLATES.TemplateResponse("home/billing.html", {"request" : request})

@router.get('/virtual-reality', status_code=status.HTTP_200_OK)
@oauth2.auth_required
def virtual_reality(request: Request):
    return TEMPLATES.TemplateResponse("home/virtual-reality.html", {"request" : request})



@router.get('/profile', status_code=status.HTTP_200_OK)
@oauth2.auth_required
def profile(request: Request):
    return TEMPLATES.TemplateResponse("home/profile.html", {"request" : request})



@router.get('/rtl', status_code=status.HTTP_200_OK)
@oauth2.auth_required
def rtl(request: Request):
    return TEMPLATES.TemplateResponse("home/rtl.html", {"request" : request})
