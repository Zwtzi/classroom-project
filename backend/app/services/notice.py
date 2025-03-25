from sqlalchemy.orm import Session
from app.models import notice as notice_model
from app.schemas import notice as notice_schema

def create_notice(db: Session, notice_in: notice_schema.NoticeCreate, professor_id: int):
    db_notice = notice_model.Notice(**notice_in.dict(), profesor_id=professor_id)
    db.add(db_notice)
    db.commit()
    db.refresh(db_notice)
    return db_notice

def get_notices_by_class(db: Session, class_id: int):
    return db.query(notice_model.Notice).filter(notice_model.Notice.clase_id == class_id)\
             .order_by(notice_model.Notice.fecha.desc()).all()
