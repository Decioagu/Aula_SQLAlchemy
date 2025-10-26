from typing import List
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker, relationship
from sqlalchemy.orm import Mapped, mapped_column

from pathlib import Path

# Caminho da pasta para arquivo SQLite
caminho= Path(__file__).parent
# Nome da tabela
nome_tabela = "cinema.sqlite"

# ======================
# ENDEREÇO DE CONEXÃO 
# ====================== 
# Criar o banco de dados e a tabela
DATABASE_URL = f"sqlite:///{caminho / nome_tabela}"  # Usando SQLite como exemplo
engine = create_engine(DATABASE_URL)

# ======================
# BANCO E SESSÃO
# ======================
Session = sessionmaker(bind=engine)

# Base principal do ORM moderno
class Base(DeclarativeBase):
    pass

# ==========================
# TABELA FILME_ATOR N:N (Tabela de Associação)
# ==========================
# O nome da tabela deve corresponder ao usado no relacionamento (filmes_ator)
# Usando 'Column' do SQLAlchemy para definir as colunas de uma tabela de associação simples.
filmes_ator = Table(
    "filmes_ator",
    Base.metadata,
    Column("filme_id", ForeignKey("filmes.id"), primary_key=True),
    Column("ator_id", ForeignKey("atores.id"), primary_key=True),
)

# ==========================
# MODELO USUÁRIO (1:N)
# ==========================
class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(80), nullable=False)

    # Um usuário pode ter vários filmes (1:N)
    filmes: Mapped[List["Filme"]] = relationship(back_populates="usuario") # Removido o argumento "Filme", pois é o padrão

    def __repr__(self) -> str:
        return f"<Usuario(nome={self.nome!r})>"


# ==========================
# MODELO FILME (1:N e N:N)
# ==========================
class Filme(Base):
    __tablename__ = "filmes"

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(120), nullable=False)
    genero: Mapped[str] = mapped_column(String(50))
    ano: Mapped[int] = mapped_column(Integer)

    # Relacionamento 1:N → com Usuario (Chave Estrangeira)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    usuario: Mapped[Usuario] = relationship(back_populates="filmes")

    # Relacionamento N:N → com Ator (CORRIGIDO)
    # Usa a tabela 'filmes_ator' como 'secondary'
    atores: Mapped[List["Ator"]] = relationship(
        secondary=filmes_ator,  # Passa a variável Table definida acima
        back_populates="filmes"
    )

    def __repr__(self) -> str:
        return f"<Filme(titulo={self.titulo!r}, ano={self.ano})>"


# ==========================
# MODELO ATOR (N:N)
# ==========================
class Ator(Base):
    __tablename__ = "atores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(80), nullable=False)

    # Relacionamento N:N → com Filmes
    filmes: Mapped[List["Filme"]] = relationship(
        secondary=filmes_ator,  # Usa a mesma variável Table
        back_populates="atores"
    )

    def __repr__(self) -> str:
        return f"<Ator(nome={self.nome!r})>"
    
# ======================
# CRIANDO AS TABELAS
# ======================
Base.metadata.create_all(engine)


with Session() as session:
    usuario = Usuario(nome="Décio")

    filme1 = Filme(titulo="Gladiador", genero="Ação", ano=2000, usuario=usuario)
    filme2 = Filme(titulo="Titanic", genero="Romance", ano=1997, usuario=usuario)

    ator1 = Ator(nome="Russell Crowe")
    ator2 = Ator(nome="Leonardo DiCaprio")

    filme1.atores.append(ator1)
    filme2.atores.append(ator2)

    session.add_all([usuario, filme1, filme2, ator1, ator2])
    session.commit()

    # Exibe filmes e seus atores
    for filme in session.query(Filme).all():
        print(filme, "→ Atores:", filme.atores)
    
    