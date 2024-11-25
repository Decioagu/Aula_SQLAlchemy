from sqlalchemy import create_engine, text, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

# Primeiro, conectar ao servidor MySQL sem especificar um banco de dados
engine = create_engine('mysql+mysqldb://root:Enigma.3@localhost:3306')

# Criar o banco de dados "cinema" caso não exista
with engine.connect() as connection:
    connection.execute(text("CREATE DATABASE IF NOT EXISTS cinema_02"))

# Apontar para o banco de dados desejado
engine = create_engine('mysql://root:Enigma.3@localhost:3306/cinema_02') # mysqlclient
BaseModel = declarative_base() # ORM do SQLAlchemy (classe)

# Session: é a classe usada para gerar "objetos de sessão"
Session = sessionmaker(bind=engine) # (interagir c/ banco de dados)
session = Session() # interação (inserções, consultas, atualizações e exclusões)

# ORM (Object-Relational Mapping)
class Filmes(BaseModel):
    __tablename__="filmes"
    titulo = Column(String(3), primary_key=True)
    genero = Column(String(3), nullable=False)
    ano = Column(Integer, nullable=False)

    # __repr__: representa a "classe Filmes" como uma "string"
    def __repr__(self):
        return f"Filme (titulo={self.titulo}, gênero={self.genero},ano={self.ano})" 

# cria a tabela após modelagem da classe "Filmes"
# BaseModel.metadata.drop_all(engine) # apagar tabelas
# BaseModel.metadata.create_all(engine) # criar tabelas

# CREATE
inserir_dados = Filmes(titulo='AAA', genero='AAA', ano=2000) # modelar dados
session.add(inserir_dados) # ação de adicionar ao Banco de Dados "objetos de sessão"
session.commit() # enviar para o Banco de Dados

# READ
busca_filme = session.query(Filmes).all() # ler dados
for filme in busca_filme: # lista de Filmes
    print(filme)

session.close() # fechar conexão