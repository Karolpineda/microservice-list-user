# app/main.py
from fastapi import FastAPI
from app.models import Base
from app.controllers.user import router as user_router


app = FastAPI()

# Incluir el router de usuario
app.include_router(user_router)