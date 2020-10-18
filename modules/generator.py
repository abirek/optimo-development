import aio_pika
import asyncio

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

    async def __run(self, loop):
        generator = self.get_fibbonacci_generator()
        connector = None

        while True:
            try:
                connector = RabbitMQConnector(username=self.__config.rabbitmq_username,
                                              password=self.__config.rabbitmq_password,
                                              host=self.__config.rabbitmq_host,
                                              port=self.__config.rabbitmq_port,
                                              vhost=self.__config.rabbitmq_vhost)
                await connector.connect(loop)
                message = str(next(generator))
                await connector.channel.default_exchange.publish(message=aio_pika.Message(body=message.encode()),
                                                                 routing_key=self.__config.rabbitmq_queue)
                print(f'Produced {message} to RabbitMQ')
                await asyncio.sleep(self.__config.delay)
            except:
                raise
            finally:
                if connector and connector.connection:
                    await connector.close()

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__run(loop))
        loop.close()
