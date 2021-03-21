# ===================================================================
# Created by Warren Sutton
# Date: 19 Jan 2020
# Purpose: Ulumbarra booking task Draft 1
# ===================================================================
from tkinter import *
from tkinter import ttk
import serial

ser = serial.Serial(
    port='COM3',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)


# ===================================================================
# The following function runs when when the save button
# is clicked, by virtue of the "command" parameter linking the
# function to the respective button. This is the most important
# section of code.
# ===================================================================

guests = []

def read_bookings():
    bookings = 'bookings.txt'
    f = open(bookings, "r")

    guest_list.set('')

    for line in f.readlines():
        line = line.rstrip('\n')
        guests.append({})
        guests[-1]['Title'] = line

    f.close()

    for guest in guests:
        guest_details = (guest_list.get() + '\n' +
                         guest['Title'])
        guest_list.set(guest_details)


def store_name():
    for line in ser.readline():
        bookings = 'bookings.txt'
        f = open(bookings, 'a+')
        f.write('%s\n' % chr(line))
        guest_name.set('')
        print(chr(line))
        f.close()


# =========================================================================
# Much of the remaining code is around setting up and dealing with
# the graphical display using tkinter. You should try to understand the
# basics of tkinter, but for each project and step you can copy and modify
# code from other projects, rather than trying to write the code from scratch.
# =========================================================================

root = Tk()
root.title("Ulumbarra Bookings")

# =========================================================================
# The following are templated setup taken from other examples
# You don't need to worry too much about the setup for now
# =========================================================================
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# =========================================================================
# The following section of code relies on Pillow Package being installed
# and for the image 'logo.jpg' being in the local path
# Pillow allows the image to be resized (scaled) to the desired size.
# The image is then placed into a Label which is placed into the grid.
# =========================================================================

# =========================================================================
# With Tkinter we need to to update values on the screen we need to use
# a StingVar() we assign these here and then use these with the textvariable
# in "Entry" widgets
# =========================================================================
guestName = StringVar()
txtName = ttk.Entry(mainframe, width=20, textvariable=guestName)
txtName.grid(column=2, row=2, sticky=(W, E))
guest_name = StringVar()
txtTitle = ttk.Entry(mainframe, textvariable=guest_name)
txtTitle.grid(column=2, row=2, columnspan=4, sticky=(W, E))

ttk.Button(mainframe, text="Save", command=store_name).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Name").grid(column=1, row=2, sticky=E)

guest_list = StringVar()
ttk.Label(mainframe, textvariable=guest_list).grid(column=1, row=14, columnspan=3, sticky=W)
store_name()
read_bookings()

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

txtName.focus_set()
root.mainloop()
