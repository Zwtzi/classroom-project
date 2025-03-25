from sqlalchemy.orm import Session
from app.models import class_model
from app.schemas import class_schema

def create_class(db: Session, class_in: class_schema.ClassCreate, professor_id: int):
    db_class = class_model.Class(**class_in.dict(), profesor_id=professor_id)
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

def get_classes(db: Session):
    return db.query(class_model.Class).all()
