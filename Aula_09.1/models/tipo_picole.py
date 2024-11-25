# import sys
# import os

from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from typing import Optional, List

# Adicionar o caminho do diretório pai ao sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from models.lote import Lote

class TipoPicole(SQLModel, table = True):
    # ESCOPO BANCO DE DADOS
    id: Optional[int] = Field(default=None, primary_key=True)
    data_criacao: datetime = Field(default=datetime.now(), index=True)
    nome: str = Field(max_length = 45, unique=True)

    # lote: List[Lote] = Relationship(back_populates="tipo_picoles")  # Relacionamento

    def __repr__(self) -> str:
        return f'<Tipo Picole: {self.nome}>'

