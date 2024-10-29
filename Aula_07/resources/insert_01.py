import sys
import os

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
            nome_ja_existe = session.query(AditivoNutritivo).filter(AditivoNutritivo.nome == nome).first()

            # Verificar se o "formula_quimica" do AditivoNutritivo já existe
            formula_quimica_ja_existe = session.query(AditivoNutritivo).filter(AditivoNutritivo.formula_quimica == formula_quimica).first()

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

# 2 - Sabor
def insert_sabor(nome=None) -> None:

    try:
        # Se "nome" for "None"
        if not nome:
            return 'Faltou indicar o "nome" do Sabor.'
    
        # dados = (ESCOPO BANCO DE DADOS)
        dados = Sabor(nome=nome)

        with criar_session() as session:
            # Verificar se o "nome" do Sabor já existe
            nome_ja_existe = session.query(Sabor).filter(Sabor.nome == nome).first()

            if nome_ja_existe:
                return f'Nome "{nome}" já esta cadastrado.'
            
            session.add(dados) # CONSULTA
            session.commit() # CONSULTA  

            exibir = (f'\n\
            id = {dados.id}\n\
            Data de criação = {dados.data_criacao}\n\
            Nome = {dados.nome}\n')

            return exibir

    except Exception as exception:
        # Reverte a transação caso haja erro
        session.rollback() # CONSULTA
        raise exception
    
# <==========================================================>

# 3 - TipoEmbalagem
def insert_tipo_embalagem(nome=None) -> None:

    try:
        # Se "nome" for "None"
        if not nome:
            return 'Faltou indicar o "nome" do TipoEmbalagem.'
    
        # dados = (ESCOPO BANCO DE DADOS)
        dados = TipoEmbalagem(nome=nome)

        with criar_session() as session:
            # Verificar se o "nome" do TipoEmbalagem já existe
            nome_ja_existe = session.query(TipoEmbalagem).filter(TipoEmbalagem.nome == nome).first()

            if nome_ja_existe:
                return f'Nome "{nome}" já esta cadastrado.'
            
            session.add(dados) # CONSULTA
            session.commit() # CONSULTA 
                
            exibir = (f'\n\
            id = {dados.id}\n\
            Data de criação = {dados.data_criacao}\n\
            Nome = {dados.nome}\n')

            return exibir 
        
    except Exception as exception:
        # Reverte a transação caso haja erro
        session.rollback() # CONSULTA
        raise exception

# <==========================================================>

# 4 - TipoPicole
def insert_tipo_picole(nome=None) -> None:

    try:
        # Se "nome" for "None"
        if not nome:
            return 'Faltou indicar o "nome" do TipoPicole.'
    
        # dados = (ESCOPO BANCO DE DADOS)
        dados = TipoPicole(nome=nome)

        with criar_session() as session:
            # Verificar se o "nome" do TipoPicole já existe
            nome_ja_existe = session.query(TipoPicole).filter(TipoPicole.nome == nome).first()

            if nome_ja_existe:
                return f'Nome "{nome}" já esta cadastrado.'
            
            session.add(dados) # CONSULTA
            session.commit() # CONSULTA  

            exibir = (f'\n\
            id = {dados.id}\n\
            Data de criação = {dados.data_criacao}\n\
            Nome = {dados.nome}\n')

            return exibir

    except Exception as exception:
        # Reverte a transação caso haja erro
        session.rollback() # CONSULTA
        raise exception
    
# <==========================================================>
    
# 5 - Ingrediente
def insert_ingrediente(nome=None) -> None:

    try:
        # Se "nome" for "None"
        if not nome:
            return 'Faltou indicar o "nome" do Ingrediente.'
    
        # dados = (ESCOPO BANCO DE DADOS)
        dados = Ingrediente(nome=nome)

        with criar_session() as session:
            # Verificar se o "nome" do Ingrediente já existe
            nome_ja_existe = session.query(Ingrediente).filter(Ingrediente.nome == nome).first()

            if nome_ja_existe:
                return f'Nome "{nome}" já esta cadastrado.'
            
            session.add(dados) # CONSULTA
            session.commit() # CONSULTA  

            exibir = (f'\n\
            id = {dados.id}\n\
            Data de criação = {dados.data_criacao}\n\
            Nome = {dados.nome}\n')

            return exibir
        
    except Exception as exception:
        # Reverte a transação caso haja erro
        session.rollback() # CONSULTA
        raise exception

