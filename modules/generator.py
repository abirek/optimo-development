import time

from connectors.rabbitmq import RabbitMQConnector


class FibonacciGenerator:
    def __init__(self, delay: int):
        self.__delay: int = delay

    @staticmethod
    def get_fibbonacci_generator():
        f1 = f2 = 1
        while True:
            yield f2
            f1, f2 = f2, f1 + f2

    def run(self):
        generator = self.get_fibbonacci_generator()
        connector = None

        while True:
            try:
                connector = RabbitMQConnector()
                connector.connect()
                message = next(generator)
                connector.channel.basic_publish(exchange='', routing_key='fibonacci_queue', body=str(message).encode())
                print(f'Produced {message} to RabbitMQ')
                time.sleep(self.__delay)
            except Exception as e:
                print(e)
                break
            finally:
                if connector and connector.connection:
                    connector.close()
