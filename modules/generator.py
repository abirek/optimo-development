import time

from configs.base import Config
from connectors.rabbitmq import RabbitMQConnector


class FibonacciGenerator:
    def __init__(self, config: Config):
        self.__config: Config = config

    @staticmethod
    def get_fibbonacci_generator():
        f1 = f2 = 1
        while True:
            yield f2
            f2, f1 = f1, f1 + f2

    def run(self):
        generator = self.get_fibbonacci_generator()
        connector = None
        while True:
            try:
                connector = RabbitMQConnector(username=self.__config.rabbitmq_username,
                                              password=self.__config.rabbitmq_password,
                                              host=self.__config.rabbitmq_host,
                                              port=self.__config.rabbitmq_port,
                                              vhost=self.__config.rabbitmq_vhost)
                connector.connect()
                message = next(generator)
                connector.channel.basic_publish(exchange='', routing_key=self.__config.rabbitmq_queue, body=str(message).encode())
                print(f'Produced {message} to RabbitMQ')
                time.sleep(self.__config.delay)
            except Exception as e:
                raise
            finally:
                if connector and connector.connection:
                    connector.close()
