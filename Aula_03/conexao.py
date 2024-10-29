from sqlalchemy import create_engine, text, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# endereço de conexão
engine = create_engine('mysql://root:Enigma.3@localhost:3306/cinema_03') # mysqlclient
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

# =========================================== CRUD ==================================================

# ============================================ CRIAR ============================================= 
# CREATE
def post_filme(_titulo_ ,_genero_ ,_ano_):
    try:
        # Inserir no Banco de Dados
        inserir_dados = Filmes(titulo=_titulo_, genero=_genero_, ano=_ano_)
        session.add(inserir_dados)
        session.commit()
        print(f"POST: Filme {_titulo_} inserido com sucesso!")
        
    except SQLAlchemyError as e:
        print("POST:")
        print(f"Ocorreu um erro ao interagir com o banco de dados: {e}")
        session.rollback()  # Reverte a transação caso haja erro
    
# ========================================== LER =================================================
# READ
def get_filmes():
    # sessão (interação com Banco de Dados)
    busca_filme = session.query(Filmes).all()
    print("GET:")
    # acesso a lista do Banco de Dados
    for filme in busca_filme:
        print(filme)

# ============================================= ATUALIZAR ===========================================
# UPDATE
def update_filme(filme_titulo, ano): 

    # Verificar se o filme já existe (Filtro com id)
    filme_existente = session.query(Filmes).filter_by(titulo=filme_titulo).first()
    """filter_by: sintaxe simples suporta apenas igualdade"""

    if filme_existente:
        print(f"UPDATE: Filme '{filme_titulo}' atualizado com sucesso!") 
        # Verificar se o filme já existe (Filtro com id)
        session.query(Filmes).filter(Filmes.titulo == filme_titulo).update({"ano": ano})
        """filter: sintaxe completa suporta (>,<,!=,==, etc)"""
        session.commit()
    else:
        print(f"UPDATE: Filme '{filme_titulo}' não encontrado para atualizar.")
    
# =========================================== DELETAR =============================================
# DELETE
def delete_filme(filme_titulo):     

    # Verificar se o filme já existe (Filtro com id)
    filme_existente = session.query(Filmes).filter_by(titulo=filme_titulo).first()

    if filme_existente:
            print(f"DELETE: Filme '{filme_titulo}' deletado com sucesso!")
            
            session.delete(filme_existente) # Deletar o filme
            session.commit()  # Confirmar a exclusão no banco de dados       
    else:
        print(f"DELETE: Filme '{filme_titulo}' não encontrado para deletar.")

# ==================================================================================================
# print()
get_filmes()
print()
delete_filme("Homens de honra")
print()
get_filmes()
print()
post_filme('Homens de honra',"Ação/Darma", 2001)
print()
get_filmes()
print()
update_filme("O predador", 1987)
print()
get_filmes()
print()
session.close() # fechar conexão