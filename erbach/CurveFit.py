import numpy as np
from scipy import interpolate


class CurveFit(object):
    """Manages generating spline curve fit functin for inputX-Y data lists"""

    def __init__(self):
        """constructor does no work"""
        pass

    def generate_fit_function(self, xd, yd):
        """return a spline fit function for input data set"""
        xi = np.array(xd)
        yi = np.array(yd)
        order = 1
        s = interpolate.InterpolatedUnivariateSpline(xi, yi, k=order)
        return s
