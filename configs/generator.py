import os

from configs.base import Config


class GeneratorConfig(Config):
    def __init__(self):
        self.ensure_value_set('GENERATOR_DELAY')
        self.ensure_value_set('GENERATOR_RABBITMQ_USERNAME')
        self.ensure_value_set('GENERATOR_RABBITMQ_PASSWORD')
        self.ensure_value_set('GENERATOR_RABBITMQ_QUEUE')

        self.delay = int(os.getenv('GENERATOR_DELAY'))
        self.rabbitmq_username = os.getenv('GENERATOR_RABBITMQ_USERNAME')
        self.rabbitmq_password = os.getenv('GENERATOR_RABBITMQ_PASSWORD')
        self.rabbitmq_queue = os.getenv('GENERATOR_RABBITMQ_QUEUE')
        self.rabbitmq_host = os.getenv('GENERATOR_RABBITMQ_HOST', 'rabbitmq')
        self.rabbitmq_port = os.getenv('GENERATOR_RABBITMQ_PORT', 5672)
        self.rabbitmq_vhost = os.getenv('GENERATOR_RABBITMQ_VHOST', '/')
