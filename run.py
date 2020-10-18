import click
# from gunicorn.app.base import Application
from configs.api import ApiConfig
from configs.generator import GeneratorConfig
from configs.ingestor import IngestorConfig
from modules.api import create_app
from modules.generator import FibonacciGenerator
from modules.ingestor import Ingestor


@click.command()
def startgenerator():
    click.echo('Starting generator')
    config = GeneratorConfig()
    FibonacciGenerator(config).run()


@click.command()
def startingestor():
    click.echo('Starting ingestor')
    config = IngestorConfig()
    Ingestor(config).run()


@click.command()
def startapi():
    click.echo('Starting REST API')
    config = ApiConfig()
    app = create_app(config)
    app.run(host="0.0.0.0", port=config.port)
    # Application().run(app)


@click.group()
def cli():
    pass


cli.add_command(startapi)
cli.add_command(startgenerator)
cli.add_command(startingestor)


if __name__ == '__main__':
    cli()
