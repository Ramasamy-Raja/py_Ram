# import libraries
from pyrevit import forms
from Ram_msgUtils import *

# check if tools are muted
if msgUtils_muted():
	muteOn = forms.alert("Re-enable notifications?", title= "py_Ram is muted", warn_icon = False)
	if muteOn:
		msgUtils_muteOff()
else:
	muteOff = forms.alert("Disable notifications?", title= "py_Ram is not muted", warn_icon = False)
	if muteOff:
		msgUtils_muteOn()