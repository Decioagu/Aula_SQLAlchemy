from sqlmodel import Field, SQLModel
from datetime import datetime
from typing import Optional

class Ingrediente(SQLModel, table = True):
    # ESCOPO BANCO DE DADOS
    id: Optional[int] = Field(default=None, primary_key=True)
    data_criacao: datetime = Field(default=datetime.now(), index=True)
    nome: str = Field(max_length = 45, unique=True)

    def __repr__(self) -> str:
        return f'<Ingrediente: {self.nome}>'

