import os

class DataFinder(object):
    """Locate available data direcrories for app"""

    def __init__(self, env_key=None, home_dir=None):
        '''check dirs named by environment key and home_dir name'''
        self.env_key = env_key
        self.home_dir = home_dir

    def get_data_dir_list(self):
        """return a list of available data directories"""
        dir_list = []
        # check configured environment variable
        if not self.home_dir is None:
            if self.env_key in os.environ:
                dp = os.environ[self.env_key]
                if os.path.isdir(dp):
                    dir_list.append[dp]

        # check home directory
        if not self.home_dir is None:
            from os.path import expanduser
            home = expanduser("~")
            hp = os.path.join(home, self.home_dir)
            if os.path.isdir(hp):
                dir_list.append(hp)

        # check application data directory
        dpath = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                'data'
            )
        )
        dir_list.append(dpath)
        return dir_list
