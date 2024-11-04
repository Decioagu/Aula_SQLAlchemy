from sqlalchemy import create_engine, text, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine



# endereço de conexão
# echo = True:  exibe no console todas as consultas SQL e outras operações que realiza
engine = create_async_engine('mysql+aiomysql://root:Enigma.3@localhost:3306/cinema_03', echo=True) # mysqlclient
BaseModel = declarative_base() # ORM do SQLAlchemy (classe)

# Session: é a classe usada para gerar objetos de sessão
Session = sessionmaker(bind=engine) # (interagir c/ banco de dados)
session = Session() # interação (inserções, consultas, atualizações e exclusões)

# ORM (Object-Relational Mapping)
class Filmes(BaseModel):
    __tablename__="filmes"

    titulo = Column(String(25), primary_key=True)
    genero = Column(String(25), nullable=False)
    ano = Column(Integer, nullable=False)

    # __repr__: representa a "classe Filmes" como uma "string"
    def __repr__(self):
        return f"Filme (titulo={self.titulo}, gênero={self.genero},ano={self.ano})"

# ============================================  CRUD  ============================================
# -------------------------------------------- CRIAR ---------------------------------------------
# CREATE
def post_filme(_titulo_: str ,_genero_: str ,_ano_: int):
    try:
        # sessão (interação com Banco de Dados)
        inserir_dados = Filmes(titulo=_titulo_, genero=_genero_, ano=_ano_)
        # Inserir no Banco de Dados
        session.add(inserir_dados)
        # Salvar
        session.commit()
        print(f"POST: Filme {_titulo_} inserido com sucesso!")
        
    except SQLAlchemyError as e:
        print("POST:")
        print(f"Ocorreu um erro ao interagir com o banco de dados: {e}")
        session.rollback()  # Reverte a transação caso haja erro
    
# -------------------------------------------- LER --------------------------------------------
# READ
def get_filmes_01():
    # sessão (interação com Banco de Dados)
    busca_filme = session.query(Filmes).all()
    print("GET 01:")
    # acesso a lista do Banco de Dados
    for filme in busca_filme:
        print(filme) # __repr__

# -------------------------------------------- LER --------------------------------------------
# READ
def get_filmes_02():
    # sessão (interação com Banco de Dados)
    busca_filme = session.query(Filmes).order_by(Filmes.ano.desc()).all()
    print("GET 02:")
    # acesso a lista do Banco de Dados
    for filme in busca_filme:
        print(filme) # __repr__

# -------------------------------------------- LER --------------------------------------------
# READ
def get_filmes_03():
    # sessão (interação com Banco de Dados)
    busca_filme = session.query(Filmes).all()
    print("GET 03:")
    # acesso a lista do Banco de Dados
    for filme in busca_filme:
        print(filme) # __repr__

# -------------------------------------------- LER --------------------------------------------
# READ
def get_filmes_04():
    # sessão (interação com Banco de Dados)
    ano = 1987
    busca_filme = session.query(Filmes).filter(Filmes.ano == ano).first()
    print("GET 04:")
    # acesso a lista do Banco de Dados
    print(busca_filme) # NÃO gera exceções se não encontra
    print(busca_filme.ano) # gera exceções se não encontra

# -------------------------------------------- LER --------------------------------------------
# READ
def get_filmes_05():
    # sessão (interação com Banco de Dados)
    ano = 1987
    busca_filme = session.query(Filmes).filter(Filmes.ano == ano).one()
    print("GET 05:")
    # acesso a lista do Banco de Dados
    print(busca_filme) # gera exceções se não encontra
    print(busca_filme.ano) # gera exceções se não encontra

# -------------------------------------------- LER --------------------------------------------
# READ
def get_filmes_06():
    # sessão (interação com Banco de Dados)
    ano = 1987
    # "where" é equivalente ao "filter"
    busca_filme = session.query(Filmes).where(Filmes.ano == ano).first()
    print("GET 06:")
    # acesso a lista do Banco de Dados
    print(busca_filme) # NÃO gera exceções se não encontra
    print(busca_filme.ano) # gera exceções se não encontra

# -------------------------------------------- ATUALIZAR --------------------------------------------
# UPDATE
def update_filme_01(filme_titulo: str, ano: int): 

    # Verificar se o filme já existe (Filtro com id)
    filme_existente = session.query(Filmes).filter_by(titulo = filme_titulo).first()
    """filter_by: sintaxe simples suporta apenas igualdade"""

    if filme_existente:
        print(f"UPDATE: Filme '{filme_titulo}' atualizado com sucesso!") 
        # Verificar se o filme já existe (Filtro com id)
        session.query(Filmes).filter(Filmes.titulo == filme_titulo).update({"ano": ano})
        """filter: sintaxe completa suporta (>,<,!=,==, etc)"""
        # Salvar
        session.commit()
    else:
        print(f"UPDATE: Filme '{filme_titulo}' não encontrado para atualizar.")

# -------------------------------------------- ATUALIZAR --------------------------------------------
# UPDATE
def update_filme_02(filme_titulo: str, ano: int): 

    # Verificar se o filme já existe (Filtro com id)
    filme_existente = session.query(Filmes).filter_by(titulo = filme_titulo).first()

    if filme_existente:
        print(f"UPDATE: Filme '{filme_titulo}' atualizado com sucesso!") 
        # Atualiza o ano do filme
        filme_existente.ano = ano
        # Salvar
        session.commit()
    else:
        print(f"UPDATE: Filme '{filme_titulo}' não encontrado para atualizar.")
    
# -------------------------------------------- DELETAR --------------------------------------------
# DELETE
def delete_filme(filme_titulo: str):     

    # Verificar se o filme já existe (Filtro com id)
    filme_existente = session.query(Filmes).filter_by(titulo = filme_titulo).first()

    if filme_existente:
            print(f"DELETE: Filme '{filme_titulo}' deletado com sucesso!")
            
            session.delete(filme_existente) # Deletar o filme
            session.commit()  # Confirmar a exclusão no banco de dados       
    else:
        print(f"DELETE: Filme '{filme_titulo}' não encontrado para deletar.")

# ====================================================================================================

print()
get_filmes_01()
# print()
# delete_filme("Homens de honra")
# print()
# get_filmes_01()
# print()
# post_filme('Homens de honra',"Ação/Darma", 2001)
# print()
# get_filmes_01()
# print()
# update_filme_01("O predador", 1987)
print()
update_filme_02("O predador", 2000)
print()
get_filmes_01()
# print()
# get_filmes_02()
# print()
# get_filmes_03()
# print()
# get_filmes_04()
# print()
# get_filmes_05()
# print()
# get_filmes_06()
session.close() # fechar conexão