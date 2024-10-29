from infra.configs.sql_alchemy import BaseModel # ORM do SQLAlchemy (classe)
from sqlalchemy import Column, String, Integer, ForeignKey

# modelo: gerenciamento e validação de dados
class Atores(BaseModel):
    # ESCOPO BANCO DE DADOS
    __tablename__ = "atores"
    id = Column(Integer, primary_key=True) # chave primaria 
    nome = Column(String, nullable=False)
    titulo_filme = Column(String, ForeignKey("filmes.titulo")) # chave estrangeira 

    # MÉTODO AUXILIAR leitura (GET)
    def __repr__(self):
        return f"Atores [ id = {self.id}, nome={self.nome}, filme={self.titulo_filme}]"
