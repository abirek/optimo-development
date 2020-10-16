import click
# from gunicorn.app.base import Application

from modules.api import app
from modules.generator import run


@click.command()
@click.option('--delay', default=60, help='')
def startgenerator(delay):
    click.echo('Starting generator')
    run()


@click.command()
def startingestor():
    click.echo('Starting ingestor')
    run()


@click.command()
def startapi():
    click.echo('Starting REST API')
    app.run()
    # Application().run(app)


@click.group()
def cli():
    pass


cli.add_command(startapi)
cli.add_command(startgenerator)


if __name__ == '__main__':
    cli()
