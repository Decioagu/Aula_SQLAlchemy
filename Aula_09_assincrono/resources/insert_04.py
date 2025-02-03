import sys
import os
import asyncio ### async
from sqlalchemy.future import select ### async

# Adicionar o caminho do diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conf.config_DB import criar_session # CONSULTA

# ESCOPO BANCO DE DADOS
from models.picole import Picole # Recursos

from models.sabor import Sabor # Chave estrangeira
from models.tipo_embalagem import TipoEmbalagem # Chave estrangeira
from models.tipo_picole import TipoPicole # Chave estrangeira

from models.ingrediente import Ingrediente # Chave estrangeira para (tabela "secundaria")
from models.conservante import Conservante # Chave estrangeira para (tabela "secundaria")
from models.aditivo_nutritivo import AditivoNutritivo # Chave estrangeira para (tabela "secundaria")

# 10 - Picole
async def insert_picole() -> None:

    try:
        
        async with criar_session() as session: 
            # ===================================================================
            print('\n10 - Picole\n')
            ### Picole ###
            preco : float = input('Informe o preço do picolé: ') 

            # Se "preco" for igual ''
            if preco == '':
                return 'Preço do picolé não pode ficar em branco.'

            # Verifica se "preco" pode ser convertido para float
            try:
                preco = float(preco)
            except ValueError:
                return "Valor inválido. Insira apenas valores numéricos."
            # ===================================================================
            ### Sabor ###
            id_sabor: int = input('Informe o ID do sabor: ') 

            # Se "id_sabor" for igual ''
            if id_sabor == '':
                return 'ID do sabor não pode ficar em branco.'

            # Verifica se "id_sabor" pode ser convertido para int
            try:
                id_sabor = int(id_sabor)
            except ValueError:
                return "Valor inválido. Insira apenas valores numéricos."
            
            # Verificar se o "id_sabor" já existe
            sabor = await session.get(Sabor, id_sabor)
                
            # Se o "sabor" não existir
            if not sabor:
                return f'\nSabor com id = "{id_sabor}" não esta cadastrado.\n'
            # ===================================================================
            ### TipoEmbalagem ###
            id_tipo_embalagem: int = input('Informe o ID do tipo de embalagem: ') 

            # Se "id_tipo_embalagem" for igual ''
            if id_tipo_embalagem == '':
                return 'ID do tipo de embalagem não pode ficar em branco.'

            # Verifica se "id_tipo_embalagem" pode ser convertido para int
            try:
                id_tipo_embalagem = int(id_tipo_embalagem)
            except ValueError:
                return "Valor inválido. Insira apenas valores numéricos."
            
            # Verificar se o "id_tipo_embalagem" já existe
            tipo_embalagem = await session.get(TipoEmbalagem, id_tipo_embalagem)
                
            # Se o "tipo_embalagem" não existir
            if not tipo_embalagem:
                return f'\nTipo de embalagem com id = "{id_tipo_embalagem}" não esta cadastrado.\n'
            
            # ===================================================================
            ### TipoPicole ###
            id_tipo_picole: int = input('Informe o ID do tipo de picolé: ')

            # Se "id_tipo_picole" for igual ''
            if id_tipo_picole == '':
                return 'ID do tipo de picole não pode ficar em branco.'

            # Verifica se "id_tipo_picole" pode ser convertido para int
            try:
                id_tipo_picole = int(id_tipo_picole)
            except ValueError:
                return "Valor inválido. Insira apenas valores numéricos."
            
            # Verificar se o "id_tipo_picole" já existe
            tipo_picole = await session.get(TipoPicole, id_tipo_picole)
                
            # Se o "tipo_picole" não existir
            if not tipo_picole:
                return f'\nTipo de picolé com id = "{id_tipo_picole}" não esta cadastrado.\n'
            # ===================================================================

            # dados = (ESCOPO BANCO DE DADOS)
            dados = Picole(preco=preco, id_sabor=id_sabor, id_tipo_embalagem=id_tipo_embalagem, id_tipo_picole=id_tipo_picole)
            session.add(dados) # CONSULTA

            # ===================================================================

            # Auxilia na impressão de dados na variável "exibir"
            lista_auxiliar_ingrediente = []

            cadastro = True
            ### Ingrediente ###
            while cadastro:

                id_ingredientes: int = input('Informe o ID do ingrediente: ')

                # Se "id_lote" não for informado
                if id_ingredientes == '':
                    return 'Informar ID de ingrediente é obrigatório.'

                # Verifica se "id_ingredientes" pode ser convertido para int
                try:
                    id_ingredientes = int(id_ingredientes)
                except ValueError:
                    return "Valor inválido. Insira apenas valores numéricos."
                
                # Verificar se o "id_ingredientes" já existe
                ingrediente = await session.get(Ingrediente, id_ingredientes)
                    
                # Se o "id_ingredientes" não existir
                if not ingrediente:
                    return f'\nIngrediente com id = "{id_ingredientes}" não esta cadastrado.\n'
                
                while True:
                    op = input('Deseja cadastrar outro ingrediente [s/n]: ').strip().upper()
                    if op in 'S':
                        break
                    elif op in 'N':
                        print()
                        cadastro = False
                        break
                    else:
                        print(f'\nOpção invalida!')
                        print(f'Digite [s] para CADASTRO ou [n] para SAIR.\n')
                
                
                dados.ingredientes.append(ingrediente)
                lista_auxiliar_ingrediente.append(ingrediente.id) # Auxilia na impressão de dados

            # -----------------------------------------------------------------
            # Auxilia na impressão de dados na variável "exibir"
            lista_auxiliar_conservantes = []

            cadastro = True
            ### Conservante ###
            while cadastro:

                id_conservantes: int = input('Informe o ID do conservantes: ')

                # Se o "id_conservantes" for igual ''
                if id_conservantes == '':
                        print()
                        cadastro = False
                        break
                
                # Verifica se "id_conservantes" pode ser convertido para int
                try:
                    id_conservantes = int(id_conservantes)
                except ValueError:
                    return "Valor inválido. Insira apenas valores numéricos."

                # Verificar se o "id_conservantes" já existe
                conservante = await session.get(Conservante, id_conservantes)
                    
                # Se o "id_conservantes" existir
                if conservante:
                    dados.conservantes.append(conservante)
                    lista_auxiliar_conservantes.append(conservante.id) # Auxilia na impressão de dados
                else:
                    print(f'\nConservante com id = "{id_conservantes}" não esta cadastrado.\n')

                
                while True:
                    op = input('Deseja cadastrar outro conservante [s/n]: ').strip().upper()
                    
                    if op in 'S':
                        break
                    elif op in 'N':
                        print()
                        cadastro = False
                        break
                    else:
                        print(f'\nOpção invalida!')
                        print(f'Digite [s] para CADASTRO ou [n] para SAIR.\n')
                
            # -----------------------------------------------------------------
            # Auxilia na impressão de dados na variável "exibir"
            lista_auxiliar_aditivos_nutritivos = []

            cadastro = True
            ### AditivoNutritivo ###
            while cadastro:

                id_aditivos_nutritivos: int = input('Informe o ID do aditivos nutritivos: ')

                # Se o "id_aditivos_nutritivos" for igual ''
                if id_aditivos_nutritivos == '':
                        print()
                        cadastro = False
                        break

                # Verifica se "id_aditivos_nutritivos" pode ser convertido para int
                try:
                    id_aditivos_nutritivos = int(id_aditivos_nutritivos)
                except ValueError:
                    return "Valor inválido. Insira apenas valores numéricos."
                
                # Verificar se o "id_aditivos_nutritivos" já existe
                aditivos_nutritivo = await session.get(AditivoNutritivo, id_aditivos_nutritivos)
                    
                # Se o "id_aditivos_nutritivos" existir
                if aditivos_nutritivo:
                    dados.aditivos_nutritivos.append(aditivos_nutritivo)
                    lista_auxiliar_aditivos_nutritivos.append(aditivos_nutritivo.id) # Auxilia na impressão de dados
                else:
                    print(f'\nAditivos nutritivos com id = "{id_aditivos_nutritivos}" não esta cadastrado.\n')
                
                while True:
                    op = input('Deseja cadastrar outro aditivos nutritivos [s/n]: ').strip().upper()
                    if op in 'S':
                        break
                    elif op in 'N':
                        print()
                        cadastro = False
                        break
                    else:
                        print(f'\nOpção invalida!')
                        print(f'Digite [s] para CADASTRO ou [n] para SAIR.\n')  

            # -----------------------------------------------------------------
                
            # ===================================================================    
            session.add(dados) # CONSULTA
            # await session.commit() # CONSULTA
            await session.refresh(dados) # Atualiza o objeto "dados" na memória com os valores mais recentes do BANCO DE DADOS
            # ===================================================================

            exibir = (f'\n\
            10 - Picole\n\
            id = {dados.id}\n\
            data_criacao = {dados.data_criacao}\n\
            preço = {dados.preco}\n\
            id_sabor = {dados.id_sabor}\n\
            id_tipo_embalagem = {dados.id_tipo_embalagem}\n\
            id_tipo_picole = {dados.id_tipo_picole}\n\
            lista ingredientes = {[ingrediente for ingrediente in lista_auxiliar_ingrediente]}\n\
            lista conservantes = {[conservante for conservante in lista_auxiliar_conservantes]}\n\
            lista aditivos_nutritivos =   {[aditivos_nutritivo for aditivos_nutritivo in lista_auxiliar_aditivos_nutritivos]}')
            
            return exibir
    
    except Exception as exception:
        # Reverte a transação caso haja erro
        session.rollback() # CONSULTA
        raise exception

if __name__ == '__main__':

    resposta_10 = asyncio.run(insert_picole())
    print(resposta_10)


