from typing import Optional

from pika import PlainCredentials, ConnectionParameters, BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel


class RabbitMQConnector:
    def __init__(self):
        self.__parameters = ConnectionParameters(host="localhost",
                                                 port=5672,
                                                 credentials=PlainCredentials("guest", "guest"),
                                                 virtual_host="/")
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
    #
    # def __enter__(self):
    #     self.connect()
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.close()
