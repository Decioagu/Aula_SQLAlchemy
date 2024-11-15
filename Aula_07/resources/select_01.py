import sys
import os

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
        dados = session.query(AditivoNutritivo).all()
        
        for filme in dados:
            print(filme) # __repr__
    
selecionar_aditivos_nutritivos()

