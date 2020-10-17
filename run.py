import click
# from gunicorn.app.base import Application

from modules.api import app
from modules.generator import FibonacciGenerator
from modules.ingestor import Ingestor


@click.command()
@click.option('--delay', default=60, help='')
def startgenerator(delay):
    click.echo('Starting generator')
    FibonacciGenerator(delay).run()


@click.command()
def startingestor():
    click.echo('Starting ingestor')
    Ingestor().run()


@click.command()
@click.option('--host', default="0.0.0.0", help='')
@click.option('--port', default=5000, help='')
def startapi(host, port):
    click.echo('Starting REST API')
    app.run(host=host, port=port)
    # Application().run(app)


@click.group()
def cli():
    pass


cli.add_command(startapi)
cli.add_command(startgenerator)
cli.add_command(startingestor)


if __name__ == '__main__':
    cli()
