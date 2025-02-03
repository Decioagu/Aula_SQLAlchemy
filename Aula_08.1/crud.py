import asyncio ### async
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession ### async
from sqlalchemy.future import select ### async

from sqlalchemy import create_engine, text, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy import inspect

# ============================================  ENDEREÇO DE CONEXÃO  ============================================
# Primeiro, conectar ao servidor MySQL sem especificar um banco de dados
engine = create_engine('mysql+mysqldb://root:Enigma.1@localhost:3306')

# Criar o banco de dados "cinema" (CASO NÃO EXISTA)
with engine.connect() as connection:
    connection.execute(text("CREATE DATABASE IF NOT EXISTS cinema_03"))

# echo = True:  exibe no console todas as consultas SQL e outras operações que realiza
engine = create_async_engine('mysql+aiomysql://root:Enigma.1@localhost:3306/cinema_03', echo=False) ### async (mysqlclient)
BaseModel = declarative_base() # ORM do SQLAlchemy (classe)

# ===========================================  CONTROLE DE TRANSAÇÕES  ===========================================
# Session: é a classe usada para gerar objetos de sessão
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False) ### async (interagir c/ banco de dados)
session = Session() # interação (inserções, consultas, atualizações e exclusões)

# ======================================  ORM (Object-Relational Mapping)  =======================================
class Filmes(BaseModel):
    __tablename__="filmes"

    titulo = Column(String(25), primary_key=True)
    genero = Column(String(25), nullable=False)
    ano = Column(Integer, nullable=False)

    # __repr__: representa a "classe Filmes" como uma "string"
    def __repr__(self):
        return f"Filme (titulo = {self.titulo}, gênero = {self.genero},ano = {self.ano})"

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
    