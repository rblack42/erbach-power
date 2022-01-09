#cmd_model.py
from erbach.DataLoader import DataLoader

class Plugin:
    help = "model plugin"

    def process(self, ctx):
        dl = DataLoader(ctx)
        alist = dl.get_model_list()
        n = len(alist)
        i = 1
        print("select model")
        for a in alist:
            if ctx.model == a:
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
            ctx.model = alist[choice-1]
            print("selected:", ctx.model)

        ctx.argcount +=1
