#cmd_polar.py
from erbach.Erbach import Erbach


class Plugin:
    """display current airfoil polar plot"""

    help = "generate velocity and power data"

    def process(self, ctx):
        """generate erbach velocity and power curves"""
        ec = Erbach(ctx)

