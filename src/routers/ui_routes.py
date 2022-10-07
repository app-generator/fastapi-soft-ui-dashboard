from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
import requests
from src.config import Settings

from src import models
from src import app
# from app import TEMPLATES

router = APIRouter(
    tags = ['User Interface']
)

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "../templates"))


@router.get("/")
def home(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("home/index.html", {"request" : request})

@router.get("/login")
def signin(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("accounts/login.html", {"request" : request})

@router.get("/register")
def register(request: Request, response_model=HTMLResponse):
    return TEMPLATES.TemplateResponse("accounts/register.html", {"request" : request})
