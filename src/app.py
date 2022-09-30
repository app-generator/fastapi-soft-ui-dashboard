from fastapi import FastAPI

import models
from helpers.database import engine
from routers.auth.auth_routes import router as auth_router
from routers.product_routes import router as product_router
from routers.user_routes import router as user_router
from routers.sales_routes import router as sales_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True, reload=True)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(product_router)
app.include_router(sales_router)
