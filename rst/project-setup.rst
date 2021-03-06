Project Setup
#############

The first step in creating a Python application involves setting up the project directory. I use simple command line tools to manage my projects, so we will begin this setup by making (pun intended) sure that **make** works properly.

Step 1: Name the Project
************************

For this example, the project name will be **erbach-power**. I keep all active
projects in a directory named **_dev** in my home directory. (The **_** in
front of that name keeps this directory near the top of the folder list when
using Windows Explorer, Mac *Finder*, or a directory listing from the command
line.

..	code-block:: shell

	$ cd ~/_dev
	$ mkdir -perbach-power
	$ cd erbach-power

The **-p** option on the **mkdir** line lets you run this set of commands over
and over without problems. This is important to me, since my documentation
actually runs these commands when i build the web pages for this project. We
will cover documentation soon enough.

Step 2: Startup Makefile
************************

Long ago I created a modular Makefile* system to simplify creating a **Makefile** for a project. Basically, this file will be in your new project folder:

..  literalinclude:: ../Makefile
    :linenos:


