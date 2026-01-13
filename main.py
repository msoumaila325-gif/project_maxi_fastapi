from fastapi import FastAPI
from database import db_dependency
import models
from routers import heroes_router, auth_router
from database import get_db, engine

app = FastAPI()  # minuscule

models.Base.metadata.create_all(bind=engine)

app.include_router(heroes_router.router)
app.include_router(auth_router.router)

