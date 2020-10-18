from typing import Optional

from pika import PlainCredentials, ConnectionParameters, BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel


class RabbitMQConnector:
    def __init__(self,
                 username: str,
                 password: str,
                 host: str = "localhost",
                 port: int = 5672,
                 vhost: str = "/"):
        self.__parameters = ConnectionParameters(host=host,
                                                 port=port,
                                                 credentials=PlainCredentials(username, password),
                                                 virtual_host=vhost)
        self.connection: Optional[BlockingConnection] = None
        self.channel: Optional[BlockingChannel] = None

    def connect(self):
        self.connection = BlockingConnection(parameters=self.__parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare("fibonacci_queue", {"durable": True})

    def close(self):
        if self.channel:
            self.channel.close()
            self.channel = None
        if self.connection:
            self.connection.close()
            self.connection = None
