#cmd_polar.py
from erbach.Plotter import Plotter
from erbach.CurveFit import CurveFit
from erbach.DataLoader import DataLoader
import numpy as np

class Plugin:
    """display current airfoil polar plot"""

    help = "generate curve fir function for airfoil coefficients"

    def process(self, ctx):
        """generate fit functions for Cl and Cd"""
        dl = DataLoader(ctx)
        dl.load_airfoil_data()
        cl= ctx.airfoil_data['CL'][1]
        alpha = ctx.airfoil_data['CL'][0]
        cf = CurveFit()
        cl_fit = cf.generate_fit_function(alpha, cl)
        ctx.fitted_airfoil_cl = cl_fit
        alpha = np.linspace(-5,20,50)
        ctx.fitted_cl = cl_fit(alpha)
        print(ctx.fitted_cl)
    
        cd= ctx.airfoil_data['CD'][1]
        alpha = ctx.airfoil_data['CD'][0]
        cf = CurveFit()
        cd_fit = cf.generate_fit_function(alpha, cd)
        ctx.fitted_airfoil_cd = cd_fit
        alpha = np.linspace(-5,20,50)
        ctx.fitted_cd = cd_fit(alpha)
        print(ctx.fitted_cd)

 
