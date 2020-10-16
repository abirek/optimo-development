import time


class FibonacciGenerator:
    def __init__(self, delay: int):
        self.__delay: int = delay


def fibbonacci_generator():
    f1 = f2 = 1
    while True:
        yield f2
        f1, f2 = f2, f1 + f2


def run():
    gen = fibbonacci_generator()
    while True:
        print(next(gen))
        time.sleep(5)
