import os
import pint
u = pint.UnitRegistry()
Q_ = u.Quantity

class ModelLoader(object):
    '''Manager for loading application curve data'''

    def __init__(self, name = 'erbach'):
        '''load dictionary data from app_data_dir/dpath/dfile.txt'''

        self.find_app_data()
        self.fpath = os.path.join(
                    self.app_data_dir,
                    'model',
                    name + '.txt')
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
                nl = fin.readline().strip()
                n,v = nl.split()
                data[n[:-1]] = v.strip()
                print(n,v)
                lines = fin.readlines()
                for l in lines:
                    d = l.strip()
                    if d == '': continue
                    items = d.split()
                    if len(items) != 3:
                        print("bad data line", items)
                    n = items[0][:-1]
                    v = float(items[1])
                    vu = items[2]
                    val = Q_(v,vu)
                    print(n,val)
                    data[n] = val
        except:
            print("data file load failure:", self.fpath)
        return data

if __name__ == '__main__':
    ml = ModelLoader('hodson-wart')
    data = ml.load_data()
    print(data)

