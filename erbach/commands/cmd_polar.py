import click
from erbach.cli import pass_environment
from erbach.Plotter import Plotter


@click.command("polar", help="Display polar for selected  airfoil.")
@pass_environment
def cli(ctx):
    """Plot Cl vs Cd for specified airfoil"""
    click.echo(f"Generating polar plot for: {ctx.airfoil}")

    p = Plotter()
    p.plot_airfoil_polar()

