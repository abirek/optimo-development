from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


class MySQLConnector:
    def __init__(self, user: str, password: str, host: str, port: int, database: str):
        self.__user: str = user
        self.__password: str = password
        self.__host: str = host
        self.__port: int = port
        self.__database: str = database
        self.engine: Optional[Engine] = None

    def get_engine(self):
        return create_engine(f'mysql+mysqldb://{self.__user}:{self.__password}@{self.__host}:{self.__port}/{self.__database}')

    def insert(self, engine: Engine, value: int):
        with engine.connect() as connection:
            connection.execute(f"INSERT INTO fibonacci (number) VALUES ({value});")


# connector = MySQLConnector('app_user', 'password', '127.0.0.1', 3307, 'app')
# engine = connector.get_engine()
#
# print(connector)
# print(engine)
#
# connection = engine.connect()
# connection.execute('select * from fibonacci')
# connection.execute('insert into fibonacci (number) values (1)')
# connection.execute('insert into fibonacci (number) values (1)')
# connection.execute('insert into fibonacci (number) values (2)')
# connection.execute('insert into fibonacci (number) values (3)')
