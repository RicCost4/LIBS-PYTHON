from dotenv import load_dotenv
import os
import psycopg2 as psy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class ConeccaoPSY:
    def __init__(self, IP, PORT, DATABASE, USERNAME, PGPASSWORD):
        self.IP = IP
        self.PORT = PORT
        self.DATABASE = DATABASE
        self.USERNAME = USERNAME
        self.PGPASSWORD = PGPASSWORD

    def conexao_banco(self):
        try:
            con_banco = psy.connect(dbname=self.DATABASE, user=self.USERNAME, password=self.PGPASSWORD, host=self.IP, port=self.PORT)
        except psy.Error as e:
            print(e)

        return con_banco

    def conexao_host(self):
        try:
            con_host = psy.connect(user=self.USERNAME, password=self.PGPASSWORD, host=self.IP, port=self.PORT)
        except psy.Error as e:
            print(e)

        return con_host

class ConnectionDB:
    def __init__(self, schema:str):
        load_dotenv()
        self.__string_connection = f'postgresql://{os.environ["USER_U_APP"]}:{os.environ["PASS_U_APP"]}@{os.environ["STRING_CONEXAO"]}'
        self.__engine = self.__create_engine(schema)
        self.session = None
        
    def __create_engine(self, schema):
        engine = create_engine(self.__string_connection, echo=False, connect_args={"options": f"-csearch_path={schema}"})
        return engine
    
    def get_engine(self):
        return self.__engine

    def create_session(self):
        """cria uma conecção ao banco."""
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()
        return self.session