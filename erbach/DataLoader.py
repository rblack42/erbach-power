import os


class DataLoader(object):

    def __init__(self, model='default', airfoil='mcbride-b7'):
        self.model = model
        self.airfoil = airfoil
        print(__file__)
        filepath = os.path.dirname(__file__)
        self.datadir = os.path.abspath(
            os.path.join(filepath,'../data'))

    def get_model_name(self):
        return self.model

    def get_airfoil_name(self):
        return self.airfoil

    def get_datadir(self):
        return self.datadir

    def set_data_dir(self, datadir):
        if datadir.startswith('.'):
            # relative path
            cwd = os.getcwd()
            self.datadir = os.path.abspath(
                os.path.join(cwd,datadir))
        elif datadir.startswith('~'):
            self.datadir = os.path.expanduser(datadir)
        else:
            # absolute path
            print(datadir)
            self.datadir = os.path.abspath(datadir)
            

if __name__ == '__main__':
    dl = DataLoader('a','b')
    dl.set_data_dir('~/data')
    print(dl.get_datadir())
