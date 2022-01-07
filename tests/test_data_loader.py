import pytest
import os

from erbach.DataLoader import DataLoader

 
def test_constructor_no_parameters():
    dl = DataLoader()
    assert dl.get_airfoil_name() == 'mcbride-b7'
    assert dl.get_model_name() == 'default'

def test_constructor_with_no_model():
    dl = DataLoader(airfoil='circular-arc')
    assert dl.get_airfoil_name() == 'circular-arc'
    assert dl.get_model_name() == 'default'

def test_constructor_with_no_airfoil():
    dl = DataLoader(model='hodson-wart')
    assert dl.get_airfoil_name() == 'mcbride-b7'
    assert dl.get_model_name() == 'hodson-wart'

def test_constructor_with_all_parameters():
    dl = DataLoader(model='hodson-wart', airfoil='circular-arc')
    assert dl.get_airfoil_name() == 'circular-arc'
    assert dl.get_model_name() == 'hodson-wart'

def test_default_datadir():
    dl = DataLoader(model='hodson-wart', airfoil='circular-arc')
    datadir = os.path.abspath(
        os.path.join(__file__,'../data'))
    assert dl.get_datadir() == datadir


