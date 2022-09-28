from fastapi import FastAPI

from helpers.database import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True, reload=True)
