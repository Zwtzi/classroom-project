from pydantic import BaseModel

class ClassBase(BaseModel):
    nombre: str
    descripcion: str
    codigo_grupo: str
    carrera: str
    cuatrimestre: int

class ClassCreate(ClassBase):
    pass

class Class(ClassBase):
    id: int
    profesor_id: int

    class Config:
        orm_mode = True
