import os

from configs.base import Config


class ApiConfig(Config):
    def __init__(self):
        self.ensure_value_set('API_PORT')
        self.ensure_value_set('API_DATABASE_USERNAME')
        self.ensure_value_set('API_DATABASE_PASSWORD')
        self.ensure_value_set('API_DATABASE_HOST')
        self.ensure_value_set('API_DATABASE_SCHEMA')
        self.ensure_value_set('API_DATABASE_TABLE')

        self.port = int(os.getenv('API_PORT'))
        self.database_username = os.getenv('API_DATABASE_USERNAME')
        self.database_password = os.getenv('API_DATABASE_PASSWORD')
        self.database_schema = os.getenv('API_DATABASE_SCHEMA')
        self.database_table = os.getenv('API_DATABASE_TABLE')
        self.database_host = os.getenv('API_DATABASE_HOST', 'mysql')
        self.database_port = int(os.getenv('API_DATABASE_PORT', 3306))
