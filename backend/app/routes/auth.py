from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import user as user_schema
from app.services import auth as auth_service
from app.database import get_db
from pydantic import BaseModel
from app.services.auth import create_user, get_user_by_email

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/register", response_model=user_schema.User)
def register(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = auth_service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    
    new_user = auth_service.create_user(db=db, user=user)

    # Convertir el modelo de SQLAlchemy a Pydantic antes de devolverlo
    return user_schema.User(
        id=new_user.id,
        nombre=new_user.nombre,
        email=new_user.email,
        tipo=new_user.tipo
    )

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    token = auth_service.authenticate_user(db, request.email, request.password)
    
    if not token:
        user = auth_service.get_user_by_email(db, request.email)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    return {"access_token": token, "token_type": "bearer"}
