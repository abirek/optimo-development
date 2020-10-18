import os


class Config:
    @staticmethod
    def ensure_value_set(key: str):
        assert os.getenv(key) is not None, f'{key} environment variable must be set'
