Command Line interface
######################

This program uses the **click** library to set up the command line interface.
This part of the design is important since it is the primary link to the human
user.

I will be using something called *Railroad Diagrams*, popular in defining
programming languages to show the command set supported by the commaind line
application.

..	note::

    The graphical user interface is coming. I develop the basic applicaion
    first, then add the GUI layer after tt==things are working well.

Here is an example of oneof these diagrams. We will introduce the command
syntax in the next section.

.. parser-rule-diagram:: 'def' ID '(' (arg (',' arg)*)? ')' ':'

Basic Commands
**************

The top-level commands are these:

..  parser-rule-diagram::   ('airfoil' | 'model') ('-i' name)? ('load' | 'set' | 'plot')?

The reason these are caled *railroad diagrams* should be apparent here. The
rounded boxes are things you type exactly. The rectabgular boxes are where you
come up with your own thing to enter. **name** in this example is the name of
the airfoil od the model you want to study.
