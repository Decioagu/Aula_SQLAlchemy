import sys
import os

# Adicionar o caminho do diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conf.config_DB import criar_session # CONSULTA

# ESCOPO BANCO DE DADOS
from models.lote import Lote
from models.tipo_picole import TipoPicole

# 8 - Lote
def insert_lote(id_tipo_picole=None, quantidade=None) -> None:

    try:
        # Verifica se "quantidade" pode ser convertido para int
        try:
            quantidade = int(quantidade)
        except ValueError:
            return "Valor inválido. Insira apenas valores numéricos inteiro."
            
        # Se "id_tipo_picole" for "None"
        if not id_tipo_picole:
            return 'Faltou indicar o "id_tipo_picole" no Lote.'
        # Se "quantidade" for "None"
        if not quantidade:
            return 'Faltou indicar o "quantidade" no Lote.'
    
        # dados = (ESCOPO BANCO DE DADOS)
        dados = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

        with criar_session() as session:
            
            # Busque no Banco de Dados "TipoPicole" a chave primária = "id_tipo_picole"
            id_tipo_picole_existe = session.get(TipoPicole, id_tipo_picole)
                
            # Se o "tipo_picole" não existir
            if not id_tipo_picole_existe:
                return f'\nTipo de picole com id = "{id_tipo_picole}" não esta cadastrado.\n'
            
            session.add(dados) # CONSULTA
            session.commit() # CONSULTA

            exibir = (f'\n\
            id = {dados.id}\n\
            data_criacao = {dados.data_criacao}\n\
            quantidade = {dados.quantidade}\n\
            nome tipo picole = {dados.tipo_picole.nome}\n')
            
            return exibir
    
    except Exception as exception:
        # Reverte a transação caso haja erro
        session.rollback() # CONSULTA
        raise exception

if __name__ == '__main__':

    resposta_08 =insert_lote(id_tipo_picole=2,quantidade=7)
    print('8 - Lote')
    print(resposta_08)


