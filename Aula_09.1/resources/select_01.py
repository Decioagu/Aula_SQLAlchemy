import sys
import os
from sqlmodel import select

# Adicionar o caminho do diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conf.config_DB import criar_session # CONSULTA

# ESCOPO BANCO DE DADOS
from models.aditivo_nutritivo import AditivoNutritivo 

# Função para realizar o select
def selecionar_aditivos_nutritivos():
    # Obtenha a sessão de conexão com o banco de dados
    with criar_session() as session:
        
        # Consulta na tabela "aditivos_nutritivos"
        filtro = select(AditivoNutritivo)
        dados = session.exec(filtro).all()
        
        for aditivo in dados:
            print(aditivo) # __repr__
    
selecionar_aditivos_nutritivos()

