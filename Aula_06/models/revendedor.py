from sqlalchemy import Column, Integer, DateTime, String

from datetime import datetime

from conf.model_base import ModelBase # ORM do SQLAlchemy (classe)


class Revendedor(ModelBase):
    __tablename__: str = 'revendedores'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = Column(DateTime, default=datetime.now, index=True)
    nome: str = Column(String(45), unique=True, nullable=False)
    razao_social: str = Column(String(100), nullable=False)
    contato: str = Column(String(100), nullable=False)

    def __repr__(self) -> str:
        return f'<Revendedor: {self.nome}>'

