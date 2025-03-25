from fastapi import FastAPI
from app.database import engine
from app.models.base import Base
from app.routes import auth
from app.routes import class_router
from app.routes import notice
from app.routes import enrollment

app = FastAPI()

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir routers de la API
app.include_router(auth.router)
app.include_router(class_router.router)
app.include_router(notice.router)
app.include_router(enrollment.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Classroom Project API"}
