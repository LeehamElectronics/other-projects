# ======================================================================================================================
# bevan matsacos
# 2/6/21
# ======================================================================================================================

# ======================================================================================================================
# vars and setup for them
# ======================================================================================================================

name_var_0 = "com port ="
val_var_0 = 5
export_var_0 = name_var_0 + str(val_var_0)

name_var_1 = "com speed ="
val_var_1 = 3800
export_var_1 = name_var_1 + str(val_var_1)

# ======================================================================================================================
# writes to the file with a new line per var
# ======================================================================================================================

file = open("Python.txt", "w")  # opens python.txt in write mode
file.write(repr(export_var_0) + "\n"
           + repr(export_var_1) + "\n")  # export var + new line writen to file
file.close()

# ======================================================================================================================
# reads the files based off line no form 0
# ======================================================================================================================

file = open("Python.txt")
read_lines = file.readlines()
import_var_0 = (read_lines[0])  # need to cut ' + /n off the end and len of name_var_0 off the start
import_var_1 = (read_lines[1])  # need to cut ' + /n off the end and len of name_var_0 off the start

# ======================================================================================================================
# cuts the imports to just data
# ======================================================================================================================

import_var_0 = (str(import_var_0)[len(name_var_0) + 1:len(name_var_0) + len(str(val_var_0)) + 1])  # same as below
import_var_1 = (str(import_var_1)[len(name_var_1) + 1:len(name_var_1) + len(str(val_var_1)) + 1])  # uses the len of
# the sent var to then cut the num out so you can edit the vars in the txt or in program

print(import_var_0)
print(import_var_1)
