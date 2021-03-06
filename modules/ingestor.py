import asyncio

from configs.base import Config
from connectors.mysql import MySQLConnector
from connectors.rabbitmq import RabbitMQConnector
from loggermixin import LoggerMixin


class Ingestor(LoggerMixin):
    def __init__(self, config: Config):
        super().__init__()
        self.__config: Config = config

    async def __run(self, loop):
        connector = None
        try:
            connector = RabbitMQConnector(username=self.__config.rabbitmq_username,
                                          password=self.__config.rabbitmq_password,
                                          host=self.__config.rabbitmq_host,
                                          port=self.__config.rabbitmq_port,
                                          vhost=self.__config.rabbitmq_vhost)
            await connector.connect(loop)
            queue = await connector.channel.declare_queue(self.__config.rabbitmq_queue, durable=True)

            self.logger.info('Waiting for messages...')
            async with queue.iterator() as queue_iter:
                async for message in queue_iter:
                    async with message.process():
                        await self.insert_to_db(message.body)
        except Exception:
            raise
        finally:
            if connector:
                await connector.close()

    async def insert_to_db(self, body: bytes):
        body = body.decode()

        query = f"INSERT INTO {self.__config.database_table} (number) VALUES ({body});"
        connector = MySQLConnector(username=self.__config.database_username,
                                   password=self.__config.database_password,
                                   schema=self.__config.database_schema,
                                   host=self.__config.database_host,
                                   port=self.__config.database_port)
        engine = connector.get_engine()
        await engine.connect()
        await engine.execute(query=query)
        await engine.disconnect()
        self.logger.info(f'Inserted to database: {body}')

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.__run(loop))
        loop.close()
