from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import  class_schema
from app.services import  class_service
from app.database import get_db

router = APIRouter(
    prefix="/classes",
    tags=["classes"]
)

@router.post("/", response_model=class_schema.Class)
def create_class(class_in: class_schema.ClassCreate, db: Session = Depends(get_db)):
    # Aquí se debería obtener el usuario autenticado (profesor)
    professor_id = 1  # Ejemplo; reemplazar por el ID del profesor autenticado
    return class_service.create_class(db, class_in, professor_id)

@router.get("/", response_model=list[class_schema.Class])
def list_classes(db: Session = Depends(get_db)):
    return class_service.get_classes(db)

# Se pueden agregar endpoints adicionales para actualizar o eliminar clases
