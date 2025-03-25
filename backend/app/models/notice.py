from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.models.base import Base
from sqlalchemy.orm import relationship

class Notice(Base):
    __tablename__ = "avisos"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    contenido = Column(Text, nullable=False)
    fecha = Column(DateTime(timezone=True), server_default=func.now())
    clase_id = Column(Integer, ForeignKey("clases.id"), nullable=False)
    profesor_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    
    clase = relationship("Class", back_populates="avisos")
    # Se puede definir una relación con el profesor si es necesario:
    profesor = relationship("User")
