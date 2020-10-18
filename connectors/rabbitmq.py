from typing import Optional

import aio_pika
from aio_pika import RobustConnection, RobustChannel


class RabbitMQConnector:
    def __init__(self,
                 username: str,
                 password: str,
                 host: str = "localhost",
                 port: int = 5672,
                 vhost: str = "/"):
        self.__username: str = username
        self.__password: str = password
        self.__host: str = host
        self.__port: int = port
        self.__vhost: str = vhost
        self.connection: Optional[RobustConnection] = None
        self.channel: Optional[RobustChannel] = None

    async def connect(self, loop):
        self.connection = await aio_pika.connect_robust(f"amqp://{self.__username}:{self.__password}@{self.__host}:{self.__port}/", loop=loop)
        self.channel = await self.connection.channel()

    async def close(self):
        if self.channel:
            await self.channel.close()
            self.channel = None
        if self.connection:
            await self.connection.close()
            self.connection = None
