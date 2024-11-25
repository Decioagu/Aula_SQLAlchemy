from sqlalchemy import Column, String, Integer

import os
import sys
# Adicionar o caminho do diretório pai ao (sys.path)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conf.conexao import BaseModel ### sys.path

# ======================================  ORM (Object-Relational Mapping)  =======================================
class Filmes(BaseModel):
    __tablename__="filmes"

    titulo = Column(String(25), primary_key=True)
    genero = Column(String(25), nullable=False)
    ano = Column(Integer, nullable=False)

    # __repr__: representa a "classe Filmes" como uma "string"
    def __repr__(self):
        return f"Filme (titulo = {self.titulo}, gênero = {self.genero},ano = {self.ano})"