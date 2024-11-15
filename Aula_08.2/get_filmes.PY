import asyncio
from sqlalchemy.future import select ### async
from conexao import Filmes, session, engine

# -------------------------------------------- LER --------------------------------------------
# READ
async def get_filmes_01(): ### async
    async with session: ### async

       # sessão (interação com Banco de Dados)
        busca_filme = await session.execute(select(Filmes)) ### async
        filmes = busca_filme.scalars().all() ### async
        print("GET 01:")
        # acesso a lista do Banco de Dados
        for filme in filmes:
            print(filme) # __repr__ 

if __name__ == '__main__':
    # Função principal para gerenciar a execução
    async def main():
        print()
        await  get_filmes_01()
        await engine.dispose()

    # # Executa o loop assíncrono
    asyncio.run(main())
print()
print('Décio Santana de Aguiar')