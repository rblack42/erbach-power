import erbach
from erbach import __version__


def test_version():
    """Return current application version string"""
    mm = erbach
    assert mm.version() == __version__
