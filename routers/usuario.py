from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas

router = APIRouter(prefix="/Usuario", tags=["Usuario"])

@router.post("/")
def criar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.email == usuario.email).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    novo_usuario = models.Usuario(**usuario.dict())
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

@router.get("/")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()

@router.get("/{usuario_id}")
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return usuario

@router.put("/{usuario_id}")
def atualizar_usuario(usuario_id: int, usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    for key, value in usuario.dict().items():
        setattr(db_usuario, key, value)
    db.commit()
    return db_usuario

@router.delete("/{usuario_id}")
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    db.delete(usuario)
    db.commit()
    return {"ok": True}

# -------------------- LOGIN --------------------

@router.post("/login")
def login(email: str = Form(...), senha: str = Form(...), db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.email == email).first()

    if not usuario or usuario.senha != senha:
        raise HTTPException(status_code=401, detail="E-mail ou senha inválidos.")
    
    return {
        "mensagem": "Login realizado com sucesso",
        "id_usuario": usuario.id_usuario,
        "nome": usuario.nome,
        "tipo_usuario": usuario.tipo_usuario
    }
