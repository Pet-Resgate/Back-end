#Valida o que o usuário pode enviar e receber.

from pydantic import BaseModel
from typing import Optional
from datetime import date

# -------------------- USUÁRIO --------------------
class UsuarioBase(BaseModel):
    tipo_usuario: str
    nome: str
    idade: Optional[int]
    email: str
    cpf: Optional[str]
    cnpj: Optional[str]
    senha: str
    telefone: Optional[str]

class UsuarioCreate(UsuarioBase): 
    pass

class UsuarioOut(UsuarioBase):
    id_usuario: int
    class Config:
        from_attributes = True 

# -------------------- PET --------------------
class PetBase(BaseModel):
    nome: Optional[str]
    idade: Optional[int]
    animal: Optional[str]
    raca: Optional[str]
    porte: Optional[str]
    descricao: Optional[str]
    status: Optional[str]
    data_resgate: Optional[date]
    brinca: Optional[int] = None        
    carinhoso: Optional[int] = None     
    sociavel: Optional[int] = None   
    sexo: Optional[str]



class PetOut(PetBase):
    id_pet: int
    
    class Config:
        from_attributes = True 

# -------------------- ADOÇÃO --------------------
class AdocaoBase(BaseModel):
    id_usuario: int
    id_pet: int
    data_adocao: date
    formulario: Optional[str]

class AdocaoCreate(AdocaoBase): 
    pass

class AdocaoOut(AdocaoBase):
    id_adocao: int
    class Config:
        from_attributes = True 

class Adocao(AdocaoBase): 
    id_adocao: int
    class Config:
        orm_mode = True 
