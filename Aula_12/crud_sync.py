from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional
from pathlib import Path

# Caminho da pasta para arquivo SQLite
caminho= Path(__file__).parent

# Nome da tabela
nome_tabela = "picoles_sincrono.sqlite"

# Definir a classe Picole
class Picole(SQLModel, table=True):
    nome: str = Field(primary_key=True, index=True)
    sabor: str = Field(nullable=False)

# Criar o banco de dados e a tabela
DATABASE_URL = f"sqlite:///{caminho / nome_tabela}"  # Usando SQLite como exemplo
engine = create_engine(DATABASE_URL)
#Criar tabelas
SQLModel.metadata.create_all(engine)

# Função para criar o banco e as tabelas
def criar_banco():
    SQLModel.metadata.create_all(engine)

# CRUD Operations
def criar_picole(nome: str, sabor: str):
    with Session(engine) as session:
        picole = Picole(nome=nome, sabor=sabor)
        session.add(picole)
        session.commit()
        session.refresh(picole)
        print(f'Picolé "{picole.nome}" criado com sucesso!')
        return picole

def ler_picole(nome: str) -> Optional[Picole]:
    with Session(engine) as session:
        picole = session.get(Picole, nome)
        return picole

def atualizar_picole(nome: str, novo_sabor: str) -> Optional[Picole]:
    with Session(engine) as session:
        picole = session.get(Picole, nome)
        if picole:
            picole.sabor = novo_sabor
            session.commit()
            session.refresh(picole)
            print(f'Picolé "{picole.nome}" atualizado para sabor "{picole.sabor}".')
            return picole
        print(f'Picolé "{nome}" não encontrado.')
        return None

def deletar_picole(id: int):
    with Session(engine) as session:
        picole = session.get(Picole, id)
        if picole:
            session.delete(picole)
            session.commit()
            print(f'Picolé "{id}" deletado com sucesso!')
        else:
            print(f'Picolé "{id}" não encontrado.')

if __name__ == '__main__':

    # Deletar picolé
    deletar_picole("Morango")
    deletar_picole("Limão")
    deletar_picole("Chocolate")

    # Criar o banco de dados e as tabelas
    criar_banco()

    # Criar picolés
    criar_picole("Morango", "Morango")
    criar_picole("Limão", "Limão")
    criar_picole("Chocolate", "Chocolate")

    # Ler picolé
    picole = ler_picole("Morango")
    print(picole)

    # Atualizar picolé
    atualizar_picole("Limão", "Limão com Hortelã")
    atualizar_picole("Chocolate", "Atualizado")

