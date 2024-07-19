import sys
default_path = "C:\\Users\\julia\\OneDrive\\Área de Trabalho\\backend"
sys.path.append(default_path)

from core.configs import settings

from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class Colaborador(Base):
    __tablename__ = "colaborador"

    cod_cracha = Column(Integer, primary_key=True, index=True)
    edv = Column(Integer)
    nome = Column(String(255))
    local_trabalho = Column(Enum("presencial", "home office"))

    beneficios = relationship("Beneficio", back_populates="colaborador")

class Beneficio(Base):
    __tablename__ = "beneficio"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(Enum("vale-refeição", "cesta básica"))
    status = Column(Enum("pendente", "concluído"))
    cod_cracha = Column(Integer, ForeignKey("colaborador.cod_cracha"))

    colaborador = relationship("Colaborador", back_populates="beneficios")
    