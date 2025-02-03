import asyncio
from conf.config_DB import criar_tabelas, fechar_conexao

if __name__ == '__main__':
    async def main():
        # Aqui você pode chamar outras funções do seu código, como criar tabelas
        await criar_tabelas()

        # Fechar a conexão antes de encerrar o programa
        await fechar_conexao()
        

    asyncio.run(main())

# Seção 4: Modelagem Dados com SQLAchemy
# .\venv\Scripts\activate
# pip install aiomysql