from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas

router = APIRouter(prefix="/Pet", tags=["Pet"])

@router.post("/")
def criar_pet(pet: schemas.PetCreate, db: Session = Depends(get_db)):
    novo_pet = models.Pet(**pet.dict())
    db.add(novo_pet)
    db.commit()
    db.refresh(novo_pet)
    return novo_pet

@router.get("/")
def listar_pets(db: Session = Depends(get_db)):
    return db.query(models.Pet).all()

@router.get("/{pet_id}")
def obter_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(models.Pet).filter(models.Pet.id_pet == pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado.")
    return pet

@router.put("/{pet_id}")
def atualizar_pet(pet_id: int, pet: schemas.PetCreate, db: Session = Depends(get_db)):
    db_pet = db.query(models.Pet).filter(models.Pet.id_pet == pet_id).first()
    if not db_pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado.")
    for key, value in pet.dict().items():
        setattr(db_pet, key, value)
    db.commit()
    return db_pet

@router.delete("/{pet_id}")
def deletar_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(models.Pet).filter(models.Pet.id_pet == pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado.")
    db.delete(pet)
    db.commit()
    return {"ok": True}
