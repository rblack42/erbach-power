from matplotlib import pyplot as plt

class Plotter(object):

    def __init__(self):
        pass

    def curveplot(self, xp,yp, xlabel, ylabel, title):
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

