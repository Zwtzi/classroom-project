import os
import jwt
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas import user as user_schema
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: user_schema.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        nombre=user.nombre,
        email=user.email,
        password_hash=hashed_password,
        tipo=user.tipo
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not pwd_context.verify(password, user.password_hash):
        return False
    token = jwt.encode({"user_id": user.id}, SECRET_KEY, algorithm="HS256")
    return token
