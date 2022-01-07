import pytest
import os


from erbach import utils

def test_normalize():
    """test reducing precision of floating point numbers"""
    fp = 1.234
    fpn = 1.2
    assert(utils.normalize(1,fp) == fpn)

# test json file loader ----------------------------------------------
def test_load_json_file():
    """check that loading sample json file does not return None"""
    assert utils.load_json_file("./tests/test_data/sample.json") != None

def test_load_sample_json_file():
    """check that loading bad file name returns None"""
    assert utils.load_json_file("junk") == None

# test yaml file loader ----------------------------------------------
def test_load_yaml_file():
    """check that loading sample yaml file does not return None"""
    print("CWD:", os.getcwd())
    assert utils.load_yaml_file("./tests/test_data/sample.yml") != None

def test_load_sample_yaml_file():
    """check that loading bad file name returns None"""
    assert utils.load_yaml_file("junk") == None

def test_load_sample_yaml_file():
    """check that loading bad file name returns None"""
    assert utils.load_yaml_file("~/.erbach/sample.yml") == None
