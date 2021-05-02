from tkinter import *
from tkinter import ttk

guests = []


# ===================================================================
# bevan matsacos
# 16th 3 2021
# step 4 ela
# this code reads and edits a textfile through python and uses tkinter as a interface
# ===================================================================


def read_bookings():
    bookings = 'bookings.txt'  # sets bookings to be the name of the file
    f = open(bookings, "r")  # opens bookings to read

    guest_list.set('')  # sets the guest list to be blank

    for line in f.readlines():  # reads each line striping \n from the end
        line = line.rstrip('\n')
        guests.append(line)  # apends the guest list as it goes
    f.close()  # closes f eg open bookings

    for guest in guests:
        guest_details = (guest_list.get() + '\n' +
                         guest)
        guest_list.set(guest_details)


def store_name():
    bookings = 'bookings.txt'  # sets bookings to be the name of the file
    f = open(bookings, 'a+')  # opens bookings in append mode so when it gets a new value it
    temp = guest_name.get()  # sets temp to guest_names value
    f.write('%s\n' % temp)  # writes to the f so adds the new name to the bottom of the txt file
    guest_name.set('')  # clears the name
    f.close()


def search_guest():  # i don't know how this works enough to explain
    totalplaynum = 4  # total times it searches
    guest = guest_list.get()
    search_name = guest_name.get()
    print(guest)

    count = 0
    found = False

    while True:  # loops till it has found the entered guest_name or till it reaches 4 searches
        if search_name == guest[count]:
            found = True
            search_name.set('True')
        count = count + 1
        if found is True or count == totalplaynum:
            break  # breaks the loop


# =========================================================================
#
# =========================================================================
root = Tk()  # starts the gui loop this runs the interface
root.title("Ulumbarra Bookings")  # gui tittle

mainframe = ttk.Frame(root, padding="3 3 12 12")  # this is all styling
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# =========================================================================
#
# =========================================================================
guestName = StringVar()  # defines guest name as a string var
txtName = ttk.Entry(mainframe, width=20, textvariable=guestName)  # ttk entry means a box the user can input data and text var is what var the data is assigned to
txtName.grid(column=2, row=2, sticky=(W, E))

guest_name = StringVar()
txtTitle = ttk.Entry(mainframe, textvariable=guest_name)
txtTitle.grid(column=2, row=2, columnspan=4, sticky=(W, E))

search_name = StringVar()
ttk.Button(mainframe, text="Save", command=store_name).grid(column=3, row=3, sticky=W)  # ttk.button is a button with a lable of text=" " and does a cerant command
ttk.Label(mainframe, textvariable=search_name).grid(column=2, row=5, columnspan=3, sticky=W)  # ttk.lable is a label displaing a given var

ttk.Label(mainframe, text="Name").grid(column=1, row=2, sticky=E)

guest_list = StringVar()
ttk.Label(mainframe, textvariable=guest_list).grid(column=1, row=14, columnspan=3, sticky=W)

ttk.Button(mainframe, text="search", command=search_guest).grid(column=2, row=3, sticky=W)

read_bookings()

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)  # styling

txtName.focus_set()
root.mainloop()  # marks the bottom of the loop
