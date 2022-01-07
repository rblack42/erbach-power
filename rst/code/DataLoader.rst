DataLoader
##########

..	automodule::	erbach.DataLoader
    :members:

Notes
*****

The **DataLoader** class manages loading model and airfoil data files located in
the configured **datapath** attribute.

For model data, one data file, either **YAML** or **JSON** should be in a
**<datadir>/models/<model>/name>.{yml | json}** file.

For airfoils, the data files are located under the airfoil name folder:
<datadir>/airfoils/<airfoil-name>/{CL|CD}.{yml|json}**. If the file is a **JSON**
file, it is assumed to have been created using the *WebAppDigitizer*
application. All installed airfoils need at lease a **CL.{yml|json}** and
**CD.{yml|json}**. files. Other files may be present, but they will not be loaded
normally.


