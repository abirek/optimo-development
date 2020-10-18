from logging import INFO, Logger, StreamHandler, Formatter
from sys import stdout


class LoggerMixin:
    default_logging_level = INFO

    def __init__(self):
        self.__logger: Logger = None

    @property
    def logger(self) -> Logger:
        if not self.__logger:
            self.__logger = Logger(self.__class__.__name__, level=self.default_logging_level)
            handler = StreamHandler(stream=stdout)
            formatter = Formatter('%(asctime)s [%(name)s] [%(levelname)s] %(message)s')
            handler.setFormatter(formatter)
            handler.setLevel(self.default_logging_level)
            self.__logger.addHandler(handler)
        return self.__logger

    @logger.setter
    def logger(self, logger: Logger):
        self.__logger = logger
