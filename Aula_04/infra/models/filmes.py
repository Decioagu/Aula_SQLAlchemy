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
    
    """
    - relationship: é uma função do SQLAlchemy que é usada para definir uma relação entre duas tabelas.
        - backref='__tablename__': é uma maneira mais simples e automática de definir um 
        relacionamento bidirecional. Ele cria automaticamente o relacionamento nos dois 
        lados (nas duas tabelas) de uma vez só. Além disso, ele configura automaticamente 
        uma referência reversa sem a necessidade de configurar explicitamente em ambos os modelos.
        - lazy='dynamic': Este parâmetro define como a carga dos dados relacionados 
        será tratada. (não obrigatório) 
    """
