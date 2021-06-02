name_var_1 = "com port ="
val_var_1 = 2
export_var_1 = name_var_1 + str(val_var_1)

name_var_2 = "com speed ="
val_var_2 = 3600
export_var_2 = name_var_2 + str(val_var_2)


file = open("Python.txt", "w")
file.write(repr(export_var_1) + "\n" + repr(export_var_2) + "\n")
file.close()

file = open("Python.txt")
read_lines = file.readlines()
import_var_1 = (read_lines[1 - 1])  # need to cut ' + /n off the end and len of name_var_1 off the start
import_var_2 = (read_lines[2 - 1])  # need to cut ' + /n off the end and len of name_var_1 off the start





print(import_var_1)
print(import_var_2)
