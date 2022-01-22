#cmd_dir.py

# Define our default class
class Plugin:
    """display current airfoil andmodel selections"""

    help = "airfoil plugin"

    def process(self, ctx):
        """show status"""
        print("Current status:")
        print("   airfoil:", ctx.airfoil)
        print("   model  :", ctx.model)

