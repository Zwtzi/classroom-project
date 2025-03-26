from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas import user as user_schema
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from .. import models
from app.schemas.user import UserCreate
from app.schemas.user import UserTypeEnum

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET_KEY = "tu_clave_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        return None  # Usuario no encontrado

    if not verify_password(password, user.password_hash):
        return None  # Contraseña incorrecta

    return create_access_token({"sub": user.email})  # Devuelve el token si es válido

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        nombre=user.nombre,
        email=user.email,
        password_hash=hashed_password,
        tipo=UserTypeEnum(user.tipo)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_jwt_token(user: models.user):
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return create_access_token({"sub": user.email}, expires_delta)
