from typing import List
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from sqlalchemy.orm import Mapped, mapped_column, relationship

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
class BaseModel(DeclarativeBase):
    pass

class Usuario(BaseModel):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)

    pedidos: Mapped[List["Pedido"]] = relationship(
        "Pedido", back_populates="usuario"
    )

class Pedido(BaseModel):
    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    descricao: Mapped[str] = mapped_column(String)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))

    usuario: Mapped["Usuario"] = relationship(
        "Usuario", back_populates="pedidos"
    )


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

    # Criação dos pedidos (USANDO a RELAÇÃO para identificar o usuário)
    pedidos = [
        Pedido(descricao="Notebook Dell", usuario=usuario1),
        Pedido(descricao="Mouse sem fio", usuario=usuario1),
        Pedido(descricao="Teclado mecânico", usuario=usuario1),
        Pedido(descricao='Monitor 27"', usuario=usuario2),
        Pedido(descricao="Cadeira gamer", usuario=usuario2),
        Pedido(descricao="Headset HyperX", usuario=usuario2),
    ]

    # Adiciona tudo à sessão
    session.add_all([usuario1, usuario2])
    session.add_all(pedidos)


    # Confirma as inserções
    session.commit()

    print("\nDados inseridos com sucesso!\n")

    # ======================
    # CONSULTA JOIN AUTOMÁTICA
    # ======================
    consulta_automatica = select(Usuario.nome, Pedido.descricao).join(Usuario.pedidos)
    result = session.execute(consulta_automatica).all()
    print(result)
