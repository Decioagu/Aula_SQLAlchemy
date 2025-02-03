from sqlalchemy import Column, Integer, DateTime, ForeignKey, Table, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime
from typing import List, Optional
from conf.model_base import ModelBase # ORM do SQLAlchemy (classe)

from models.sabor import Sabor # Chave estrangeira e relacionamento
from models.tipo_embalagem import TipoEmbalagem # Chave estrangeira e relacionamento
from models.tipo_picole import TipoPicole # Chave estrangeira e relacionamento

from models.ingrediente import Ingrediente # chave estrangeira para nova (tabela "secundaria")
from models.conservante import Conservante # chave estrangeira para nova (tabela "secundaria")
from models.aditivo_nutritivo import AditivoNutritivo # chave estrangeira para nova (tabela "secundaria")


# Picolé pode ter vários ingredientes (muitos-para-muitos)
ingredientes_picole = Table(
    'ingredientes_picole', # nome
    ModelBase.metadata, # manipula estrutura do banco de dados com tabelas associadas (contêiner)
    Column('id_picole', Integer, ForeignKey('picoles.id')),
    Column('id_ingrediente', Integer, ForeignKey('ingredientes.id'))
)

# Picolé pode ter vários conservantes (muitos-para-muitos)
conservantes_picole = Table(
    'conservantes_picole', # nome
    ModelBase.metadata, # manipula estrutura do banco de dados com tabelas associadas (contêiner)
    Column('id_picole', Integer, ForeignKey('picoles.id')),
    Column('id_conservante', Integer, ForeignKey('conservantes.id'))
)

# Picole pode ter vários aditivos nutritivos (muitos-para-muitos)
aditivos_nutritivos_picole = Table(
    'aditivos_nutritivos_picole', # nome
    ModelBase.metadata, # manipula estrutura do banco de dados com tabelas associadas (contêiner)
    Column('id_picole', Integer, ForeignKey('picoles.id')),
    Column('id_aditivo_nutritivo', Integer, ForeignKey('aditivos_nutritivos.id'))
)


class Picole(ModelBase):
    # ESCOPO BANCO DE DADOS
    __tablename__: str = 'picoles'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = Column(DateTime, default=datetime.now, index=True)
    preco: float = Column(DECIMAL(8,2), nullable=False)

    id_sabor: Mapped[int] = mapped_column(Integer, ForeignKey('sabores.id')) # chave estrangeira 
    sabor: Mapped[Sabor] = relationship('Sabor', lazy='joined') # Relacionamento

    id_tipo_embalagem: Mapped[int] = mapped_column(Integer, ForeignKey('tipos_embalagem.id')) # chave estrangeira 
    tipo_embalagem: Mapped[TipoEmbalagem] = relationship('TipoEmbalagem', lazy='joined') # Relacionamento

    id_tipo_picole: Mapped[int] = mapped_column(Integer, ForeignKey('tipos_picole.id')) # chave estrangeira 
    tipo_picole: Mapped[TipoPicole] = relationship('TipoPicole', lazy='joined') # Relacionamento

    # Um picole pode ter vários ingredientes (tabela "secundaria")
    ingredientes: Mapped[List[Ingrediente]] = relationship('Ingrediente', secondary=ingredientes_picole, backref='ingrediente', lazy='dynamic')
    ''' OBS: em SQLalchemy assíncrono utilizar "lazy='dynamic" ao manipular lista'''

    # Um picolé pode ter vários conservantes ou mesmo nenhum (tabela "secundaria")
    conservantes: Mapped[Optional[List[Conservante]]] = relationship('Conservante', secondary=conservantes_picole, backref='conservante', lazy='dynamic')
    ''' OBS: em SQLalchemy assíncrono utilizar "lazy='dynamic" ao manipular lista'''

    # Um picole pode ter vários aditivos nutritivos ou mesmo nenhum (tabela "secundaria")
    aditivos_nutritivos: Mapped[Optional[List[AditivoNutritivo]]] = relationship('AditivoNutritivo', secondary=aditivos_nutritivos_picole, backref='aditivo_nutritivo', lazy='dynamic')
    ''' OBS: em SQLalchemy assíncrono utilizar "lazy='dynamic" ao manipular lista'''
    
    def __repr__(self) -> str:
        return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}>'

