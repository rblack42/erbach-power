
class Airfoil(object):
    '''manages airfoil data'''

    def __init__(self, ctx):
        self.ctx = ctx

    def set_airfoil(self, name):
        '''change current airfoil'''
        self.name = name
        self.load_coefficients()

