from sqlalchemy import Column, Integer, DateTime, String

from datetime import datetime

from conf.model_base import ModelBase # ORM do SQLAlchemy (classe)

class Conservante(ModelBase):
    # ESCOPO BANCO DE DADOS
    __tablename__: str = 'conservantes'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = Column(DateTime, default=datetime.now, index=True)
    nome: str = Column(String(45), unique=True, nullable=False)
    descricao: str = Column(String(45), nullable=False)

    def __repr__(self) -> str:
        return f'<Conservante: {self.nome}>'

