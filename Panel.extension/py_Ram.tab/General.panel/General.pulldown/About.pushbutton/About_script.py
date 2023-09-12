# import libraries
import clr
# import pyrevit libraries
from pyrevit import forms

# Display message
form_message = "Thanks for using py_Ram, The Ram toolbar to support our template and content!" + "\n\n" + "If you have queries or suggestions about these tools, please reach me" + "\n" + "r.raja@wmeglobal.com"
forms.alert(form_message, title= "About py_Ram", warn_icon=False)