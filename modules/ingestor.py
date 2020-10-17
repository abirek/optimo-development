from connectors.mysql import MySQLConnector
from connectors.rabbitmq import RabbitMQConnector


class Ingestor:

    def run(self):

        def callback(ch, method, properties, body):
            body = body.decode()
            connector = MySQLConnector(username="app_user", password="password", database="app")
            engine = connector.get_engine()
            with engine.connect() as connection:
                connection.execute(f"INSERT INTO fibonacci (number) VALUES ({body});")
            print(f" [x] Inserted {body}")

        connector = None
        try:
            connector = RabbitMQConnector(username="guest", password="guest")
            connector.connect()
            connector.channel.basic_consume(queue='fibonacci_queue', on_message_callback=callback, auto_ack=True)

            print(' [*] Waiting for messages. To exit press CTRL+C')
            connector.channel.start_consuming()
        except Exception as e:
            print(e)
        finally:
            if connector and connector.connection:
                connector.close()
