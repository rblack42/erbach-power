import os


class DataLoader(object):
    """Manage loading airfoil and model data"""

    def __init__(self, ctx):
        self.ctx = ctx
        cwd = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
        self.ctx.apath = os.path.join(cwd ,'data', 'airfoils')
        self.ctx.mpath = os.path.join(cwd ,'data', 'models')

    def get_airfoil_list(self):
        files = os.listdir(self.ctx.apath)
        afiles = []
        for a in files:
            if a.startswith('.'): continue
            afiles.append(a)
        print(afiles)
        return afiles

    def get_model_list(self):
        files = os.listdir(self.ctx.mpath)
        afiles = []
        for a in files:
            if a.startswith('.'): continue
            afiles.append(a[:-4])
        return afiles

