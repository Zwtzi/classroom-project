from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.models.base import Base
from sqlalchemy.orm import relationship

class Class(Base):
    __tablename__ = "clases"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text)
    codigo_grupo = Column(String(20), unique=True, nullable=False)
    carrera = Column(String(100), nullable=False)
    cuatrimestre = Column(Integer, nullable=False)
    profesor_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    
    profesor = relationship("User", back_populates="clases")
    avisos = relationship("Notice", back_populates="clase", cascade="all, delete")
