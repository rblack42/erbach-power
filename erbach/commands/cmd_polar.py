import click
from erbach.cli import pass_environment
from erbach.Plotter import Plotter


@click.command("polar", help="Display polar for selected  airfoil.")
@pass_environment
def cli(ctx):
    """Plot Cl vs Cd for specified airfoil"""
    click.echo(f"Generating polar plot for: {ctx.airfoil}")

    xp = [0.008, 0.009, 0.010, 0.012, 0.014, 0.019, 0.024, 0.0335]
    yp = [0.06, 0.135, 0.20, 0.25, 0.30, 0.35, 0.395, 0.440]

    p = Plotter()
    p.curveplot(xp, yp, "Cl", "Cd", "McBride B7 Polar")

