from infra.configs.config_DB import Config_DB # configuração do Banco de Dados
from infra.models.filmes import Filmes
from sqlalchemy.orm.exc import NoResultFound
import traceback

# rota Filmes (CRUD)
class FilmesRepository:
    # método de (Leitura)
    def select(self):
        with Config_DB() as db:
            try:
                # data = (CONEXÃO).(CONSULTA).(ESCOPO BANCO DE DADOS).(retornar todos)
                data = db.session.query(Filmes).all()
            except Exception:
                db.session.rollback() # Reverte a transação caso haja erro
                traceback.print_exc() # ver class do erro
                raise 
            
            return data
    
    # método de (Leitura por genero)
    def select_genero(self, genero=None):
        with Config_DB() as db:
            try:
                if not genero:
                    return 'Faltou indicar o "genero" do filme.'

                # data = (CONEXÃO).(CONSULTA).(ESCOPO BANCO DE DADOS).(filtar por genero).(retornar um)
                data = db.session.query(Filmes).filter(Filmes.genero==genero).all()
                # Se "genero" for "None"
                
                # Se "data" for "None"
                if not data:
                    return f'Não foi encontrado o genero "{genero}" na lista de Filmes'
            except Exception as exception:
                db.session.rollback() # Reverte a transação caso haja erro
                raise exception
            
            return data

    # método de (Criar)
    def insert(self, titulo=None, genero=None, ano=None):
        with Config_DB() as db:
            try:
                # Se "genero" for "None"
                if not titulo:
                    return 'Faltou indicar o "titulo" do filme.'
                # Se "genero" for "None"
                if not genero:
                    return 'Faltou indicar o "genero" do filme.'
                # Se "genero" for "None"
                if not ano:
                    return 'Faltou indicar o "ano" do filme.'

                # Verificar se o filme com o mesmo título já existe
                existe_filme = db.session.query(Filmes).filter(Filmes.titulo == titulo).first()
                if existe_filme:
                    return f'Filme com título "{titulo}" já existe.'
                
                # >>> INSERIR AO BANCO DE DADOS <<<
                data_isert = Filmes(titulo=titulo, genero=genero, ano=ano) 
                
                db.session.add(data_isert) # adicionar no Banco de Dados
                db.session.commit()
            except Exception as exception:
                db.session.rollback() # Reverte a transação caso haja erro
                raise exception
            
            return f'Filme "{data_isert.titulo}" cadastrado com sucesso!!!'

    # método de (Deletar por titulo)
    def delete(self, titulo=None):
        with Config_DB() as db:
            try:
                # Se "genero" for "None"
                if not titulo:
                    return 'Faltou informar o "titulo" do filme.'

                # titulo_filme = (CONEXÃO).(CONSULTA).(ESCOPO BANCO DE DADOS).(filtra por titulo)
                titulo_filme = db.session.query(Filmes).filter(Filmes.titulo == titulo).first()

                # Se "data" for "None"
                if not titulo_filme:
                    return f'Não foi encontrado o filme "{titulo}" na lista de Filmes'

                db.session.delete(titulo_filme) # Excluir do banco
                db.session.commit()
            except NoResultFound as e:
                db.session.rollback() # Reverte a transação caso haja erro
                raise e
            except Exception as exception:
                db.session.rollback() # Reverte a transação caso haja erro
                raise exception
            
            return f'Filme "{titulo}" foi excluído.'
            
    # método de (Atualização por titulo)
    def update(self, titulo=None, ano=None):
        with Config_DB() as db:
            try:
                # Se "genero" for "None"
                if not titulo:
                    return 'Faltou informar o "titulo" do filme.'
                
                # Se "genero" for "None"
                if not ano:
                    return 'Faltou indicar o "ano" do filme.'
                
                # titulo_filme = (CONEXÃO).(CONSULTA).(ESCOPO BANCO DE DADOS).(filtra por titulo)
                titulo_filme = db.session.query(Filmes).filter(Filmes.titulo == titulo).first()

                # Se "data" for "None"
                if not titulo_filme:
                    return f'Não foi encontrado o filme "{titulo}" na lista de Filmes'

                # >>> ATUALIZAÇÃO NO BANCO DE DADOS <<<
                titulo_filme.ano = ano 

                db.session.commit()
            except Exception as exception:
                db.session.rollback() # Reverte a transação caso haja erro
                raise exception
            
            return f'Dados alterado com sucesso!!!'