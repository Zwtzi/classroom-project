from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import notice as notice_schema
from app.services import notice as notice_service
from app.database import get_db

router = APIRouter(
    prefix="/notices",
    tags=["notices"]
)

@router.post("/", response_model=notice_schema.Notice)
def create_notice(notice_in: notice_schema.NoticeCreate, db: Session = Depends(get_db)):
    # Se debe obtener el profesor autenticado; aquí se usa un valor de ejemplo
    professor_id = 1  # Reemplazar con el ID del profesor autenticado
    return notice_service.create_notice(db, notice_in, professor_id)

@router.get("/class/{class_id}", response_model=list[notice_schema.Notice])
def get_notices(class_id: int, db: Session = Depends(get_db)):
    return notice_service.get_notices_by_class(db, class_id)
