import os
from . Context import Context
from . import utils
import json

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
        #/
        #print(afiles)
        return afiles

    def get_model_list(self):
        files = os.listdir(self.ctx.mpath)
        afiles = []
        for a in files:
            if a.startswith('.'): continue
            afiles.append(a[:-4])
        return afiles

    def get_model_data(self):
        model = self.ctx.model
        mpath = self.ctx.mpath
        #print("loading data for:", model, "from",mpath)
        mname = os.path.join(mpath, model+'.yml')
        data = utils.load_yaml_file(mname)
        #print(data)

    def load_airfoil_data(self):
        """read raw data files, extract Cl, Cd points"""
        airfoil = self.ctx.airfoil
        apath = self.ctx.apath
        #print("loading data for:", airfoil, "from",apath)
        adir = os.path.join(apath, airfoil)

        # load Cl data ---------------------------------
        aname = os.path.join(adir,"CL.yml")
        data = utils.load_yaml_file(aname)
        if data is None:
            aname = os.path.join(adir,'CL.json')
            data = utils.load_json_file(aname)
            if not data is None:
                #extract curve points from WAD data
                points = data['datasetColl'][0]['data']
                x = []
                y = []
                for p in points:
                    x.append(p['value'][0])
                    y.append(p['value'][1])
                data = (x,y)
        else:
            #extract curve points from yaml data
                points = data['data']
                x = []
                y = []
                for p in points:
                    x.append(p[0])
                    y.append(p[1])
                data = (x,y)
        CL = data

        # load Cd data ---------------------------------
        aname = os.path.join(adir,"CD.yml")
        data = utils.load_yaml_file(aname)
        if data is None:
            aname = os.path.join(adir,'CD.json')
            data = utils.load_json_file(aname)
            if not data is None:
                #extract curve points from WAD data
                points = data['datasetColl'][0]['data']
                x = []
                y = []
                for p in points:
                    x.append(p['value'][0])
                    y.append(p['value'][1])
                data = (x,y)
        else:
            #extract curve points from yaml data
                points = data['data']
                x = []
                y = []
                for p in points:
                    x.append(p[0])
                    y.append(p[1])
                data = (x,y)
        CD = data

        # save point setsin context
        self.ctx.airfoil_data = {'CL': CL, 'CD': CD}

    def get_airfoil_data(self):
        """return airfoil Cl, Cd points"""
        return self.ctx.airfoil_data


if __name__ =='__main__':
    ctx = Context()
    dl = DataLoader(ctx)
    dl.load_airfoil_data()
    print(dl.get_airfoil_data())

