from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models import enrollment as enrollment_model
from app.schemas import enrollment as enrollment_schema

def enroll_student(db: Session, enrollment_in: enrollment_schema.EnrollmentCreate):
    db_enrollment = enrollment_model.Enrollment(**enrollment_in.dict())
    db.add(db_enrollment)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise Exception("El alumno ya está inscrito en esta clase")
    db.refresh(db_enrollment)
    return db_enrollment
