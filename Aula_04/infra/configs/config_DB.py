from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# configuração do Banco de Dados
class Config_DB:
    # ==================================== CONEXÃO =====================================
    # endereço de conexão (construtor)
    def __init__(self) -> None:
        self.__engine = create_engine ('mysql://root:Enigma.1@localhost:3306/cinema_04')
        self.session = None

    # instanciar conexão
    def get_engine(self):
        return self.__engine
    # ==================================== CONSULTA =====================================
    # iniciar seção (interagir c/ banco de dados)
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    # fechar seção (interagir c/ banco de dados)
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
    # ===================================================================================

    '''
    (exc_type, exc_val, exc_tb) ou (exc_type, exc_value, traceback))
    Esses parâmetros são usados para manipular exceções que ocorrem dentro do with bloco.
    '''