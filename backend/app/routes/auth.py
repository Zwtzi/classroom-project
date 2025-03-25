from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import user as user_schema
from app.models.user import User
from app.services import auth as auth_service
from app.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register", response_model=user_schema.User)
def register(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = auth_service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    return auth_service.create_user(db=db, user=user)

@router.post("/login")
def login(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    token = auth_service.authenticate_user(db, email=user.email, password=user.password)
    if not token:
        raise HTTPException(status_code=400, detail="Credenciales inválidas")
    return {"access_token": token, "token_type": "bearer"}
