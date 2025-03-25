from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import enrollment as enrollment_schema
from app.services import enrollment as enrollment_service
from app.database import get_db

router = APIRouter(
    prefix="/enrollments",
    tags=["enrollments"]
)

@router.post("/", response_model=enrollment_schema.Enrollment)
def enroll_student(enrollment_in: enrollment_schema.EnrollmentCreate, db: Session = Depends(get_db)):
    return enrollment_service.enroll_student(db, enrollment_in)
