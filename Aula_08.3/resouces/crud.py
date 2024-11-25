import asyncio ### async
from sqlalchemy.future import select ### async
from sqlalchemy.exc import SQLAlchemyError

import os
import sys
# Adicionar o caminho do diretório pai ao (sys.path)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conf.conexao import Session, engine, tabela_existe, criar_tables ### sys.path
from model.catalago import Filmes ### sys.path

# ============================================  CRUD  ============================================
# -------------------------------------------- CRIAR ---------------------------------------------
# CREATE
async def post_filme(_titulo_: str ,_genero_: str ,_ano_: int): ### async
    async with Session() as session: ### async
        try:
            # sessão (interação com Banco de Dados)
            inserir_dados = Filmes(titulo =_titulo_, genero =_genero_, ano =_ano_)

            # Verificar se o "nome" do AditivoNutritivo já existe
            titulo_ja_existe = await session.get(Filmes, _titulo_)

            if titulo_ja_existe:
                print(f'Título "{_titulo_}" já esta cadastrado.')
                return

            # Inserir no Banco de Dados
            session.add(inserir_dados)
            # Salvar
            await session.commit() ### async
            print(f"POST: Filme {_titulo_} inserido com sucesso!")
            
        except SQLAlchemyError as e:
            print("POST:")
            print(f"Ocorreu um erro ao interagir com o banco de dados: {e}")
            await session.rollback()  ### async (Reverte a transação caso haja erro)

# -------------------------------------------- LER --------------------------------------------
# READ
async def get_filmes_01(): ### async
    async with Session() as session: ### async

       # sessão (interação com Banco de Dados)
        busca_filme = await session.execute(select(Filmes)) ### async
        filmes = busca_filme.scalars().all() ### async
        print("GET 01:")
        # acesso a lista do Banco de Dados
        for filme in filmes:
            print(filme) # __repr__ 

# -------------------------------------------- LER --------------------------------------------
# READ
async def get_filmes_02(): ### async
    async with Session() as session: ### async
        # sessão (interação com Banco de Dados)
        filmes = await session.execute(select(Filmes).order_by(Filmes.ano.desc()))  ### async
        filmes_lista = filmes.scalars().all()  ### async
        print("GET 02:")
        # acesso a lista do Banco de Dados
        for filme in filmes_lista:
            print(filme)  # __repr__

# -------------------------------------------- LER --------------------------------------------
# READ
async def get_filmes_03(ano: int = None): ### async
    async with Session() as session: ### async
        # sessão (interação com Banco de Dados)
        busca_filme = await session.execute(select(Filmes).where(Filmes.ano == ano)) ### async
        filme = busca_filme.scalars().all()  ### async

        print("GET 03:")
        # acesso a lista do Banco de Dados
        print(filme) # NÃO gera exceções se não encontra

# -------------------------------------------- ATUALIZAR --------------------------------------------
# UPDATE
async def update_filme(filme_titulo: str, ano: int): ### async
    async with Session() as session: ### async
        # Verificar se o filme já existe (Filtro com id)
        filme_existente = await session.get(Filmes, filme_titulo)
        print(filme_existente)

        if filme_existente:
            # Verificar se o filme já existe (Filtro com id)
            print(f"UPDATE: Filme '{filme_titulo}' atualizado com sucesso!") 
            # Atualiza o ano do filme
            filme_existente.ano = ano
            # Salvar
            await session.commit()
        else:
            print(f"UPDATE: Filme '{filme_titulo}' não encontrado para atualizar.")
            return 

# -------------------------------------------- DELETAR --------------------------------------------
# DELETE
async def delete_filme(filme_titulo: str):     
    async with Session() as session: ### async
        # Verificar se o filme já existe (Filtro com id)
        filme_existente = await session.get(Filmes, filme_titulo)
        print(filme_existente)

        if filme_existente:
                print(f"DELETE: Filme '{filme_titulo}' deletado com sucesso!")
                
                await session.delete(filme_existente) # Deletar o filme
                await session.commit()  # Confirmar a exclusão no banco de dados
        else:
            print(f"DELETE: Filme '{filme_titulo}' não encontrado para deletar.")

# ====================================================================================================
if __name__ == '__main__':
    async def main():
        # Verifica a existência de tabela 
        if await tabela_existe(engine, "filmes"):
            print("A tabela 'filmes' existe.")
        else:
            print("A tabela 'filmes' não existe.")
            await criar_tables(engine) # cria tabela (CASO NÃO EXISTA)
        print()
        await  get_filmes_01()
        print()
        await post_filme("AAA", "AAA", 2021)
        print()
        await  get_filmes_01()
        print()
        await  get_filmes_02()
        print()
        await  get_filmes_03(2021)
        print()
        await update_filme("VVV", 1987)
        print()
        await  get_filmes_01()
        print()
        await  delete_filme("AAA")
        print()
        await  get_filmes_01()
        print()
        await engine.dispose()

    asyncio.run(main())
    