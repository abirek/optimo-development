from configs.base import Config
from connectors.mysql import MySQLConnector
from connectors.rabbitmq import RabbitMQConnector


class Ingestor:
    def __init__(self, config: Config):
        self.__config: Config = config

    def run(self):

        def callback(ch, method, properties, body):
            body = body.decode()
            connector = MySQLConnector(username=self.__config.database_username,
                                       password=self.__config.database_password,
                                       schema=self.__config.database_schema,
                                       host=self.__config.database_host,
                                       port=self.__config.database_port)
            engine = connector.get_engine()
            with engine.connect() as connection:
                connection.execute(f"INSERT INTO {self.__config.database_table} (number) VALUES ({body});")
            print(f" [x] Inserted {body}")

        connector = None
        try:
            connector = RabbitMQConnector(username=self.__config.rabbitmq_username,
                                          password=self.__config.rabbitmq_password,
                                          host=self.__config.rabbitmq_host,
                                          port=self.__config.rabbitmq_port,
                                          vhost=self.__config.rabbitmq_vhost)
            connector.connect()
            connector.channel.basic_consume(queue=self.__config.rabbitmq_queue, on_message_callback=callback, auto_ack=True)

            print(' [*] Waiting for messages. To exit press CTRL+C')
            connector.channel.start_consuming()
        except Exception as e:
            raise
        finally:
            if connector and connector.connection:
                connector.close()
