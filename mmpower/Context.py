class Context(object):
    """manages data passed between commands"""

    model = "erbach"
    airfoil = "mcbride-b7"
    env_key = "MATHMAGIK"
    home_dir = "MathMagik"
    airfoil_data = ()
    model_data = {}
    CL = []
    CD= {}

