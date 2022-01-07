import pytest
import os
from erbach import utils


from erbach.CurveFit import CurveFit

def test_fit_function():
    """test fit function returns point from input"""
    xp = [1,2,3,4,5]
    yp = [5,4,3,2,1]
    cf=CurveFit();
    fitter = cf.generate_fit_function(xp, yp)
    assert fitter(3) == 3
