import asyncio ### async
from sqlalchemy.future import select ### async

import os
import sys
# Adicionar o caminho do diretório pai ao (sys.path)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conf.conexao import session, engine ### sys.path
from model.catalago import Filmes ### sys.path


# -------------------------------------------- LER --------------------------------------------
# READ
async def get_filmes(): ### async
    async with session: ### async

       # sessão (interação com Banco de Dados)
        busca_filme = await session.execute(select(Filmes).filter(Filmes.ano == 2000)) ### async
        filmes = busca_filme.scalars().all()### async
        print("GET 01:")
        # acesso a lista do Banco de Dados
        for filme in filmes:
            print(filme) # __repr__ 

if __name__ == '__main__':
    # Função principal para gerenciar a execução
    async def main():
        print()
        await  get_filmes()
        await engine.dispose()

    # # Executa o loop assíncrono
    asyncio.run(main())
