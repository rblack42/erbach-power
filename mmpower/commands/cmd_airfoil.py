#cmd_airfoil.py
from mmpower.DataLoader import DataLoader

# Define our default class
class Plugin:
    help = "airfoil plugin"

    def process(self, ctx):
        dl = DataLoader(ctx)
        alist = dl.get_airfoil_list()
        n = len(alist)
        i = 1
        print("select airfoil")
        for a in alist:
            if ctx.airfoil == a:
                tag = "*"
            else:
                tag = " "
            print(f"  {i}: {a} {tag}")
            i += 1
        print("  0: exit")
        print("\nEnter choice:", end=" ")
        choice = int(input())
        if choice < 1 or choice>n:
            if choice == 0:
                return
            print("bad choice")
        else:
            ctx.airfoil = alist[choice-1]
            print("selected:", ctx.airfoil)

        ctx.argcount +=1
