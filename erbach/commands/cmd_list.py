import click
from erbach.cli import pass_environment
from erbach.DataLoader import DataLoader


@click.command("listr", help="Display list of installed models and airfoils.")
@pass_environment
def cli(ctx):
    """Generate model and airfoil list"""
    d = DataLoader()
    models = d.get_model_list()
    airfoils = d.get_airfoil_list()
    current_model = d.get_model_name()
    current_airfoil = d.get_airfoil_name()
    datadir = d.get_datadir()
    click.echo(f"Generating listing for: {datadir}")
    click.echo("Model List:")
    for m in models:
        if m == current_model:
            tag = "*"
        else:
            tag = " "
        click.echo(f"\t {m} {tag}")
    click.echo("Airfoil_List:")
    for m in airfoils:
        if m == current_airfoil:
            tag = "*"
        else:
            tag=" "
        click.echo(f"\t {m} {tag}")

