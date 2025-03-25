from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from app.models.base import Base
from sqlalchemy.orm import relationship

class Enrollment(Base):
    __tablename__ = "inscripciones"
    
    id = Column(Integer, primary_key=True, index=True)
    alumno_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    clase_id = Column(Integer, ForeignKey("clases.id"), nullable=False)
    
    __table_args__ = (UniqueConstraint('alumno_id', 'clase_id', name='unique_enrollment'), )
    
    alumno = relationship("User")
    clase = relationship("Class")