# <==========================================================>

# 6 - Conservante
def insert_conservante(nome=None, descricao=None) -> None:

    try:
        # Se "nome" for "None"
        if not nome:
            return 'Faltou indicar o "nome" do Conservante.'
        # Se "descricao" for "None"
        if not descricao:
            return 'Faltou indicar o "descricao" do Conservante.'
    
        # dados = (ESCOPO BANCO DE DADOS)
        dados = Conservante(nome=nome, descricao=descricao)

        with criar_session() as session:
            # Verificar se o "nome" do Conservante já existe
            nome_ja_existe = session.query(Conservante).filter(Conservante.nome == nome).first()

            # Verificar se o "formula_quimica" do Conservante já existe
            descricao_ja_existe = session.query(Conservante).filter(Conservante.descricao == descricao).first()

            if nome_ja_existe:
                return f'Nome "{nome}" já esta cadastrado.'
            if descricao_ja_existe:
                return f'Formula quimica "{descricao}" já esta cadastrado.'
            
            session.add(dados) # CONSULTA
            session.commit() # CONSULTA

            exibir = (f'\n\
            id = {dados.id}\n\
            Data de criação = {dados.data_criacao}\n\
            Nome = {dados.nome}\n\
            Descrição = {dados.descricao}\n')
    
            return exibir
    
    except Exception as exception:
        # Reverte a transação caso haja erro
        session.rollback() # CONSULTA
        raise exception

    

# <==========================================================>

# 7 - Revendedor
def insert_revendedor(cnpj=None, razao_social=None, contato=None) -> None:

    try:
        # Se "cnpj" for "None"
        if not cnpj:
            return 'Faltou indicar o "cnpj" do Revendedor.'
        # Se "razao_social" for "None"
        if not razao_social:
            return 'Faltou indicar o "razão social" do Revendedor.'
        # Se "contato" for "None"
        if not contato:
            return 'Faltou indicar o "contato" do Revendedor.'

    
        # dados = (ESCOPO BANCO DE DADOS)
        dados = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

        with criar_session() as session:
            # Verificar se o "cnpj" do Revendedor já existe
            cnpj_ja_existe = session.query(Revendedor).filter(Revendedor.cnpj == cnpj).first()
            # Verificar se o "razao_social" do Revendedor já existe
            razao_social_ja_existe = session.query(Revendedor).filter(Revendedor.razao_social ==razao_social).first()
            # Verificar se o "contato" do Revendedor já existe
            contato_ja_existe = session.query(Revendedor).filter(Revendedor.contato == contato).first()

            if cnpj_ja_existe:
                return f'CNPJ "{cnpj}" já esta cadastrado.'
            if razao_social_ja_existe:
                return f'Razão social "{razao_social}" já esta cadastrado.'
            if contato_ja_existe:
                return f'Contato "{contato}" já esta cadastrado.'
            
            session.add(dados) # CONSULTA
            session.commit() # CONSULTA

            exibir = (f'\n\
            id = {dados.id}\n\
            Data de criação = {dados.data_criacao}\n\
            CNPJ = {dados.cnpj}\n\
            Razão Social = {dados.razao_social}\n\
            Contato = {dados.contato}\n')
            
            return exibir
    
    except Exception as exception:
        # Reverte a transação caso haja erro
        session.rollback() # CONSULTA
        raise exception

    

# <==========================================================>

if __name__ == '__main__':
    resposta_01 =insert_aditivo_nutritivo(nome='x',formula_quimica='x')
    print('1 - AditivoNutritivo')
    print(resposta_01)

    resposta_02 =insert_sabor('x')
    print('2 - Sabor')
    print(resposta_02)

    resposta_03 =insert_tipo_embalagem(nome='x')
    print('3 - TipoEmbalagem')
    print(resposta_03)

    resposta_04 =insert_tipo_picole(nome='x')
    print('4 - TipoPicole')
    print(resposta_04)

    resposta_05 =insert_ingrediente(nome='x')
    print('5 - Ingrediente')
    print(resposta_05)

    resposta_06 =insert_conservante(nome='o',descricao='o')
    print('6 - Conservante')
    print(resposta_06)

    resposta_07 =insert_revendedor(cnpj='p',razao_social='p',contato='p')
    print('7 - Revendedor')
    print(resposta_07)
