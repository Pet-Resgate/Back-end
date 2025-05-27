from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas

router = APIRouter(prefix="/Adocao", tags=["Adocao"])

@router.post("/", response_model=schemas.Adocao)
def criar_adocao(adocao: schemas.AdocaoCreate, db: Session = Depends(get_db)):
    pet_adotado = db.query(models.Adocao).filter(models.Adocao.id_pet == adocao.id_pet).first()
    if pet_adotado:
        raise HTTPException(status_code=400, detail="Este pet já foi adotado.")
    nova_adocao = models.Adocao(**adocao.dict())
    db.add(nova_adocao)
    db.commit()
    db.refresh(nova_adocao)
    return nova_adocao

@router.get("/", response_model=list[schemas.Adocao])
def listar_adocoes(db: Session = Depends(get_db)):
    return db.query(models.Adocao).all()

@router.get("/{adocao_id}", response_model=schemas.Adocao)
def obter_adocao(adocao_id: int, db: Session = Depends(get_db)):
    adocao = db.query(models.Adocao).filter(models.Adocao.id_adocao == adocao_id).first()
    if not adocao:
        raise HTTPException(status_code=404, detail="Adoção não encontrada.")
    return adocao

@router.delete("/{adocao_id}")
def deletar_adocao(adocao_id: int, db: Session = Depends(get_db)):
    adocao = db.query(models.Adocao).filter(models.Adocao.id_adocao == adocao_id).first()
    if not adocao:
        raise HTTPException(status_code=404, detail="Adoção não encontrada.")
    db.delete(adocao)
    db.commit()
    return {"ok": True}
