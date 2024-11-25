import sys
import os
from sqlmodel import select

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
def insert_aditivo_nutritivo(nome=None, formula_quimica=None) -> None:

    try:
        # Se "nome" for "None"
        if not nome:
            return 'Faltou indicar o "nome" do AditivoNutritivo.'
        # Se "formula_quimica" for "None"
        if not formula_quimica:
            return 'Faltou indicar o "formula_quimica" do AditivoNutritivo.'
    
        # dados = (ESCOPO BANCO DE DADOS)
        dados = AditivoNutritivo(nome=nome, formula_quimica=formula_quimica)

        with criar_session() as session:
            # Verificar se o "nome" do AditivoNutritivo já existe
            filtro_01 = select(AditivoNutritivo).filter(AditivoNutritivo.nome == nome)
            nome_ja_existe = session.exec(filtro_01).first()

            # Verificar se o "formula_quimica" do AditivoNutritivo já existe
            filtro_02 = select(AditivoNutritivo).filter(AditivoNutritivo.formula_quimica == formula_quimica)
            formula_quimica_ja_existe = session.exec(filtro_02).first()

            if nome_ja_existe:
                return f'Nome "{nome}" já esta cadastrado.'
            if formula_quimica_ja_existe:
                return f'Formula quimica "{formula_quimica}" já esta cadastrado.'
            
            session.add(dados) # CONSULTA
            session.commit() # CONSULTA

            exibir = (f'\n\
            id = {dados.id}\n\
            Data de criação = {dados.data_criacao}\n\
            Nome = {dados.nome}\n\
            Formula quimica = {dados.formula_quimica}\n')
            
            return exibir
    
    except Exception as exception:
        # Reverte a transação caso haja erro
        session.rollback() # CONSULTA
        raise exception

    
# <==========================================================>

if __name__ == '__main__':
    resposta_01 =insert_aditivo_nutritivo(nome='b',formula_quimica='w')
    print('1 - AditivoNutritivo')
    print(resposta_01)
