from pydantic import BaseModel, EmailStr
from enum import Enum

class UserTypeEnum(str, Enum):
    alumno = "alumno"
    profesor = "profesor"

class UserBase(BaseModel):
    nombre: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    tipo: UserTypeEnum

class User(UserBase):
    id: int
    tipo: UserTypeEnum

    class Config:
        orm_mode = True
