from conexao import Filmes, session
from sqlalchemy import select

# -------------------------------------------- LER --------------------------------------------
# READ
# READ
def get_filmes_01():
    # sessão (interação com Banco de Dados)
    busca_filme = session.query(Filmes).all()
    print("GET 01:")
    # acesso a lista do Banco de Dados
    for filme in busca_filme:
        print(filme) # __repr__
    session.close()

def get_filmes_02():
    # sessão (interação com Banco de Dados)
    selecionar = select(Filmes)
    busca_filme = session.execute(selecionar)
    print("GET 02:")
    # acesso a lista do Banco de Dados
    for filme in busca_filme:
        print(filme) # __repr__
    session.close()

if __name__ == '__main__':
    get_filmes_01()
    print()
    get_filmes_02()