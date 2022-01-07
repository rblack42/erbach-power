import click
from erbach.cli import pass_environment
from erbach.DataLoader import DataLoader


@click.command("airfoil", help="Select airfoil for test.")
def cli():
    """Load specified airfoil data"""
    click.echo(f"Loading: {ctx.airfoil}")
