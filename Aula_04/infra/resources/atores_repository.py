from infra.configs.config_DB import Config_DB # configuração do Banco de Dados
from infra.models.atores import Atores
from infra.models.filmes import Filmes

# rota Atores (CRUD)
class AtoresRepository:
    # método de (Leitura 1)
    def select(self):
        with Config_DB() as db:
            try: 
                # data = (CONEXÃO).(CONSULTA).(ESCOPO BANCO DE DADOS).(retornar todos)
                data = db.session.query(Atores).all()
            except Exception as exception:
                db.session.rollback() # Reverte a transação caso haja erro
                raise exception
            
            return data
                
    # método de (Leitura 2)
    def select_filmes(self):
        with Config_DB() as db:
            try: 
                # data = (CONEXÃO).(CONSULTA)\
                # (ESCOPO BANCO DE DADOS = Atores)\
                # (realizar junções Filmes e Atoes)\
                # (selecionar colunas)\
                # (retornar todos)
                data = db.session\
                    .query(Atores)\
                    .join(Filmes, Atores.titulo_filme == Filmes.titulo)\
                    .with_entities(
                        Atores.id,
                        Atores.nome,
                        Filmes.genero,
                        Filmes.titulo,
                        Filmes.ano
                    )\
                    .all()
            except Exception as exception:
                db.session.rollback() # Reverte a transação caso haja erro
                raise exception
            
            return data
            
        
        """
            .join(): é usado para realizar junções (joins) entre tabelas, 
            assim como a cláusula JOIN em SQL no geral. Ele permite que você conecte 
            tabelas relacionadas com base em colunas de chave estrangeira (ou em uma 
            condição de junção personalizada).
            Exemplo personalizado: "Atores.titulo_filme == Filmes.titulo"

            .with_entities: é usado quando se deseja especificar quais colunas ou 
            entidades selecionar em uma consulta
        """
            
            
        
