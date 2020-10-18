from flask import Flask
from flask_restful import Resource, Api
from flaskext.mysql import MySQL

from configs.base import Config


def create_app(config: Config):
    app = Flask(__name__)

    app.config['MYSQL_DATABASE_HOST'] = config.database_host
    app.config['MYSQL_DATABASE_PORT'] = config.database_port
    app.config['MYSQL_DATABASE_USER'] = config.database_username
    app.config['MYSQL_DATABASE_PASSWORD'] = config.database_password
    app.config['MYSQL_DATABASE_DB'] = config.database_schema

    db = MySQL(app)
    api = Api(app)

    class ListFibonacciNumbers(Resource):
        def get(self):
            cursor = db.get_db().cursor()
            cursor.execute(f'SELECT * FROM {config.database_schema}.{config.database_table}')
            results = cursor.fetchall()
            cursor.close()
            return {'results': tuple((v[1] for v in results))}

    api.add_resource(ListFibonacciNumbers, '/numbers')

    return app
