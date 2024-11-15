import asyncio
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# endereço de conexão assíncrona
engine = create_async_engine('mysql+aiomysql://root:Enigma.3@localhost:3306/cinema_03', echo=True)
BaseModel = declarative_base()

# Configuração da sessão assíncrona
async_session = sessionmaker(
    bind=engine, 
    expire_on_commit=False, 
    class_=AsyncSession
)

# ORM (Object-Relational Mapping)
class Filmes(BaseModel):
    __tablename__ = "filmes"
    titulo = Column(String(25), primary_key=True)
    genero = Column(String(25), nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Filme (titulo={self.titulo}, gênero={self.genero}, ano={self.ano})"

# ============================================  CRUD  ============================================

# CREATE
async def post_filme(_titulo_: str, _genero_: str, _ano_: int):
    async with async_session() as session:
        async with session.begin():
            try:
                inserir_dados = Filmes(titulo=_titulo_, genero=_genero_, ano=_ano_)
                titulo_ja_existe = await session.get(Filmes, _titulo_)

                if titulo_ja_existe:
                    print(f'Título "{_titulo_}" já está cadastrado.')
                    return

                session.add(inserir_dados)
                await session.commit()
                print(f"POST: Filme {_titulo_} inserido com sucesso!")

            except SQLAlchemyError as e:
                print("POST:")
                print(f"Ocorreu um erro ao interagir com o banco de dados: {e}")
                await session.rollback()

# READ
async def get_filmes_01():
    async with async_session() as session:
        async with session.begin():
            busca_filme = await session.execute(Filmes.__table__.select())
            filmes = busca_filme.scalars().all()
            print("GET 01:")
            for filme in filmes:
                print(filme)

# UPDATE
async def update_filme_01(filme_titulo: str, ano: int):
    async with async_session() as session:
        async with session.begin():
            filme_existente = await session.get(Filmes, filme_titulo)
            if filme_existente:
                filme_existente.ano = ano
                await session.commit()
                print(f"UPDATE: Filme '{filme_titulo}' atualizado com sucesso!")
            else:
                print(f"UPDATE: Filme '{filme_titulo}' não encontrado para atualizar.")

# DELETE
async def delete_filme(filme_titulo: str):
    async with async_session() as session:
        async with session.begin():
            filme_existente = await session.get(Filmes, filme_titulo)
            if filme_existente:
                await session.delete(filme_existente)
                await session.commit()
                print(f"DELETE: Filme '{filme_titulo}' deletado com sucesso!")
            else:
                print(f"DELETE: Filme '{filme_titulo}' não encontrado para deletar.")

# Função principal para executar operações assíncronas
async def main():
    # await get_filmes_01()
    await post_filme('Homens de honra', "Ação/Drama", 2001)
    # await get_filmes_01()
    # await update_filme_01("Homens de honra", 2002)
    # await delete_filme("Homens de honra")
    # await get_filmes_01()

# Executar as operações
asyncio.run(main())
