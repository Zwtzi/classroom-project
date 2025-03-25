from pydantic import BaseModel
from datetime import datetime

class NoticeBase(BaseModel):
    titulo: str
    contenido: str

class NoticeCreate(NoticeBase):
    clase_id: int

class Notice(NoticeBase):
    id: int
    fecha: datetime
    clase_id: int
    profesor_id: int

    class Config:
        orm_mode = True
