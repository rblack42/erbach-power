Event Loops
###########

This program is designed to run until the user explicitly stops it. While
running it waits for the user to enter some command. It runs that command and
returns to the loop waiting for another command. The loop that manages this
process is called an *Event Loop*.

In a sophisticated program, each action is runin a separate thread so the user
gets control back quickly. This is how many games are written, but for our
purposes, all we need is a simple loop like thia:


..  code-block:: python

    while True:
        do-something()

This loops great, but it hasnot way to terminate, short of killing the program.
It would be better to setup the loop in a slightly different way:

..  code-block:: python

    running = true
    while  running:
        running = dosimething()

Now, weask our **dosomething** routine to return a value that will contol whether or not we
continue in the loop.


