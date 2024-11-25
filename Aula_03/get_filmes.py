from conexao import Filmes, session

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

if __name__ == '__main__':
    get_filmes_01()