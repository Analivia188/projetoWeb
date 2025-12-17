from sqlalchemy import Column, String, Integer, Boolean, DateTime, Float
from sqlalchemy.orm import declarative_base
from dao.banco import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    email = Column(String, primary_key=True)
    nome = Column(String)
    senha = Column(String)

    def __repr__(self):
        return f"<Usuario(email='{self.email}', nome='{self.nome}')>"

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    valor = Column(Float)

    def __repr__(self):
        return f"<Produto(id='{self.id}', nome='{self.nome}')>"

