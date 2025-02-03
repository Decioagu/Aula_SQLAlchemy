from sqlalchemy import Column, Integer, DateTime, String

from datetime import datetime

from conf.model_base import ModelBase # ORM do SQLAlchemy (classe)

class AditivoNutritivo(ModelBase):
    # ESCOPO BANCO DE DADOS
    __tablename__: str = 'aditivos_nutritivos'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = Column(DateTime, default=datetime.now, index=True)
    nome: str = Column(String(45), unique=True, nullable=False)
    formula_quimica: str = Column(String(45), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'<Aditivo Nutritivo: {self.nome}>'

