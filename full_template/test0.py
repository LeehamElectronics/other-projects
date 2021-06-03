from tkinter import *
from tkinter import ttk


# ===================================================================
# bevan matsacos
# 2/6/21
# tk template for variables
# ===================================================================


def read():
    file = open("Python.txt")
    read_lines = file.readlines()

    import_var_0 = (read_lines[0])
    val_var_0.set(import_var_0[len(str(name_var_0.get())) + 1
                               :len(str(import_var_0)) - 2])  # - 2 from end

    import_var_1 = (read_lines[1])
    val_var_1.set(import_var_1[len(str(name_var_1.get())) + 1
                               :len(str(import_var_1)) - 2])
    file.close()


def save():
    export_var_0 = str(name_var_0.get()) + val_var_0.get()
    export_var_1 = str(name_var_1.get()) + val_var_1.get()

    file = open("Python.txt", "w")  # opens python.txt in write mode
    file.write(repr(export_var_0) + "\n" +
               repr(export_var_1) + "\n")  # export var + new line writen to file
    file.close()
    read()


# =========================================================================
#
# =========================================================================
root = Tk()
root.title("store var")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# =========================================================================
#
# =========================================================================
import_var_0 = StringVar()
name_var_0 = StringVar()
val_var_0 = StringVar()
name_var_0.set("Com port    = ")
txtTitle = ttk.Entry(mainframe, textvariable=val_var_0)
txtTitle.grid(column=2, row=1, columnspan=4, sticky=(W, E))
ttk.Label(mainframe, text=name_var_0.get()).grid(column=1, row=1, sticky=E)

import_var_1 = StringVar()
name_var_1 = StringVar()
val_var_1 = StringVar()
name_var_1.set("Com speed = ")
txtTitle = ttk.Entry(mainframe, textvariable=val_var_1)
txtTitle.grid(column=2, row=2, columnspan=4, sticky=(W, E))
ttk.Label(mainframe, text=name_var_1.get()).grid(column=1, row=2, sticky=E)

ttk.Button(mainframe, text="save", command=save).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="read", command=read).grid(column=1, row=3, sticky=W)

read()

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()
