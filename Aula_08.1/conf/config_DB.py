import sqlalchemy as banco # CONEXÃO
from sqlalchemy.future.engine import Engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session # CONSULTA

# Usado em SQLite
from pathlib import Path 
import os

from typing import Optional # tipagem

from conf.model_base import ModelBase # ORM do SQLAlchemy (classe)

from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine ### async

# ENDEREÇO DE CONEXÃO
__async_engine: Optional[AsyncEngine] = None ### async

# CONEXÃO (Função para configurar a conexão ao banco de dados)
def criar_banco_de_dados(sqlite: bool = False) -> AsyncEngine: ### async

    global __async_engine ### async ENDEREÇO DE CONEXÃO

    # Se "ENDEREÇO DE CONEXÃO" existir
    if __async_engine: ### async
        return # retorne
    
    if sqlite:
        # endereço da pasta atual
        caminho_do_arquivo = Path(__file__) # ver caminho do arquivo executado
        basedir = os.path.abspath(os.path.dirname(caminho_do_arquivo.parent))

        conn_str = 'sqlite+aiosqlite:///' + os.path.join(basedir, 'picoles.sqlite') ### async (tipo de banco)
        __async_engine = banco.create_engine(url=conn_str, echo=False, connect_args={"check_same_thread": False}) ### async
    else:
        # Primeiro, conectar ao servidor MySQL sem especificar um banco de dados
        engine =  banco.create_engine('mysql+aiomysql://root:Enigma.3@localhost:3306') ### async

        # Criar o banco de dados "picoles" caso não exista
        with engine.connect() as connection:
            # "banco.text" permite execução de instruções SQL em sqlalchemy
            connection.execute(banco.text("CREATE DATABASE IF NOT EXISTS picoles"))

        # Apontar para o banco de dados desejado
        conn_str = "mysql+aiomysql://root:Enigma.3@localhost:3306/picoles" ### async
        __async_engine = banco.create_engine(url=conn_str, echo=False) ### async
    
    return __async_engine ### async

# CONSULTA (Função para criar sessão, consulta ao banco de dados)
def criar_session() -> Session:

    global __async_engine # ENDEREÇO DE CONEXÃO

    if not __async_engine: ### async
        criar_banco_de_dados() # MySQL

    __async_session = sessionmaker(__async_engine, expire_on_commit=False, class_= AsyncSession) ### async
    session: AsyncSession = __async_session() ### async (consulta ao banco de dados)

    return session


async def criar_tabelas() -> None: ### async

    global __async_engine # ENDEREÇO DE CONEXÃO

    # Se "ENDEREÇO DE CONEXÃO" não existir
    if not __async_engine:
        criar_banco_de_dados() # MySQL
        # criar_banco_de_dados(sqlite=True) # SQLite
    
    # >>>>>>>>>> CRIAR TABELAS <<<<<<<<<<<
    import models.__all_models # MODELOS DE TABELAS
    async with __async_engine.begin() as conn: ### async
        await conn.run_sync(ModelBase.metadata.drop_all) ### async (apagar tabelas)
        await conn.run_sync(ModelBase.metadata.create_all) ### async (criar tabelas)