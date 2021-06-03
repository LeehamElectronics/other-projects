from tkinter import *
from tkinter import ttk

# ===================================================================
# bevan matsacos
#
#
# ===================================================================


def read_bookings():
    pass


def store_name():
    pass


def search_guest():
    pass

# =========================================================================
#
# =========================================================================
root = Tk()  # starts the gui loop this runs the interface
root.title("store var")  # gui tittle

mainframe = ttk.Frame(root, padding="3 3 12 12")  # this is all styling
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# =========================================================================
#
# =========================================================================
name_var_0 = StringVar()
txtName = ttk.Entry(mainframe, width=20, textvariable=name_var_0)
txtName.grid(column=2, row=2, sticky=(W, E))

guest_name = StringVar()
txtTitle = ttk.Entry(mainframe, textvariable=guest_name)
txtTitle.grid(column=2, row=2, columnspan=4, sticky=(W, E))

search_name = StringVar()
ttk.Label(mainframe, textvariable=search_name).grid(column=2, row=5, columnspan=3, sticky=W)  # ttk.lable is a label displaing a given var

ttk.Label(mainframe, text="Name").grid(column=1, row=2, sticky=E)

guest_list = StringVar()
ttk.Label(mainframe, textvariable=guest_list).grid(column=1, row=14, columnspan=3, sticky=W)

ttk.Button(mainframe, text="save", command=search_guest).grid(column=2, row=3, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)  # styling

root.mainloop()  # marks the bottom of the loop
