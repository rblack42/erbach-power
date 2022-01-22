#deafult.py
# Define our default class

class Plugin:
    help = "default plugin"

    # Define static method, so no self parameter
    def process(self, ctx2):
        # Some prints to identify which plugin is been used
        print("This is my default plugin")
        print(f"Numbers are {num1} and {num2}")
        ctx['argcount'] += 5
