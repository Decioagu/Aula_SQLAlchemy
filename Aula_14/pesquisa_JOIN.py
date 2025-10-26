from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey, create_engine, select
from sqlalchemy.orm import declarative_base, relationship, Session

# ======================
# CONEXÃO AO BANCO
# ======================
engine = create_engine("sqlite:///:memory:")

# ======================
# BANCO E SESSÃO
# ======================
session = Session(engine)

# ======================
# MODELAGEM DO BANCO
# ======================
BaseModel = declarative_base()

class Usuario(BaseModel):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

    # Relacionamento 1:N (um usuário tem vários pedidos)
    pedidos = relationship("Pedido", back_populates="usuario")

class Pedido(BaseModel):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True)
    descricao = Column(String)
    usuario_id = Column(ForeignKey("usuarios.id"))

    # Lado oposto do relacionamento
    usuario = relationship("Usuario", back_populates="pedidos")

# ======================
# CRIANDO AS TABELAS
# ======================
BaseModel.metadata.create_all(engine)

# ======================
# INSERÇÃO DE DADOS
# ======================
u1 = Usuario(nome="Alice")
p1 = Pedido(descricao="Pedido A", usuario=u1)
p2 = Pedido(descricao="Pedido B", usuario=u1)

session.add_all([u1, p1, p2])
session.commit()

# ======================
# CONSULTA JOIN AUTOMÁTICA
# ======================
# Agora não precisamos mais informar a condição do join:
consulta_automatica = select(Usuario.nome, Pedido.descricao).join(Usuario.pedidos)

result = session.execute(consulta_automatica).all()
print(result)  # [('Alice', 'Pedido A'), ('Alice', 'Pedido B')]

# ======================
# CONSULTA JOIN MANUAL (explícita)
# ======================
consulta_manual = (select(Usuario.nome, Pedido.descricao).join(Pedido, Pedido.usuario_id == Usuario.id))

result = session.execute(consulta_manual).all()
print(result)  # [('Alice', 'Pedido A'), ('Alice', 'Pedido B')]

session.close()