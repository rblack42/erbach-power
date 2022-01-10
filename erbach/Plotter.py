from matplotlib import pyplot as plt
from . DataLoader  import DataLoader
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline

class Plotter(object):

    def __init__(self,ctx):
        """create plotter using current contect"""
        self.ctx = ctx

    def plot_airfoil_lift(self):
        airfoil_data = self.ctx.airfoil_data
        name = self.ctx.airfoil
        #print(airfoil_data)
        x = []
        y = []
        CL = airfoil_data['CL'][1]
        alpha = airfoil_data['CL'][0]
        title = f"{name} Lift Coefficient"
        for l in CL:
            y.append(l)
        for a in alpha:
            x.append(a)
        self.curveplot(x,y,"Alpha", "Cl", title)

    def plot_fitted_airfoil_lift(self):
        airfoil_data = self.ctx.fitted_airfoil_data
        name = self.ctx.airfoil
        #print(airfoil_data)
        x = []
        y = []
        CL = airfoil_data['CL'][1]
        alpha = airfoil_data['CL'][0]
        title = f"{name} Lift Coefficient"
        for l in CL:
            y.append(l)
        for a in alpha:
            x.append(a)
        self.curveplot(x,y,"Alpha", "Cl", title)


    def plot_airfoil_drag(self):
        airfoil_data = self.ctx.airfoil_data
        name = self.ctx.airfoil
        #print(airfoil_data)
        x = []
        y = []
        CD = airfoil_data['CD'][1]
        alpha = airfoil_data['CD'][0]
        title = f"{name} Drag Coefficient"
        for d in CD:
            y.append(d)
        for a in alpha:
            x.append(a)
        self.curveplot(x,y,"Alpha", "Cd", title)

    def plot_airfoil_polar(self):
        name = self.ctx.airfoil
        #print(airfoil_data)
        xp = self.ctx.fitted_cd
        yp = self.ctx.fitted_cl
        title = f"{name} Polar"
        self.curveplot(xp,yp,"Cd", "Cl", title)

    def curveplot(self, xp,yp, xlabel, ylabel, title):
        #print("CD", xp)
        #print("CL",yp)
        plt.plot(xp,yp,)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()


def fit_curve(self, xp, yp):
    xi = np.array(xp)
    yi = np.array(yp)
    order = 1
    s = InterpolatedUnivariateSpline(xi, yi, k=order)
    return s


if __name__ == '__main__':
    xp = [0.008, 0.009, 0.010, 0.012, 0.014, 0.019, 0.024, 0.0335]
    yp = [0.06, 0.135, 0.20, 0.25, 0.30, 0.35, 0.395, 0.440]

    p = Plotter()
    p.curveplot(xp, yp, "Cl", "Cd", "McBeide B7 Polar")

