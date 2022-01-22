from mmpower.DataFinder import DataFinder
import os

def test_data_loader_constructor(dirlist):
    """check default returns data path"""
    dp = dirlist[0]
    dl = DataFinder().get_data_dir_list()
    assert dp in dl

