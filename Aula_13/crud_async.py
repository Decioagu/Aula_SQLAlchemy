from sqlmodel import SQLModel, Field, select
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from typing import Optional
from pathlib import Path
import asyncio

# Caminho da pasta para arquivo SQLite
caminho = Path(__file__).parent
nome_tabela = "picoles_assincrono.sqlite"
DATABASE_URL = f"sqlite+aiosqlite:///{caminho / nome_tabela}"  # Usando SQLite assíncrono
engine = create_async_engine(DATABASE_URL)

# Definir a classe Picole
class Picole(SQLModel, table=True):
    nome: str = Field(primary_key=True, index=True)
    sabor: str = Field(nullable=False)

# Função para criar o banco e as tabelas
async def criar_banco():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

# CRUD Operations
async def criar_picole(nome: str, sabor: str):
    async with AsyncSession(engine) as session:
        picole = Picole(nome=nome, sabor=sabor)
        session.add(picole)
        await session.commit()
        await session.refresh(picole)
        print(f'Picolé "{picole.nome}" criado com sucesso!')
        return picole

async def ler_picole(nome: str) -> Optional[Picole]:
    async with AsyncSession(engine) as session:
        result = await session.exec(select(Picole).where(Picole.nome == nome))
        return result.first()

async def atualizar_picole(nome: str, novo_sabor: str) -> Optional[Picole]:
    async with AsyncSession(engine) as session:
        result = await session.exec(select(Picole).where(Picole.nome == nome))
        picole = result.first()
        if picole:
            picole.sabor = novo_sabor
            await session.commit()
            await session.refresh(picole)
            print(f'Picolé "{picole.nome}" atualizado para sabor "{picole.sabor}".')
            return picole
        print(f'Picolé "{nome}" não encontrado.')
        return None

async def deletar_picole(nome: str):
    async with AsyncSession(engine) as session:
        result = await session.exec(select(Picole).where(Picole.nome == nome))
        picole = result.first()
        if picole:
            await session.delete(picole)
            await session.commit()
            print(f'Picolé "{nome}" deletado com sucesso!')
        else:
            print(f'Picolé "{nome}" não encontrado.')

async def main():
    # Criar banco de dados
    await criar_banco()

    # Deletar picolés (caso existam)
    await deletar_picole("Morango")
    await deletar_picole("Limão")
    await deletar_picole("Chocolate")

    # Criar picolés
    await criar_picole("Morango", "Morango")
    await criar_picole("Limão", "Limão")
    await criar_picole("Chocolate", "Chocolate")

    # Ler picolé
    picole = await ler_picole("Morango")
    print(picole)

    # Atualizar picolé
    await atualizar_picole("Limão", "Limão com Hortelã")
    await atualizar_picole("Chocolate", "Atualizado")

if __name__ == '__main__':
    asyncio.run(main())
