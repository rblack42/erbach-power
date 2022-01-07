import pytest
import os

from erbach.DataLoader import DataLoader

# constructor tests ----------------------------------------
def test_constructor_no_parameters():
    """test constructor with no parameters"""
    dl = DataLoader()
    assert dl.get_airfoil_name() == 'mcbride-b7'
    assert dl.get_model_name() == 'default'

def test_constructor_with_no_model():
    """test constructor with no model specified"""
    dl = DataLoader(airfoil='circular-arc')
    assert dl.get_airfoil_name() == 'circular-arc'
    assert dl.get_model_name() == 'default'

def test_constructor_with_no_airfoil():
    """test constructor with no airfoil specified"""
    dl = DataLoader(model='hodson-wart')
    assert dl.get_airfoil_name() == 'mcbride-b7'
    assert dl.get_model_name() == 'hodson-wart'

def test_constructor_with_all_parameters():
    """test constructor with all parameters"""
    dl = DataLoader(model='hodson-wart', airfoil='circular-arc')
    assert dl.get_airfoil_name() == 'circular-arc'
    assert dl.get_model_name() == 'hodson-wart'

# test datadir setup --------------------------------------------
def test_default_datadir():
    """test default datadir option"""
    dl = DataLoader(model='hodson-wart', airfoil='circular-arc')
    dirname = os.path.dirname(__file__)
    datadir = os.path.abspath(
        os.path.join(dirname,'../data'))
    assert dl.get_datadir() == datadir

def test_set_relative_data_dir_path():
    """test setting relative datadir path"""
    dirname = os.path.dirname(__file__)
    relpath = "../testdata"
    dl = DataLoader(model='hodson-wart', airfoil='circular-arc')
    dl.set_data_dir(relpath)
    testpath = os.path.abspath(os.path.join(dirname,relpath))
    assert dl.get_datadir() == testpath

def test_set_home_data_dir_path():
    """test setting datadir path in home directory"""
    dirname = os.path.expanduser('~')
    relpath = "~/testdata"
    dl = DataLoader(model='hodson-wart', airfoil='circular-arc')
    dl.set_data_dir(relpath)
    testpath = os.path.abspath(os.path.join(dirname,'testdata'))
    assert dl.get_datadir() == testpath

def test_set_absolute_data_dir_path():
    """test setting datadir path to absolute path"""
    abspath = "/testdata"
    dl = DataLoader(model='hodson-wart', airfoil='circular-arc')
    dl.set_data_dir(abspath)
    assert dl.get_datadir() == abspath


