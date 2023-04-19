"""first click script
"""
from importlib import metadata
import click

def showVersion():
    version = metadata.version("gh-test-first")
    click.echo(f"{version}")

@click.command(no_args_is_help=True,help="Automated greeter")
@click.option("--name",help="Name of person to greet")
@click.option("--version","-v",is_flag=True)
def cli(name,version):
    if version:
        showVersion()
    else:
        click.echo(f"hello {name}")
