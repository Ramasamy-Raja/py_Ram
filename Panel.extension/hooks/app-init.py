# import pyrevit libraries
import clr
from pyrevit import forms,script
from Ram_msgUtils import *

# check if notifications are disabled
if msgUtils_muted():
	script.exit()

# Get icon file (doesn't work)
# curPath = script.get_script_path()
# remPath = curPath.split('py_Ram.tab')[0]
# icoFile = remPath + r'bin\Graphics\icons_01.ico'

# Display the message to the user
forms.toast("Toolbar has been loaded!","py_Ram for Revit",appid="py_Ram")