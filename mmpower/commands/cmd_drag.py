#cmd_drag.py

from mmpower.Plotter import Plotter
from mmpower.DataLoader import DataLoader


class Plugin:
    """display current airfoil polar plot"""

    help = "airfoil polar plotplugin"

    def process(self, ctx):
        """display polar"""
        dl = DataLoader(ctx)
        dl.load_airfoil_data()
        plt = Plotter(ctx)
        plt.plot_airfoil_drag()
