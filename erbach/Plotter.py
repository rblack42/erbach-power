from matplotlib import pyplot as plt
from . DataLoader  import DataLoader


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
        airfoil_data = self.ctx.airfoil_data
        name = self.ctx.airfoil
        #print(airfoil_data)
        x = []
        y = []
        CL = airfoil_data['CL'][1]
        CD = airfoil_data['CD'][1]
        title = f"{name} Polar"
        for l in CL:
            y.append(l)
        for d in CD:
            x.append(d)
        self.curveplot(x,y,"Cd", "Cl", title)

    def curveplot(self, xp,yp, xlabel, ylabel, title):
        #print("CD", xp)
        #print("CL",yp)
        plt.plot(xp,yp,)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()

if __name__ == '__main__':
    xp = [0.008, 0.009, 0.010, 0.012, 0.014, 0.019, 0.024, 0.0335]
    yp = [0.06, 0.135, 0.20, 0.25, 0.30, 0.35, 0.395, 0.440]

    p = Plotter()
    p.curveplot(xp, yp, "Cl", "Cd", "McBeide B7 Polar")

