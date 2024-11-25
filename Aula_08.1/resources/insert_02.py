import sys
import os
import asyncio ### async
from sqlalchemy.future import select ### async

# Adicionar o caminho do diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conf.config_DB import criar_session # CONSULTA

# ESCOPO BANCO DE DADOS
from models.lote import Lote # Recursos
from models.tipo_picole import TipoPicole # Chave estrangeira

# 8 - Lote
async def insert_lote(id_tipo_picole=None, quantidade=None) -> None:
    print('Décio Santana de Aguiar')
    async with criar_session() as session:
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
        
        #     # dados = (ESCOPO BANCO DE DADOS)
            dados = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

            
        #     # Busque no Banco de Dados "TipoPicole" a chave primária = "id_tipo_picole"
            id_tipo_picole_existe = await session.get(TipoPicole, id_tipo_picole)
                
        #     # Se o "tipo_picole" não existir
            if not id_tipo_picole_existe:
                return f'\nTipo de picole com id = "{id_tipo_picole}" não esta cadastrado.\n'
            
            session.add(dados) # CONSULTA
            await session.commit() # CONSULTA

            exibir = (f'\n\
            8 - Lote\n\
            id = {dados.id}\n\
            data_criacao = {dados.data_criacao}\n\
            quantidade = {dados.quantidade}\n\
            nome tipo picole = {dados.tipo_picole.nome}\n')
            
            return exibir
        
        except Exception as exception:
            # Reverte a transação caso haja erro
            await session.rollback() # CONSULTA
            raise exception

if __name__ == '__main__':

    resposta_08 =asyncio.run(insert_lote(id_tipo_picole=2,quantidade=7))
    print(resposta_08)
    