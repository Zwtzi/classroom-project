import enum
from sqlalchemy import Column, Integer, String, Enum
from app.models.base import Base
from sqlalchemy.orm import relationship

class UserTypeEnum(str, enum.Enum):
    alumno = "alumno"
    profesor = "profesor"

class User(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    tipo = Column(Enum(UserTypeEnum), nullable=False)
    
    # Relación con clases (si es profesor)
    clases = relationship("Class", back_populates="profesor")
