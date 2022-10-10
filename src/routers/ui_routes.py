import requests as url_requests
from fastapi import APIRouter, Request, Depends, status, Response, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
import http3


import src.oauth2 as oauth2
from src.config import Settings
from src import models
from src import app


router = APIRouter(
    tags = ['User Interface']
)

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "../templates"))


@router.get("/", status_code=status.HTTP_200_OK)
async def home(request: Request, response_model=HTMLResponse):

    print ('\n\n\n')
    print ('HOME HEADERS')
    print (request.headers)
    print ('\n\n\n')

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
        headers = {
            'Authorization': f'Bearer {token}',
        }
        print (headers)
        # print (headers)
        redirect = RedirectResponse(url='/')
        redirect.status_code = 302
        redirect.headers.append('authorization', f'Bearer {token}')
        return redirect

    return TEMPLATES.TemplateResponse("accounts/login.html", {"request" : request})

@router.get("/register", status_code=status.HTTP_200_OK)
async def register(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("accounts/register.html", {"request" : request})
