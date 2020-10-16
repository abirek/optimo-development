from flask import Flask
from flask_restful import Resource, Api
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3307
app.config['MYSQL_DATABASE_USER'] = 'app_user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'app'

db = MySQL(app)
api = Api(app)


class ListFibonacciNumbers(Resource):
    def get(self):
        cursor = db.get_db().cursor()
        cursor.execute('SELECT * FROM app.fibonacci')
        results = cursor.fetchall()
        cursor.close()
        return {'results': tuple((v[1] for v in results))}


api.add_resource(ListFibonacciNumbers, '/numbers')
