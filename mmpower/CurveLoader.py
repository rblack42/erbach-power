import os

class curveLoader(object):
    '''Manager for loading application curve data'''

    def __init__(self, dpath, dname, dfile):
        '''load data from app_data_dir/dpath/dname/dfile.txt'''
        self.dfile = dfile
        self.find_app_data()
        self.fpath = os.path.join(
                    self.app_data_dir,
                    dpath,
                    dname,
                    dfile + '.txt')
        if not os.path.isfile(self.fpath):
            print("data file no found:", self.fpath)

    def find_app_data(self):
        '''locate data in possible locations'''
        app_dir = os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),'data'
                )
        )
        self.app_data_dir = app_dir

    def load_data(self):
        data = {}
        try:
            with open(self.fpath,'r') as fin:
                name = fin.readline()
                lines = fin.readlines()
                points = []
                for l in lines:
                    d = l.strip()
                    if d == '': continue
                    x,y = d.split()
                    fx = float(x)
                    fy = float(y)
                    points.append([fx, fy])
                data['name'] = name.strip()
                data['file'] = self.dfile
                data['points'] = points
        except:
            print("data file load failure:", self.dpath)
        return data

if __name__ == '__main__':
    dl = CurveLoader('airfoil', 'mcbride-b7', 'CL')
    print(dl.load_data())

