import numpy as np
from . DataLoader  import DataLoader

class Erbach(object):
    """calculate level flight power and velocity"""

    def __init__(self, ctx):
        """ save the incoming context"""
        self.ctx = ctx
        model = ctx.model
        dl = DataLoader(ctx)
        dl.load_model_data()
        model_data = ctx.model_data
        print(model)
        print(model_data)

