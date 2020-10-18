from databases import Database


class MySQLConnector:
    def __init__(self,
                 username: str,
                 password: str,
                 schema: str,
                 host: str = "localhost",
                 port: int = 3306):
        self.__username: str = username
        self.__password: str = password
        self.__host: str = host
        self.__port: int = port
        self.__schema: str = schema

    def get_engine(self):
        return Database(f'mysql://{self.__username}:{self.__password}@{self.__host}:{self.__port}/{self.__schema}')
