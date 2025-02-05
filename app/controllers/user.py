from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.user import get_users
from app.database import get_db

router = APIRouter()

# Ruta Health para verificar si el microservicio está activo
@router.get("/health")
def health_check():
    return {"status": "Microservice Users is up and running"}

# Ruta para listar todos los usuarios
@router.get("/users")
def list_users(db: Session = Depends(get_db)):
    users = get_users(db)
    
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    
    return {"users": users}
