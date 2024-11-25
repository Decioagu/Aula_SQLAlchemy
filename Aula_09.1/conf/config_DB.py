from sqlmodel import SQLModel, Session, create_engine, text
from sqlalchemy.future.engine import Engine

# Usado em SQLite
from pathlib import Path 
import os

from typing import Optional # tipagem

# ENDEREÇO DE CONEXÃO
__engine: Optional[Engine] = None

# CONEXÃO (Função para configurar a conexão ao banco de dados)
def criar_banco_de_dados(sqlite: bool = False) -> Engine:

    global __engine # ENDEREÇO DE CONEXÃO

    # Se "ENDEREÇO DE CONEXÃO" existir
    if __engine:
        return # retorne
    
    if sqlite:
        # endereço da pasta atual
        caminho_do_arquivo = Path(__file__) # ver caminho do arquivo executado
        basedir = os.path.abspath(os.path.dirname(caminho_do_arquivo.parent))

        conn_str = 'sqlite:///' + os.path.join(basedir, 'picoles_02.sqlite') # tipo de banco
        __engine = create_engine(url=conn_str, echo=False, connect_args={"check_same_thread": False})
    else:
        # # Primeiro, conectar ao servidor MySQL sem especificar um banco de dados
        # engine =  create_engine('mysql://root:Enigma.3@localhost:3306')

        # # Criar o banco de dados "picoles_02" caso não exista
        # with engine.connect() as connection:
        #     # "banco.text" permite execução de instruções SQL em sqlalchemy
        #     connection.execute(text("CREATE DATABASE IF NOT EXISTS picoles_02"))

        # Apontar para o banco de dados desejado
        conn_str = "mysql://root:Enigma.3@localhost:3306/picoles_02"
        __engine = create_engine(url=conn_str, echo=False)
    
    return __engine

# CONSULTA (Função para criar sessão, consulta ao banco de dados)
def criar_session() -> Session:

    global __engine # ENDEREÇO DE CONEXÃO

    if not __engine:
        criar_banco_de_dados() # MySQL

    session = Session(__engine) # consulta ao banco de dados

    return session


def criar_tabelas() -> None:

    global __engine # ENDEREÇO DE CONEXÃO

    # Se "ENDEREÇO DE CONEXÃO" não existir
    if not __engine:
        criar_banco_de_dados() # MySQL
        # criar_banco_de_dados(sqlite=True) # SQLite
    
    # >>>>>>>>>> CRIAR TABELAS <<<<<<<<<<<
    import models.__all_models # MODELOS DE TABELAS
    SQLModel.metadata.drop_all(__engine) # apagar tabelas
    SQLModel.metadata.create_all(__engine) # criar tabelas
