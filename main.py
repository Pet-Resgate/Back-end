#inicializador
from fastapi import FastAPI
from database import Base, engine
from routers import usuario, pet, adocao

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(usuario.router, tags=["Usuario"])
app.include_router(pet.router, tags=["Pet"])
app.include_router(adocao.router, tags=["Adocao"])
