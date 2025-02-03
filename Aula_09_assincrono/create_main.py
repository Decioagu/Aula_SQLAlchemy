import asyncio
from conf.config_DB import criar_tabelas

if __name__ == '__main__':
    async def main():
        await criar_tabelas()

    asyncio.run(main())

# Seção 4: Modelagem Dados com SQLAchemy
# .\venv\Scripts\activate
# pip install aiomysql