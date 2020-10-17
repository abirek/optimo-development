from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


class MySQLConnector:
    def __init__(self,
                 username: str,
                 password: str,
                 database: str,
                 host: str = "mysql",
                 port: int = 3306):
        self.__username: str = username
        self.__password: str = password
        self.__host: str = host
        self.__port: int = port
        self.__database: str = database
        self.engine: Optional[Engine] = None

    def get_engine(self):
        return create_engine(f'mysql+mysqldb://{self.__username}:{self.__password}@{self.__host}:{self.__port}/{self.__database}')
