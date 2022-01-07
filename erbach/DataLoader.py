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

    # accessors -------------------------------------------------
    def get_model_name(self):
        """returns current model name"""
        return self.model

    def get_airfoil_name(self):
        """returns current airfoil name"""
        return self.airfoil

    def get_datadir(self):
        """returns current data dir"""
        return self.datadir

    def get_model_list(self):
        model_path = os.path.join(self.datadir,'models')
        files = os.listdir(model_path)
        models = []
        for f in files:
            n,e = f.split('.')
            models.append(n)
        return models

    def get_airfoil_list(self):
        airfoil_path = os.path.join(self.datadir,'airfoils')
        files = os.listdir(airfoil_path)
        airfoils = []
        for n in files:
            if not n.startswith('.'):
                airfoils.append(n)
        return airfoils

    # setters ---------------------------------------------------
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

    # mutatore - change state ------------------------------------
    def load_data(self):
        """load configured data files"""

        # load model data
        model = self.model
        # load airfoil cl, and cd data
        datadir = self._find_data_path('model', model)
        fileset = self._find_data_files('model', model)
        print("Loading:", datadir)
        print("files:", fileset)

        # load airfoil data
        airfoil = self.airfoil
        datadir = self._find_data_path('airfoil', airfoil)
        fileset = self._find_data_files('airfoil', model)
        print("loading:", datadir)
        print("files:", fileset)

    def _find_data_path(self, dtype, dpath):
        datadir = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../data', dtype, dpath))
        return datadir

    def _find_data_files(self, dtype, dname):
        """returns a list if available data files"""
        if dtype == 'model':
            return ["erbach-basic.yml"]
        else:
            return ["mcbride-b7/CL.yml", "mcbride-b7/CD.yml"]

if __name__ == '__main__':
    dl = DataLoader('a','b')
    #dl.set_data_dir('~/data')
    #print(dl.get_datadir())
    #print(dl.get_airfoil_list())
    dl.load_data()

