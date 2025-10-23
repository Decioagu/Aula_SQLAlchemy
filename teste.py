from infra.configs.sql_alchemy import BaseModel # ORM do SQLAlchemy (classe)
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

# modelo: gerenciamento e validação de dados
class Filmes(BaseModel):
    # ESCOPO BANCO DE DADOS
    __tablename__ = "filmes"
    titulo = Column(Integer, primary_key=True) # chave primaria 
    genero = Column(Integer, nullable=False)
    ano = Column(Integer, nullable=False)

    # MÉTODO AUXILIAR leitura (GET)
    def __repr__(self):
        return f"Filme [titulo={self.titulo}, genero={self.genero}, ano={self.ano}]"