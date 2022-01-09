import click
from erbach.cli import pass_environment
from erbach.DataLoader import DataLoader


@click.command("load", help="Load selected data files.")
@pass_environment
def cli(ctx):
    """Load selected data files"""
    d = DataLoader()
    model = d.get_model_name()
    airfoil = d.get_airfoil_name()
    click.echo(f"Loading data files for {model} and {airfoil}")
    d.load_data()

