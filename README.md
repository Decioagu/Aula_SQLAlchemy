# Aula_SQLAlchemy
 Gerenciador Banco de Dados

__SQLAlchemy__ é uma biblioteca de __ORM__ (__Object-Relational Mapping__) em Python que permite interagir com bancos de dados usando classes e objetos, abstraindo as consultas SQL complexas. Além de funcionar como ORM, SQLAlchemy também oferece ferramentas para executar consultas SQL diretamente. Ex: __text__.

**Aula_01**

__OBS: Banco de Dados gerado pelo arquivo BD_01.sql__

- __create_engine__: é o ponto de entrada (conexão) para o SQLAlchemy quando se deseja se conectar a um banco de dados. Ela cria um "engine", que é a conexão entre o código Python e o banco de dados subjacente.

- __text__: permite que você execute instruções SQL diretamente, sem a necessidade de utilizar as abstrações de ORM (Object-Relational Mapping) do SQLAlchemy.
---

**Aula_02**

- __engine__: é o ponto central para a __conexão__ entre o aplicativo Python e o banco de dados.

- __ORM (Object-Relational Mapping)__: é uma técnica que permite que desenvolvedores interajam com bancos de dados relacionais de maneira mais simples e intuitiva, utilizando __objetos__ em vez de comandos SQL diretos.

- __Sessions__: interagem com o banco de dados usando o ORM, o SQLAlchemy utiliza o conceito de sessões. Uma sessão é responsável por operar __consulta__ no Banco de Dados.

- __BaseModel.metadata.create_all(engine)__:  cria todas as tabelas definidas em um modelo (class) de banco de dados a partir do objeto engine.
- __BaseModel.metadata.drop_all(engine)__: é o método chamado para eliminar todas as tabelas que estão registradas no metadata da BaseModel.

    - __BaseModel__: é uma classe que herda de "declarative_base()", que contem definições de tabelas e seus relacionamentos. Resumo: __declarative_base() = BaseModel__
    - __metadata__: Este é um atributo do BaseModel que contém informações sobre as tabelas que foram definidas nas classes.
    - __create_all(engine)__: cria todas as tabelas que estão registradas no metadata da BaseModel.
    - drop_all(engine): eliminar todas as tabelas que estão registradas no metadata da BaseModel.
---

**Aula_03**

__OBS: Banco de Dados gerado pelo arquivo BD_03.sql__

- Operações __(CRUD)__ em __SQLAlchemy__:
    - __CREATE (Criar)__: Insere novos registros em uma tabela do banco de dados.
    - __READ (Ler)__: Recupera dados existentes na tabela, podendo filtrar por critérios específicos.
    - __UPDATE (Atualizar)__: Modifica o conteúdo de registros já existentes.
    - __DELETE (Excluir)__: Remove registros da tabela.

- __CRUD__:
    - CRUD - CREATE   |  READ        |  UPDATE     |  DELETE
    - =====> Criar    |  Ler         |  Atualizar  |  Excluir
    - <==========================================================>
    - API  - POST     |  GET         |  PUT        |  DELETE
    - =====> Enviar   |  Solicitar   |  Atualizar  |  Excluir
    - <==========================================================>
    - SQL  - INSERT   |  SELECT      |  UPDATE     |  DELETE
    - =====> Inserir  |  Selecionar  |  Atualizar  |  Excluir
---

**Aula_04**

- Projeto: __Catalogo de Cinema__

__OBS: Banco de Dados gerado pelo arquivo BD_04.sql__

- __Models__ (modelos): gerencia e valida dados que transitam entre API e Banco de Dados, por meio de solicitação de usuário, permitindo apenas saída e entrada de dados definidos no modelo.

- __Resources__ (recursos): são recursos de acesso aos dados por meio de métodos, __regras de negocio__.

- Arquivos: 
    - mysql.sql = instruções SQL para criação de Banco de Dados.
    - run.py = instanciar Banco de Dados.
    - infra
        - config
            - __config_DB.py__ = configuração Banco de Dados em __SQLAlchemy__
            - __sql_alchemy.py__: ORM (Object Relational Mapping) => conexão para Banco de Dados <=
        - models
            - __atores.py__ e __filmes.py__ = (modelo) 
        - resource
            - __atores_repository.py__ e __filmes_repository.py__ = (recursos)

- Relacionamento entre tabelas __.\models\atores.py__ e __.\models\filmes.py__.
    - relationship: é uma função do SQLAlchemy que é usada para definir uma relação entre duas tabelas.
        - backref='NOME_DA_TABELA': é uma maneira mais simples e automática de definir um relacionamento bidirecional. Ele cria automaticamente o relacionamento nos dois lados (nas duas tabelas) de uma vez só. Além disso, ele configura automaticamente uma referência reversa sem a necessidade de configurar explicitamente em ambos os modelos.
        - back_populates='NOME_DA_TABELA': Este parâmetro é usado para definir a relação bidirecional.
        - lazy='dynamic': Não carrega imediatamente os dados relacionados. Em vez disso, retorna um objeto Query, que permite realizar consultas adicionais sobre os dados relacionados. (possibilita consultas com filtro ou paginação)
        - lazy='joined': Esse parâmetro carrega os dados relacionados utilizando um JOIN, carregando o relacionamento ao consultar o banco de dados. (traz as tabelas relacionadas em uma única consulta )  
        - secondary=NOME_DA_TABELA: é usado para definir relacionamentos muitos-para-muitos (many-to-many) entre duas tabelas. Ele permite especificar uma tabela intermediária (ou de associação) que faz a ligação entre as duas tabelas principais.
---

**Aula_05**

- Projeto: __Picoles__

- Configuração de novo projeto utilizando __SQLAlchemy__ com __SQLite__ ou __MySQL__.

- Arquivos:
    - conf:
        - __config_DB.py__ = = configuração Banco de Dados em __SQLAlchemy__
        - __model_base.py__: ORM (Object Relational Mapping) => conexão para Banco de Dados <=

    - __create_main.py__: instanciar Banco de Dados.
---

**Aula_06**

- Projeto: __Picoles__

- __Models__ (modelos): gerencia e valida dados que transitam entre API e Banco de Dados, por meio de solicitação de usuário, permitindo apenas saída e entrada de dados definidos no modelo.

- Arquivos:
    - conf:
        - __config_DB.py__ = configuração Banco de Dados em __SQLAlchemy__
    - models:
        - __all-models.py = responsável por aglutinar e instanciar todos os modelos
        - __aditivo_nutritivo.py__ = (modelo)
        - __conservante.py__ = (modelo)
        - __ingrediente.py__ = (modelo)
        - __lote.py__ = (modelo)
        - __nota_fiscal.py__ = (modelo)
        - __picole.py__ = (modelo)
        - __revendedor.py__ = (modelo)
        - __sabor.py__ = (modelo)
        - __tipo_embalagem.py__ = (modelo)
        - __tipo_picole.py__ = (modelo)
---