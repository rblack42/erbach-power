import matplotlib.pyplot as plt

class Plotter(object):
    '''General purpose line plotter class'''

    def __init__(self):
        """create plotter object"""
        pass

    def add_title(self, title):
        '''add title to plot'''
        plt.title(title)

    def add_labels(self, xlabel, ylabel):
        '''add labels to x and y axes'''
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

    def add_legend(self, loc):
        ''' add legend at specified location'''
        plt.legend(loc = loc)

    def add_line(self, xp, yp, label):
        plt.plot(xp, yp, label = label)

    def show_plot(self):
        plt.show()

if __name__ == '__main__':
    p = Plotter()
    x = [1,2,3,4,5]
    y = [0.3,0.5,0.6,0.5,0.4]
    p.add_title('test plot')
    p.add_labels('cl','cd')
    p.add_line(x,y,'polar')
    p.add_legend('upper right')
    p.show_plot()

