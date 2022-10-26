# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from src.routers.auth.auth_routes import router as auth_router
from src.routers.product_routes import router as product_router
from src.routers.user_routes import router as user_router
from src.routers.sales_routes import router as sales_router
from src.routers.ui_routes import router as ui_router

app = FastAPI(debug=True, reload=True)
app.mount("/static", StaticFiles(directory="src/static"), name="static")

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins 
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(product_router)
app.include_router(sales_router)
app.include_router(ui_router)
