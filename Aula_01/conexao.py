from sqlalchemy import create_engine, text
"""
    PyMySQL é a ponte entre Python e MySQL: serve como um intermediário, 
    permitindo que seu código Python se comunique com o banco de dados MySQL.
    O parâmetro "mysql+pymysql" na criação do engine indica explicitamente que 
    você está utilizando o driver PyMySQL para se conectar ao servidor MySQL.

    - py -m pip install PyMySQL
    create_engine('mysql+pymysql://root:Enigma.3@localhost:3306/cinema')

    OU

    O "mysqlclient" é um dos drivers mais populares e eficientes para conectar 
    aplicações Python a bancos de dados MySQL ou MariaDB. 
    
    - pip install mysqlclient
    engine = create_engine('mysql://root:Enigma.3@localhost:3306/cinema')
"""

# endereço Banco de Dados
# engine = create_engine('mysql+pymysql://root:Enigma.3@localhost:3306/cinema') # pymysql
engine = create_engine('mysql://root:Enigma.3@localhost:3306/cinema_01') # mysqlclient

conn = engine.connect() # abrir conexão

"""
    O "text" permite que você execute instruções SQL diretamente, sem a necessidade 
    de utilizar as abstrações de ORM (Object-Relational Mapping) do SQLAlchemy.

    Proteção contra SQL Injection:
    query = text("SELECT * FROM filmes WHERE diretor = :nome_diretor")
    result = conn.execute(query, {"nome_diretor": "Steven Spielberg"})
"""

# Faz consulta no banco (query)
resposta = conn.execute(text('SELECT * FROM filmes;'))
for linha in resposta:
    print(f'Consuta => {linha}')

# for linha in resposta:
#     print(linha.titulo)
#     print(linha.genero)
#     print(linha.ano)

conn.close() # fechar conexão