from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import create_engine, select
from sqlalchemy.orm import declarative_base, Session, sessionmaker

'''Modelagem SQLAlchemy 1 - Sem Mapped'''

from pathlib import Path

# ======================
# ENDEREÇO DE CONEXÃO 
# ====================== 
engine = create_engine("sqlite:///:memory:")


# ======================
# BANCO E SESSÃO
# ======================
Session = sessionmaker(bind=engine)

# ======================
# MODELAGEM DO BANCO DE DADOS
# ======================
BaseModel = declarative_base()

class Usuario(BaseModel):
    __tablename__ = "usuarios"

    id: int = Column(Integer, primary_key=True)
    nome: str = Column(String, nullable=False)

class Pedido(BaseModel):
    __tablename__ = "pedidos"

    id: int = Column(Integer, primary_key=True)
    descricao: str = Column(String)
    usuario_id: int = Column(ForeignKey("usuarios.id"))

# ======================
# CRIANDO AS TABELAS
# ======================
BaseModel.metadata.create_all(engine)

# ======================
# INSERÇÃO DE DADOS
# ======================
with Session() as session:
    # Criação dos usuários
    usuario1 = Usuario(nome="Alice")
    usuario2 = Usuario(nome="Bruno")

    # Criação dos pedidos (SEM RELAÇÃO, Usando ID para identificar o usuário)
    pedidos = [
        Pedido(descricao="Notebook Dell", usuario_id=1),
        Pedido(descricao="Mouse sem fio", usuario_id=1),
        Pedido(descricao="Teclado mecânico", usuario_id=1),
        Pedido(descricao='Monitor 27"', usuario_id=2),
        Pedido(descricao="Cadeira gamer", usuario_id=2),
        Pedido(descricao="Headset HyperX", usuario_id=2),
    ]

    # Adiciona tudo à sessão
    session.add_all([usuario1, usuario2])
    session.add_all(pedidos)


    # Confirma as inserções
    session.commit()

    print("\nDados inseridos com sucesso!\n")

    # ======================
# CONSULTA JOIN MANUAL (explícita)
# ======================
consulta_manual = (select(Usuario.nome, Pedido.descricao).join(Pedido, Pedido.usuario_id == Usuario.id))

result = session.execute(consulta_manual).all()
print(result)  # [('Alice', 'Pedido A'), ('Alice', 'Pedido B')]

session.close()