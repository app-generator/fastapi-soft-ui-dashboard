from fastapi import APIRouter, Request, Depends, status, Response, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

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

    token = request.headers.get('Authorization')

    if (token):
        return TEMPLATES.TemplateResponse("home/index.html", {"request" : request})

    return RedirectResponse(url=router.url_path_for('signin'))



@router.get("/login", status_code=status.HTTP_200_OK)
async def signin(request: Request, response_model=HTMLResponse):

    print('\n\n')
    print(request.method)
    print('\n\n')

    return TEMPLATES.TemplateResponse("accounts/login.html", {"request" : request})

@router.get("/register", status_code=status.HTTP_200_OK)
async def register(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("accounts/register.html", {"request" : request})
