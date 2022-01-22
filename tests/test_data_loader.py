from mmpower.DataLoader import DataLoader
import os


def test_data_loader_constructor(dirlist,ctx):
    """check default returns data path"""
    dp = dirlist[0]
    dl = DataLoader(ctx).get_data()
    assert dp in dl

