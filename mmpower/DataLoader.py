import os

class DataLoader(object):
    """load data files for specified model, airfoil"""

    def __init__(self,ctx):
        """load ctx with model and airfoil data"""
        self.ctx = ctx

    def load_data(self):
        pass

    def get_data(self):
        return {
            'model': self.ctx.model,
            'airfoil': self.ctx.airfoil,
            'model_data': self.ctx.model_data,
            'airfoil_data': (self.ctx.CL, self.ctx.CD)
            }


