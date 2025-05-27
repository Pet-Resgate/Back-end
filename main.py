#inicializador
from fastapi import FastAPI
from database import Base, engine
from routers import usuario, pet, adocao

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(usuario.router, prefix="/Usuario", tags=["Usuario"])
app.include_router(pet.router, prefix="/Pets", tags=["Pet"])
app.include_router(adocao.router, prefix="/Adocao", tags=["Adocao"])
