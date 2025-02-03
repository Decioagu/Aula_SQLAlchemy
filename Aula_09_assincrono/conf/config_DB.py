from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text

# Usado em SQLite
from pathlib import Path 

from typing import Optional # tipagem

from conf.model_base import ModelBase # ORM do SQLAlchemy (classe)

import os
import sys
# Adicionar o caminho do diretório pai ao (sys.path)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine ### async (CONSULTA)
from sqlalchemy.future import select ### async

# ENDEREÇO DE CONEXÃO
__async_engine: Optional[AsyncEngine] = None ### async

# CONEXÃO (Função para configurar a conexão ao banco de dados)
async def criar_banco_de_dados(sqlite: bool = False) -> AsyncEngine: ### async

    global __async_engine ### async ENDEREÇO DE CONEXÃO

    # Se "ENDEREÇO DE CONEXÃO" existir
    if __async_engine: ### async
        return # retorne
    
    if sqlite:
        # endereço da pasta atual
        caminho_do_arquivo = Path(__file__) # ver caminho do arquivo executado
        basedir = os.path.abspath(os.path.dirname(caminho_do_arquivo.parent))

        conn_str = 'sqlite+aiosqlite:///' + os.path.join(basedir, 'picoles_async.sqlite') ### async (tipo de banco)
        __async_engine = create_async_engine(url=conn_str, echo=False, connect_args={"check_same_thread": False}) ### async
    else:
        # # Primeiro, conectar ao servidor MySQL sem especificar um banco de dados
        engine =  create_engine('mysql://root:Enigma.1@localhost:3306')

        # Criar o banco de dados "picoles_async" caso não exista
        with engine.connect() as connection:
            # "banco.text" permite execução de instruções SQL em sqlalchemy
            connection.execute(text("CREATE DATABASE IF NOT EXISTS picoles_async"))

        # Apontar para o banco de dados desejado
        conn_str = "mysql+aiomysql://root:Enigma.1@localhost:3306/picoles_async" ### async
        __async_engine = create_async_engine(url=conn_str, echo=False) ### async
    
    return __async_engine ### async

# CONSULTA (Função para criar sessão, consulta ao banco de dados)
async def criar_session() -> AsyncSession:

    global __async_engine # ENDEREÇO DE CONEXÃO

    if not __async_engine: ### async
        # criar_banco_de_dados() # MySQL
        await criar_banco_de_dados(sqlite=True) # SQLite

    __async_session = sessionmaker(bind = __async_engine, expire_on_commit=False, class_= AsyncSession) ### async
    session: AsyncSession = __async_session() ### async (consulta ao banco de dados)

    return session


async def criar_tabelas() -> None: ### async

    global __async_engine # ENDEREÇO DE CONEXÃO

    # Se "ENDEREÇO DE CONEXÃO" não existir
    if not __async_engine:
        await criar_banco_de_dados() # MySQL
        # await criar_banco_de_dados(sqlite=True) # SQLite
    
    # >>>>>>>>>> CRIAR TABELAS <<<<<<<<<<<
    import models.__all_models # MODELOS DE TABELAS
    async with __async_engine.begin() as conn: ### async
        # await conn.run_sync(ModelBase.metadata.drop_all) ### async (apagar tabelas)
        await conn.run_sync(ModelBase.metadata.create_all) ### async (criar tabelas)

# FUNÇÃO PARA FECHAR A CONEXÃO COM O BANCO DE DADOS
async def fechar_conexao():
    global __async_engine
    if __async_engine is not None:
        await __async_engine.dispose()
        __async_engine = None        
