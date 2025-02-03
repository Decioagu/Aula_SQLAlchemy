from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
from conf.model_base import ModelBase

from models.tipo_picole import TipoPicole # Chave estrangeira e relacionamento


class Lote(ModelBase):
    # ESCOPO BANCO DE DADOS
    __tablename__: str = 'lotes'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = Column(DateTime, default=datetime.now, index=True)
    quantidade: int = Column(Integer, nullable=False)

    # Chave estrangeira e relacionamento
    id_tipo_picole: Mapped[int] = mapped_column(Integer, ForeignKey('tipos_picole.id')) # chave estrangeira
    tipo_picole: Mapped[TipoPicole] = relationship('TipoPicole', lazy='joined') # Relacionamento

    def __repr__(self) -> str:
        return f'<Lote: {self.id}>'

'''
sqlalchemy.orm: Módulo que habilita o mapeamento objeto-relacional.
Mapped: Tipo genérico para definir o tipo de dados mapeado para colunas.
mapped_column: Função para criar colunas no banco de dados com atributos configuráveis.
relationship: Define relações entre tabelas (como um-para-muitos, muitos-para-muitos).
'''