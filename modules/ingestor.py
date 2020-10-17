from connectors.mysql import MySQLConnector
from connectors.rabbitmq import RabbitMQConnector


class Ingestor:

    def run(self):

        def callback(ch, method, properties, body):
            body = body.decode()
            connector = MySQLConnector('app_user', 'password', '127.0.0.1', 3307, 'app')
            engine = connector.get_engine()
            connector.insert(engine, body)
            print(f" [x] Inserted {body}")

        connector = None
        try:
            connector = RabbitMQConnector()
            connector.connect()
            connector.channel.basic_consume(queue='fibonacci_queue', on_message_callback=callback, auto_ack=True)

            print(' [*] Waiting for messages. To exit press CTRL+C')
            connector.channel.start_consuming()
        except Exception as e:
            print(e)
        finally:
            if connector and connector.connection:
                connector.close()
