# Utility functions
import os
import yaml
import json


def normalize(n,d):
	"""reduce floating point number to n digits"""
	f = 10**n
	di = int(d * f)
	return di/f

def load_json_file(name):
        """return data from JSON file"""
        cwd = os.getcwd()
        ypath = os.path.abspath(os.path.join(cwd,name))
        #print("U:", ypath)

        if os.path.isfile(ypath):
            try:
                with open(ypath,'r') as fin:
                    data = json.load(fin)
            except:
                #print("json file failed to load:", ypath)
                return None
            return data
        #print("file not found: ->{}<-".format(ypath))
        return None

def load_yaml_file(name):
    """return data from a YML file"""
    cwd = os.getcwd()
    ypath = os.path.abspath(os.path.join(cwd,name))
    #print("U:", ypath)
    if os.path.isfile(ypath):
        try:
            with open(ypath,'r') as fin:
                data = yaml.safe_load(fin)
        except:
            #print("yaml file failed to load:", ypath)
            return None
        return data
    #print("file not found: ->{}<-".format(ypath))
    return None

if __name__ == '__main__':
    data = load_yaml_file("./tests/test_data/sample.yml")
    print(data)

