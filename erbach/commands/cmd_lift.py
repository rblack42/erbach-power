#cmd_polar.py
from erbach.Plotter import Plotter
from erbach.DataLoader import DataLoader


class Plugin:
    """display current airfoil polar plot"""

    help = "airfoil polar plotplugin"

    def process(self, ctx):
        """display polar"""
        dl = DataLoader(ctx)
        dl.load_airfoil_data()
        plt = Plotter(ctx)
        plt.plot_airfoil_lift()
