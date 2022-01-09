import sys

class CLI(object):
    """Primative event loop for commandline"""
    def __init__(self):
        self.running = True
        self.commands = ['airfoil', 'model', 'power', 'plot']

    def run(self):
        while self.running:
            print(">",end=" ")
            command = input()
            self.process_command(command)

        print("Program terminating...")
        sys.exit()

    def process_command(self,cmd):
        if cmd == 'quit':
            self.running = False
            return
        if cmd in self.commands:
            print("handled ", cmd)
        else:
            print("illegal command - ignored")



if __name__ == '__main__':
    cli = CLI()
    cli.run()

