import sys
import os

from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from datetime import datetime

# Adicionar o caminho do diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.tipo_picole import TipoPicole # Chave estrangeira e relacionamento

class Lote(SQLModel, table = True):
    # ESCOPO BANCO DE DADOS
    id: Optional[int] = Field(default=None, primary_key=True)
    data_criacao: datetime = Field(default=datetime.now(), index=True)
    quantidade: int = Field()

    # Chave estrangeira e relacionamento
    id_tipo_picole: int = Field(foreign_key='tipo_picoles.id') # chave estrangeira
    tipo_picoles: TipoPicole = Relationship(sa_relationship_kwargs={'lazy':'joined'}) # Relacionamento

    def __repr__(self) -> str:
        return f'<Lote: {self.id}>'

'''
Relationship: Define relações entre tabelas (como um-para-muitos, muitos-para-muitos).
'''