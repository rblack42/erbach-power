import utils
import

class WebAppDigitizerLoader(object):
    """Manager for WebAppDigitized data files"""

    def __init__(self, name):
        """create manager for specified input file"""
        self.name = name

    def get_WAD_points(self):
        """extract curve points from WAD data"""
        points = self.data['datasetColl'][0]['data']
        x = []
        y = []
        for p in points:
            x.append(p['value'][0])
            y.append(p['value'][1])
        return x,y

    def WADreader(self):
        """read specified JSON data file"""
        data = utils.load_json_file(self.name)
        if data == None:
            print("Failed to load:", self.name)
            return [],[]
        else:
            points = data['datasetColl'][0]['data']
            x = []
            y = []
            for p in points:
                x.append(p['value'][0])
                y.append(p['value'][1])
            return x,y


if __name__ == '__main__':
    mgr = WebAppDigitizerLoader('data/airfoils/circular-arc-3%/CL.json')
    x,y = mgr.WADreader()
    print("X:",x)
    print("Y:",y)

