from os import name
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

# from app import TEMPLATES

router = APIRouter(
    tags = ['User Interface']
)

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "../templates"))


@router.get("/")
def home(request: Request):
    return TEMPLATES.TemplateResponse("home/index.html", {"request" : request})


@router.get("/login")
def login(request: Request):
    return TEMPLATES.TemplateResponse("accounts/login.html", {"request" : request})
