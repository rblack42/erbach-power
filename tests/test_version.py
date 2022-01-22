import mmpower
from mmpower import __version__


def test_version():
    """Return current application version string"""
    mm = mmpower
    assert mm.version() == __version__
