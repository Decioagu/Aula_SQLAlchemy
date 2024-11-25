from sqlmodel import SQLModel, Field, Session, create_engine, select, text

# Primeiro, conectar ao servidor MySQL sem especificar um banco de dados
# engine = create_engine('mysql+mysqldb://root:Enigma.3@localhost:3306')

# Criar o banco de dados "cinema" caso não exista
# with engine.connect() as connection:
#     connection.execute(text("CREATE DATABASE IF NOT EXISTS cinema_09")) # Apontar para o banco de dados desejado

# Apontar para o banco de dados desejado
engine = create_engine('mysql://root:Enigma.3@localhost:3306/cinema_09')
# engine = create_engine('postgresql://Enigma.3:senha@localhost:5432/teste')

# ORM (Object-Relational Mapping)
class Filmes(SQLModel, table=True):
    __tablename__: str = 'filmes'
    titulo: str = Field(max_length = 3, primary_key=True)
    genero: str = Field(max_length = 3)
    ano: int = Field()

# cria a tabela após modelagem da classe "Filmes"
# SQLModel.metadata.drop_all(engine) # apagar tabelas
# SQLModel.metadata.create_all(engine) # criar tabelas

# Criar uma instância de um filme
novo_filme = Filmes(titulo="sss", ano=2001, genero="sss")

# CREATE
with Session(engine) as session:
    try:
        session.add(novo_filme)  # Adiciona o filme à sessão
        session.commit()         # Salva as alterações no banco de dados
        print()
        print("Filme adicionado com sucesso!")
        print()
    except Exception as exception:
        print()
        print("Filme adicionado já existe!")
        print()
        session.rollback() # CONSULTA

# READ
with Session(engine) as session:
    filtro = select(Filmes)
    filtro_filmes = session.exec(filtro).all()
    for filme in filtro_filmes:
        print(filme)