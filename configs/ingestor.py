import os

from configs.base import Config


class IngestorConfig(Config):
    def __init__(self):
        self.ensure_value_set('INGESTOR_DATABASE_USERNAME')
        self.ensure_value_set('INGESTOR_DATABASE_PASSWORD')
        self.ensure_value_set('INGESTOR_DATABASE_SCHEMA')
        self.ensure_value_set('INGESTOR_DATABASE_TABLE')

        self.ensure_value_set('INGESTOR_RABBITMQ_USERNAME')
        self.ensure_value_set('INGESTOR_RABBITMQ_PASSWORD')
        self.ensure_value_set('INGESTOR_RABBITMQ_QUEUE')

        self.database_username = os.getenv('INGESTOR_DATABASE_USERNAME')
        self.database_password = os.getenv('INGESTOR_DATABASE_PASSWORD')
        self.database_schema = os.getenv('INGESTOR_DATABASE_SCHEMA')
        self.database_table = os.getenv('INGESTOR_DATABASE_TABLE')
        self.database_host = os.getenv('INGESTOR_DATABASE_HOST', 'mysql')
        self.database_port = os.getenv('INGESTOR_DATABASE_PORT', 3306)

        self.rabbitmq_username = os.getenv('INGESTOR_RABBITMQ_USERNAME')
        self.rabbitmq_password = os.getenv('INGESTOR_RABBITMQ_PASSWORD')
        self.rabbitmq_queue = os.getenv('INGESTOR_RABBITMQ_QUEUE')
        self.rabbitmq_host = os.getenv('INGESTOR_RABBITMQ_HOST', 'rabbitmq')
        self.rabbitmq_port = os.getenv('INGESTOR_RABBITMQ_PORT', 5672)
        self.rabbitmq_vhost = os.getenv('INGESTOR_RABBITMQ_VHOST', '/')
