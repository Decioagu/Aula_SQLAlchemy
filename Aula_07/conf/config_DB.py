import sqlalchemy as banco # CONEXÃO
from sqlalchemy.future.engine import Engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session # CONSULTA

# Usado em SQLite
from pathlib import Path 
import os

from typing import Optional # tipagem

from conf.model_base import ModelBase # ORM do SQLAlchemy (classe)

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

        conn_str = 'sqlite:///' + os.path.join(basedir, 'picoles.sqlite') # tipo de banco
        __engine = banco.create_engine(url=conn_str, echo=False, connect_args={"check_same_thread": False})
    else:
        # Primeiro, conectar ao servidor MySQL sem especificar um banco de dados
        engine =  banco.create_engine('mysql://root:Enigma.1@localhost:3306')

        # Criar o banco de dados "picoles" caso não exista
        with engine.connect() as connection:
            # "banco.text" permite execução de instruções SQL em sqlalchemy
            connection.execute(banco.text("CREATE DATABASE IF NOT EXISTS picoles"))

        # Apontar para o banco de dados desejado
        conn_str = "mysql://root:Enigma.1@localhost:3306/picoles"
        __engine = banco.create_engine(url=conn_str, echo=False)
    
    return __engine

# CONSULTA (Função para criar sessão, consulta ao banco de dados)
def criar_session() -> Session:

    global __engine # ENDEREÇO DE CONEXÃO

    if not __engine:
        criar_banco_de_dados() # MySQL

    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    session: Session = __session() # consulta ao banco de dados

    return session


def criar_tabelas() -> None:

    global __engine # ENDEREÇO DE CONEXÃO

    # Se "ENDEREÇO DE CONEXÃO" não existir
    if not __engine:
        criar_banco_de_dados() # MySQL
        # criar_banco_de_dados(sqlite=True) # SQLite
    
    # >>>>>>>>>> CRIAR TABELAS <<<<<<<<<<<
    import models.__all_models # MODELOS DE TABELAS
    ModelBase.metadata.drop_all(__engine) # apagar tabelas
    ModelBase.metadata.create_all(__engine) # criar tabelas
