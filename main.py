# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from routers import usuario, pet, adocao

app = FastAPI()

# Middleware CORS liberado para qualquer origem (público)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite qualquer origem
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cria as tabelas automaticamente no banco de dados
Base.metadata.create_all(bind=engine)

# Registra as rotas da API
app.include_router(usuario.router, tags=["Usuario"])
app.include_router(pet.router, tags=["Pet"])
app.include_router(adocao.router, tags=["Adocao"])

# Rota raiz opcional
@app.get("/")
def root():
    return {"mensagem": "API do Pet Resgate SP está online"}
