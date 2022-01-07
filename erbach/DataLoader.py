import os


class DataLoader(object):
    """Manages loading of model and airfoil for project"""

    def __init__(self, model='default', airfoil='mcbride-b7'):
        """class constructor, model and airfoil parameters"""
        self.model = model
        self.airfoil = airfoil
        print(__file__)
        filepath = os.path.dirname(__file__)
        self.datadir = os.path.abspath(
            os.path.join(filepath,'../data'))

    def get_model_name(self):
        """returns current model name"""
        return self.model

    def get_airfoil_name(self):
        """returns current airfoil name"""
        return self.airfoil

    def get_datadir(self):
        """returns current data dir"""
        return self.datadir

    def set_data_dir(self, datadir):
        """set project data directory path"""
        if datadir.startswith('.'):
            # relative path
            filepath = os.path.dirname(__file__)
            self.datadir = os.path.abspath(
                os.path.join(filepath,datadir))
        elif datadir.startswith('~'):
            self.datadir = os.path.expanduser(datadir)
            print("HOME:",self.datadir)
        else:
            # absolute path
            print(datadir)
            self.datadir = os.path.abspath(datadir)


if __name__ == '__main__':
    dl = DataLoader('a','b')
    #dl.set_data_dir('~/data')
    print(dl.get_datadir())
