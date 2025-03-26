from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models.base import Base
from app.routes import auth, class_router, notice, enrollment


app = FastAPI()

origins = [
    "http://localhost:3000",  # Ajusta esto al puerto de tu frontend
    # Agrega otros orígenes según sea necesario
    "http://127.0.0.1:3000"  # Agregar esta variante puede ayudar

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir solicitudes solo desde estos orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)


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
