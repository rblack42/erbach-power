import os
import click
from erbach import __version__

class Environment:
    """Context class holding state for cli commands"""

    def __init__(self):
        self.cwd = os.getcwd()
        self.debug = False

pass_environment = click.make_pass_decorator(Environment, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))


class CLI(click.MultiCommand):
    """Modular CLI class"""

    def list_commands(self, ctx):
        """scan command directory and list all cli commands"""
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        """import cli command file on demand"""
        try:
            mod = __import__(f"erbach.commands.cmd_{name}", None, None, ["cli"])
        except ImportError: # pragma: no cover
            return
        return mod.cli

@click.version_option(__version__, "-v", "--version")

@click.command(cls=CLI)
@click.option("--debug", is_flag=True, help="Enable debug output")
@click.option("--model", help="model from data directory", default="erbach-basic")
@click.option("--airfoil", help="airfoil for this model", default="mcbride-b7")

@pass_environment
def cli(ctx, debug, model, airfoil):
    """primary CLI interface"""
    ctx.debug = debug
    if not airfoil is None:
        ctx.airfoil = airfoil
    if not model is None:
        ctx.model = model
