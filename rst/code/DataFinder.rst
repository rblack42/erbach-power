DataFinder
##########

..	automodule::	erbach.DataFinder
    :members:

Notes
*****

This module manages locating data directories in one of three locations

* A location defined by the **MATHMAGIC** environment variable

* The **MathMagik** directory in the user's home directory

* The **data** directory in the **mmflight** application source code directory.

The default data provided in that last directory was extracted from Erbach's
original Basic code.

For this program, the required data files will be located in the **model** and
**airfoils** subdirectories.

Data File Format
================

The data files are simple text files containing point data for the curve
defined. The first line in the file includes the name of the curve.
The curve is defined by a series of lines, each containing the **x** and  **y** values,
space separated.
