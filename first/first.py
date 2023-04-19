"""First.py - my first click script
"""
import click

@click.command(no_args_is_help=True,help="Sample help message")
@click.option("--name",help="Name of person to greet")
def main(name):
    print(f"hello {name}")
