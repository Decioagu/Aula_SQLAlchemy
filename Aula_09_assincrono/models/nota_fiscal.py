
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Table, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
from typing import List
from conf.model_base import ModelBase # ORM do SQLAlchemy (classe)

from models.revendedor import Revendedor # Chave estrangeira e relacionamento
from models.lote import Lote # chave estrangeira para nova (tabela "secundaria")

# Nota Fiscal pode ter vários lotes (muitos-para-muitos)
lotes_nota_fiscal = Table(
    'lotes_nota_fiscal', # nome
    ModelBase.metadata, # manipula estrutura do banco de dados com tabelas associadas (contêiner)
    Column('id_nota_fiscal', Integer, ForeignKey('notas_fiscais.id')),
    Column('id_lote', Integer, ForeignKey('lotes.id'))
)
'''Definindo uma tabela diretamente usando MetaData'''


class NotaFiscal(ModelBase):
    # ESCOPO BANCO DE DADOS
    __tablename__: str = 'notas_fiscais'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = Column(DateTime, default=datetime.now, index=True)
    valor: float = Column(DECIMAL(8,2), nullable=False)
    numero_serie: str = Column(String(45), unique=True, nullable=False)
    descricao: str = Column(String(200), nullable=False)

    id_revendedor: Mapped[int] = mapped_column(Integer, ForeignKey('revendedores.id')) # chave estrangeira
    revendedor: Mapped[Revendedor] = relationship('Revendedor', lazy='joined') # Relacionamento

    # Uma nota fiscal pode ter vários lotes e um lote está ligado a uma nota fiscal (tabela "secundaria")
    lotes: Mapped[List[Lote]] = relationship('Lote', secondary=lotes_nota_fiscal, backref='lote', lazy='dynamic')
    ''' OBS: em SQLalchemy assíncrono utilizar "lazy='dynamic" ao manipular lista'''

    def __repr__(self) -> int:
        return f'<Nota Fiscal: {self.numero_serie}>'

