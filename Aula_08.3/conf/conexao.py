from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession ### async

from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

from sqlalchemy import inspect # inspecionar tabela existente

# ============================================  ENDEREÇO DE CONEXÃO  ============================================
# Primeiro, conectar ao servidor MySQL sem especificar um banco de dados
engine = create_engine('mysql+mysqldb://root:Enigma.3@localhost:3306')

# Criar o banco de dados "cinema" (CASO NÃO EXISTA)
with engine.connect() as connection:
    connection.execute(text("CREATE DATABASE IF NOT EXISTS cinema_03"))

# echo = True:  exibe no console todas as consultas SQL e outras operações que realiza
engine = create_async_engine('mysql+aiomysql://root:Enigma.3@localhost:3306/cinema_03', echo=False) ### async (mysqlclient)
BaseModel = declarative_base() # ORM do SQLAlchemy (classe)

# ===========================================  CONTROLE DE TRANSAÇÕES  ===========================================
# Session: é a classe usada para gerar objetos de sessão
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False) ### async (interagir c/ banco de dados)
session = Session() # interação (inserções, consultas, atualizações e exclusões)

# ======================================  CRIAR TABELA APOS MODELAGEM  =======================================
# Função para verificar a existência de uma tabela em um contexto assíncrono
async def tabela_existe(engine, nome_tabela: str) -> bool:
    async with engine.connect() as conn:
        # Usa run_sync para chamar o inspetor de forma síncrona
        return await conn.run_sync(lambda sync_conn: inspect(sync_conn).has_table(nome_tabela))

# cria a tabela após modelagem da classe "Filmes" (CASO NÃO EXISTA)
async def criar_tables(engine):
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)

