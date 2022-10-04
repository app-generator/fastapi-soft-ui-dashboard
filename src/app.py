from fastapi import FastAPI

from src.routers.auth.auth_routes import router as auth_router
from src.routers.product_routes import router as product_router
from src.routers.user_routes import router as user_router
from src.routers.sales_routes import router as sales_router

app = FastAPI(debug=True, reload=True)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(product_router)
app.include_router(sales_router)
