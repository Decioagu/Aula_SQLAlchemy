from typing import List
from sqlmodel import Field, SQLModel, Relationship
from decimal import Decimal

from typing import Optional

from datetime import datetime

from models.revendedor import Revendedor # Chave estrangeira e relacionamento
from models.lote import Lote # chave estrangeira para nova (tabela "secundaria")

# Nota Fiscal pode ter vários lotes (muitos-para-muitos)
class LotesNotaFiscal(SQLModel, table = True):
    id_nota_fiscal: int = Field(foreign_key='notas_fiscais.id')
    id_lote: int = Field(foreign_key='lotes.id')

'''Definindo uma tabela diretamente usando MetaData'''


class NotaFiscal(SQLModel, table = True):
    # ESCOPO BANCO DE DADOS
    id: Optional[int] = Field(default=None, primary_key=True)
    data_criacao: datetime = Field(default=datetime.now(), index=True)
    valor: Decimal = Field(max_digits=8, decimal_places=2) # https://sqlmodel.tiangolo.com/advanced/decimal/
    numero_serie: str = Field(max_length = 45, unique=True)
    descricao: str = Field(max_length = 200)

    id_revendedor: int = Field(foreign_key  = 'revendedores.id') # chave estrangeira
    revendedor: Revendedor = Relationship(back_populates = 'revendedores',  sa_relationship_kwargs={'lazy':'joined'}) # Relacionamento

    # Uma nota fiscal pode ter vários lotes e um lote está ligado a uma nota fiscal (tabela "secundaria")
    lotes: List[Lote] = Relationship(link_model=LotesNotaFiscal, back_populates = 'lote', sa_relationship_kwargs={'lazy':'dynamic'})

    def __repr__(self) -> int:
        return f'<Nota Fiscal: {self.numero_serie}>'

