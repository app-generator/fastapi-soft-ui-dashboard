from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

from src.routers.auth.auth_routes import router as auth_router
from src.routers.product_routes import router as product_router
from src.routers.user_routes import router as user_router
from src.routers.sales_routes import router as sales_router

app = FastAPI(debug=True, reload=True)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins
)

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))


@app.get("/")
def home(request: Request):
    return TEMPLATES.TemplateResponse("home/index.html", {"request" : request})


app.include_router(auth_router, prefix='/api')
app.include_router(user_router, prefix='/api')
app.include_router(product_router, prefix='/api')
app.include_router(sales_router, prefix='/api')
