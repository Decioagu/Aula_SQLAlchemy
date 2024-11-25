from sqlmodel import Field, SQLModel, Relationship
from decimal import Decimal

from datetime import datetime
from typing import List, Optional

from models.sabor import Sabor # Chave estrangeira e relacionamento
from models.tipo_embalagem import TipoEmbalagem # Chave estrangeira e relacionamento
from models.tipo_picole import TipoPicole # Chave estrangeira e relacionamento

from models.ingrediente import Ingrediente # chave estrangeira para nova (tabela "secundaria")
from models.conservante import Conservante # chave estrangeira para nova (tabela "secundaria")
from models.aditivo_nutritivo import AditivoNutritivo # chave estrangeira para nova (tabela "secundaria")


# Picolé pode ter vários ingredientes (muitos-para-muitos)
class IngredientesPicole(SQLModel, table = True):
    id_picole: int = Field(foreign_key='picoles.id')
    id_ingrediente: int = Field(foreign_key='ingredientes.id')


# Picolé pode ter vários conservantes (muitos-para-muitos)
class ConservantesPicole(SQLModel, table = True):
    id_picole: int = Field(foreign_key=('picoles.id'))
    id_conservante: int = Field(foreign_key=('conservantes.id'))


# Picole pode ter vários aditivos nutritivos (muitos-para-muitos)
class AditivosNutritivosPicole(SQLModel, table = True):
    id_picole: int = Field(foreign_key=('picoles.id'))
    id_aditivo_nutritivo: int = Field(foreign_key=('aditivos_nutritivos.id'))


class Picole(SQLModel, table = True):
    # ESCOPO BANCO DE DADOS
    id: Optional[int] = Field(default=None, primary_key=True)
    data_criacao: datetime = Field(default=datetime.now(), index=True)
    preco: Decimal = Field(max_digits=8, decimal_places=2) # https://sqlmodel.tiangolo.com/advanced/decimal/

    id_sabor: int = Field(foreign_key='sabores.id') # chave estrangeira 
    sabor: Sabor = Relationship(back_populates='sabores', sa_relationship_kwargs={'lazy':'joined'}) # Relacionamento

    id_tipo_embalagem: int = Field(foreign_key='tipos_embalagem.id') # chave estrangeira 
    tipo_embalagem: TipoEmbalagem = Relationship(back_populates='tipos_embalagem', sa_relationship_kwargs={'lazy':'joined'}) # Relacionamento

    id_tipo_picole: int = Field(foreign_key='tipos_picole.id') # chave estrangeira 
    tipo_picole: TipoPicole = Relationship(back_populates='tipos_picole', sa_relationship_kwargs={'lazy':'joined'}) # Relacionamento

    # Um picole pode ter vários ingredientes (tabela "secundaria")
    ingredientes: List[Ingrediente] = Relationship(link_model=IngredientesPicole, back_populates = 'ingredientes', sa_relationship_kwargs={'lazy':'joined'})

    # Um picolé pode ter vários conservantes ou mesmo nenhum (tabela "secundaria")
    conservantes: Optional[List[Conservante]] = Relationship(link_model=ConservantesPicole, back_populates = 'conservantes', sa_relationship_kwargs={'lazy':'joined'})

    # Um picole pode ter vários aditivos nutritivos ou mesmo nenhum (tabela "secundaria")
    aditivos_nutritivos: Optional[List[AditivoNutritivo]] = Relationship(link_model=AditivosNutritivosPicole, back_populates = 'aditivos_nutritivos', sa_relationship_kwargs={'lazy':'joined'})

    def __repr__(self) -> str:
        return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}>'

