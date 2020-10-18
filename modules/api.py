from quart import Quart

from configs.base import Config
from connectors.mysql import MySQLConnector


def create_app(config: Config):
    app = Quart(__name__)

    async def get_numbers():
        query = f'SELECT number FROM {config.database_schema}.{config.database_table}'
        connector = MySQLConnector(username=config.database_username,
                                   password=config.database_password,
                                   schema=config.database_schema,
                                   host=config.database_host,
                                   port=config.database_port)
        engine = connector.get_engine()
        await engine.connect()
        results = await engine.fetch_all(query=query)
        await engine.disconnect()
        return tuple((v[0] for v in results))

    @app.route('/numbers')
    async def numbers():
        results = await get_numbers()
        return {'results': results}

    return app
