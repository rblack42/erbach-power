#cmd_polar.py

from mmpower.Plotter import Plotter


class Plugin:
    """display current airfoil polar plot"""

    help = "airfoil polar plotplugin"

    def process(self, ctx):
        """display polar"""
        plt = Plotter(ctx)
        plt.plot_airfoil_polar()
