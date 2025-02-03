import sys
import os
import asyncio ### async
from sqlalchemy.future import select ### async

# Adicionar o caminho do diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conf.config_DB import criar_session # CONSULTA

# ESCOPO BANCO DE DADOS
from models.aditivo_nutritivo import AditivoNutritivo 
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor


# 1 - AditivoNutritivo
async def insert_aditivo_nutritivo(nome=None, formula_quimica=None) -> None:

    async with criar_session() as session:
        try:
            # Se "nome" for "None"
            if not nome:
                return 'Faltou indicar o "nome" do AditivoNutritivo.'
            # Se "formula_quimica" for "None"
            if not formula_quimica:
                return 'Faltou indicar o "formula_quimica" do AditivoNutritivo.'
        
            # dados = (ESCOPO BANCO DE DADOS)
            dados = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)
            
            # Verificar se o "nome" do AditivoNutritivo já existe
            nome_ja_existe = await session.execute(select(AditivoNutritivo).where(AditivoNutritivo.nome == nome))
            resultado_nome = nome_ja_existe.scalars().all() ### async

            # Verificar se o "formula_quimica" do AditivoNutritivo já existe
            formula_quimica_ja_existe = await session.execute(select(AditivoNutritivo).where(AditivoNutritivo.formula_quimica == formula_quimica))
            resultado_formula_quimica = formula_quimica_ja_existe.scalars().all() ### async

            if resultado_nome:
                return f'Nome "{nome}" já esta cadastrado.'
            if resultado_formula_quimica:
                return f'Formula quimica "{formula_quimica}" já esta cadastrado.'
            
            session.add(dados) # CONSULTA
            await session.commit() # CONSULTA

            exibir = (f'\n\
            1 - AditivoNutritivo\n\
            id = {dados.id}\n\
            Data de criação = {dados.data_criacao}\n\
            Nome = {dados.nome}\n\
            Formula quimica = {dados.formula_quimica}\n')
            
            return exibir
    
        except Exception as exception:
            # Reverte a transação caso haja erro
            await session.rollback() # CONSULTA
            raise exception

# <==========================================================>

if __name__ == '__main__':
    resposta_01 = asyncio.run(insert_aditivo_nutritivo(nome='l',formula_quimica='l'))
    print(resposta_01)
