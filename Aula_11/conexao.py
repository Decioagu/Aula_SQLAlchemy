from sqlmodel import SQLModel, Field, Relationship, create_engine, Session, text
from typing import Optional, List

from pathlib import Path 

# ------------------------------ SQL --------------------------------
# endereço da pasta atual
caminho_do_arquivo = Path(__file__).parent # ver caminho do arquivo executado # ver caminho do arquivo executado
nome_tabela = "teste_picoles.sqlite"
# ----------------------------------------------------------------------


# ------------------------------ MySQL --------------------------------
# Primeiro, conectar ao servidor MySQL sem especificar um banco de dados
engine = create_engine('mysql+mysqldb://root:Enigma.1@localhost:3306')

# Criar o banco de dados "cinema" caso não exista
with engine.connect() as connection:
    connection.execute(text("CREATE DATABASE IF NOT EXISTS teste_11")) # Apontar para o banco de dados desejado
# ----------------------------------------------------------------------

# Configuração do banco de dados
sqlite_url = (f'sqlite:///{caminho_do_arquivo / nome_tabela}')
# sqlite_url = ('mysql://root:Enigma.1@localhost:3306/teste_11')
# sqlite_url = ('postgresql://Enigma.1:senha@localhost:5432/teste_11')

engine = create_engine(sqlite_url)

# Tabela User
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    posts: List["Post"] = Relationship(back_populates="user")  # Relacionamento

# Tabela Post
class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    user_id: int = Field(foreign_key="user.id")  # Chave estrangeira
    user: User = Relationship(back_populates="posts")  # Relacionamento reverso

#Criar tabelas
SQLModel.metadata.create_all(engine)

# Criar sessão para interagir com o banco de dados
with Session(engine) as session:
    # Criar um novo usuário
    new_user = User(name="John Doe", email="john.doe@example.com")
    session.add(new_user)
    session.commit()
    session.refresh(new_user)  # Atualiza o objeto com o ID gerado

    # Criar posts para o usuário
    post1 = Post(title="Primeiro Post", content="Conteúdo do primeiro post", user_id=new_user.id)
    post2 = Post(title="Segundo Post", content="Conteúdo do segundo post", user_id=new_user.id)

    session.add_all([post1, post2])
    session.commit()

# Recuperar dados e acessar os relacionamentos
with Session(engine) as session:
    user = session.get(User, 1)  # Buscar usuário com ID=1
    print(f"Usuário: {user.name}, Email: {user.email}")
    for post in user.posts:
        print(f"Post: {post.title}, Conteúdo: {post.content}")
