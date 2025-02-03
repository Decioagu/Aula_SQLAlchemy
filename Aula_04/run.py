from infra.resources.atores_repository import AtoresRepository
from infra.resources.filmes_repository import FilmesRepository

# rota Atores (CRUD)
# método de (Leitura 1)
resposta_01 = AtoresRepository().select() 
print(resposta_01) # lista de atores

# rota Atores (CRUD)
# método de (Leitura 2)
resposta_02 = AtoresRepository().select_filmes() 
print(resposta_02) # lista de atores e filmes

# rota Filmes (CRUD)
# método de (Leitura)
resposta_03 = FilmesRepository().select()
print(resposta_03)  # lista de filmes

# rota Filmes (CRUD)
# método de (Leitura por genero)
resposta_04 = FilmesRepository().select_genero(genero='Ação')
print(resposta_04) # lista de filmes de genero informado

# rota Filmes (CRUD)
# método de (Criar)
resposta_05 = FilmesRepository().insert(titulo="a", genero="a", ano=1999)
print(resposta_05)

# rota Filmes (CRUD)
# método de (Deletar por titulo)
resposta_06 = FilmesRepository().delete(titulo="A")
print(resposta_06)

# rota Filmes (CRUD)
# método de (Atualização por titulo)
resposta_07 = FilmesRepository().update(titulo="Predador", ano=1987)
print(resposta_07)

# Verificar  se banco de dados cinema_04 exite: utilizar DB_04.sql

