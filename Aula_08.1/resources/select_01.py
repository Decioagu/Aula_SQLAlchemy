import sys
import os
import asyncio ### async
from sqlalchemy.future import select ### async

# Adicionar o caminho do diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conf.config_DB import criar_session, criar_banco_de_dados

# ESCOPO BANCO DE DADOS
from models.aditivo_nutritivo import AditivoNutritivo 

# Função para realizar o select
async def selecionar_aditivos_nutritivos():
    # Obtenha a sessão de conexão com o banco de dados de forma assíncrona
    async with criar_session() as session:
        query = select(AditivoNutritivo)

        # Consulta assíncrona na tabela "aditivos_nutritivos"
        dados = await session.execute(query)

        # Extrair os resultados da consulta
        aditivos = dados.scalars().all()
        
        for aditivo in aditivos:
            print(aditivo)  # __repr__
        
# Função para garantir o fechamento do loop
if __name__ == '__main__':

    # Função principal para gerenciar a execução
    async def main():
        print()
        await  selecionar_aditivos_nutritivos()

    # Executa o loop assíncrono
    asyncio.run(main())


