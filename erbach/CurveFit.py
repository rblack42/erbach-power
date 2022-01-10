import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline


class CurveFit(object):
    """Manages generating spline curve fit function"""

 
    def __init__(self):
        """constructor does no work"""
        pass

    def generate_fit_function(self, xd, yd):
        """return a spline fit function for input data set"""
        xi = np.array(xd)
        yi = np.array(yd)
        order = 1
        s = InterpolatedUnivariateSpline(xi, yi, k=order)
        return s
