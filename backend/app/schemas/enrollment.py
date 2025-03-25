from pydantic import BaseModel

class EnrollmentBase(BaseModel):
    alumno_id: int
    clase_id: int

class EnrollmentCreate(EnrollmentBase):
    pass

class Enrollment(EnrollmentBase):
    id: int

    class Config:
        orm_mode = True
