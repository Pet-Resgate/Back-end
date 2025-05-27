from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Usuario(Base):
    __tablename__ = "Usuario"
    id_usuario = Column(Integer, primary_key=True, index=True)
    tipo_usuario = Column(String(20), nullable=False)
    nome = Column(String(50), nullable=False)
    idade = Column(Integer)
    email = Column(String(50), unique=True, nullable=False)
    CPF = Column(String(11))
    CNPJ = Column(String(14))
    senha = Column(String(50), nullable=False)
    telefone = Column(String(20))

    pets = relationship("Pet", back_populates="dono")
    adocoes = relationship("Adocao", back_populates="adotante")

class Pet(Base):
    __tablename__ = "Pet"
    id_pet = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("Usuario.id_usuario", ondelete="CASCADE"), nullable=False)
    nome = Column(String(20))
    idade = Column(Integer)
    animal = Column(Text)
    raca = Column(String(50))
    porte = Column(String(20))
    descricao = Column(Text)
    status = Column(String(30))
    data_resgate = Column(Date)

    dono = relationship("Usuario", back_populates="pets")
    adocao = relationship("Adocao", uselist=False, back_populates="pet")

class Adocao(Base):
    __tablename__ = "Adocao"
    id_adocao = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("Usuario.id_usuario", ondelete="CASCADE"), nullable=False)
    id_pet = Column(Integer, ForeignKey("Pet.id_pet", ondelete="CASCADE"), unique=True, nullable=False)
    data_adocao = Column(Date, nullable=False)
    formulario = Column(Text)

    adotante = relationship("Usuario", back_populates="adocoes")
    pet = relationship("Pet", back_populates="adocao")