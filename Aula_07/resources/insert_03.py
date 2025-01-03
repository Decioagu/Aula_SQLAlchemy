import sys
import os

# Adicionar o caminho do diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conf.config_DB import criar_session # CONSULTA

# ESCOPO BANCO DE DADOS
from models.nota_fiscal import NotaFiscal # Recursos
from models.revendedor import Revendedor # Chave estrangeira
from models.lote import Lote # Chave estrangeira para (tabela "secundaria")

# 9 - Nota Fiscal
def insert_nota_fiscal() -> None:

    try:
        
        with criar_session() as session: 
            # ===================================================================
            print('\n09 - Nota Fiscal\n')
            ### NotaFiscal ###
            valor : float = input('Informe o valor da nota fiscal: ')

            # Se "valor" não for informado
            if valor == '':
                return 'Valor da nota fiscal não pode ficar em branco.'

            # Verifica se "valor" pode ser convertido para float
            try:
                valor = float(valor)
            except ValueError:
                return "Valor inválido. Insira apenas valores numéricos."
            # ===================================================================
            ### NotaFiscal ###
            numero_serie: str = input('Informe o número de serie da nota fiscal: ')

            # Se "numero_serie" não for informado
            if numero_serie == '':
                return 'Número de serie da nota fiscal não pode ficar em branco.'

            pesquisa = session.query(NotaFiscal).filter(NotaFiscal.numero_serie == numero_serie).first()
            
            # Se "numero_serie" não for informado
            if pesquisa:
                return 'Número de serie já foi cadastrado.'
            # ===================================================================
            ### NotaFiscal ###
            descricao: str = input('Faça uma descrição da nota fiscal: ')
                
            # Se "descricao" não for informado
            if descricao == '':
                return 'Descrição da nota fiscal não pode ficar em branco.'
            # ===================================================================
            ### Revendedor ###
            id_revendedor: int = input('Informe o ID do revendedor: ')

            # Se "id_revendedor" não for informado
            if id_revendedor == '':
                return 'ID do revendedor não pode ficar em branco.'

            # Verifica se "id_revendedor" pode ser convertido para int
            try:
                id_revendedor = int(id_revendedor)
            except ValueError:
                return "Valor inválido. Insira apenas valores numéricos."
            
            # Verificar se o "id_revendedor" já existe
            revendedor = session.get(Revendedor, id_revendedor)
                
            # Se o "revendedor" não existir
            if not revendedor:
                return f'\nSabor com id = "{id_revendedor}" não esta cadastrado.\n'
            # ===================================================================

            # dados = (ESCOPO BANCO DE DADOS)
            dados = NotaFiscal(valor=valor, numero_serie=numero_serie, descricao=descricao, id_revendedor=id_revendedor)
            session.add(dados) # CONSULTA

            # -----------------------------------------------------------------
            cadastro = True
            ### Lote ###
            while cadastro:

                id_lote: int = input('Informe o ID do lote: ')

                # Se "id_lote" não for informado
                if id_lote == '':
                    return 'ID do revendedor não pode ficar em branco.'

                # Verifica se "id_lote" pode ser convertido para int
                try:
                    id_lote = int(id_lote)
                except ValueError:
                    return "Valor inválido. Insira apenas valores numéricos."
                
                # Verificar se o "id_lote" já existe
                lote = session.get(Lote, id_lote)
                    
                # Se o "id_lote" não existir
                if not lote:
                    return f'\nLote com id = "{id_lote}" não esta cadastrado.\n'
                
                while True:
                    op = input('Deseja cadastrar outro lote [s/n]: ').strip().upper()
                    if op in 'S':
                        break
                    elif op in 'N':
                        print()
                        cadastro = False
                        break
                    else:
                        print(f'\nOpção invalida!')
                        print(f'Digite [s] para CADASTRO ou [n] para SAIR.\n')
                
                dados.lotes.append(lote)
            # -----------------------------------------------------------------
                
            # ===================================================================
            session.add(dados) # CONSULTA
            session.commit() # CONSULTA
            # ===================================================================

            exibir = (f'\n\
            id = {dados.id}\n\
            data criação = {dados.data_criacao}\n\
            valor = {dados.valor}\n\
            numero serie = {dados.numero_serie}\n\
            descrição = {dados.descricao}\n\
            id revendedor = {dados.revendedor.id}\n\
            CNPJ revendedor = {dados.revendedor.cnpj}\n\
            lista lotes =   {[lote.id for lote in dados.lotes]}')
            
            return exibir
    
    except Exception as exception:
        # Reverte a transação caso haja erro
        session.rollback() # CONSULTA
        raise exception

if __name__ == '__main__':

    resposta_09 = insert_nota_fiscal()
    print(resposta_09)
