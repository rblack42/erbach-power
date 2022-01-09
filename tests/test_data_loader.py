from erbach.DataLoader import DataLoader
from erbach.Context import Context


def test_data_loader_constructor():
    """check defaults in dl"""
    ctx = Context()

    dl = DataLoader(ctx)
    assert dl.ctx.airfoil == "mcbride-b7"
    assert dl.ctx.apath.endswith("data/airfoils")
    assert dl.ctx.mpath.endswith("data/models")

def test_data_loader_constructor():
    """check default airfoil list"""
    ctx = Context()
    dl = DataLoader(ctx)
    assert "mcbride-b7" in dl.get_airfoil_list()

def test_data_loader_constructor():
    """check default model list"""
    ctx = Context()
    dl = DataLoader(ctx)
    assert "erbach-basic" in dl.get_model_list()


