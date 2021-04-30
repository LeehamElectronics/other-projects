

# =========================================================================
# Created by bevan matsacos
# start date 28/4/21
# =========================================================================
from tkinter import *
from tkinter import ttk
import time
import board
#import neopixel
import re
import math
import random
import numpy
import scipy
import sys
# =========================================================================
#
# =========================================================================


coords = []

def light_setup():
    coordfilename = "Python/coords.txt"

    fin = open(coordfilename, 'r')
    coords_raw = fin.readlines()

    coords_bits = [i.split(",") for i in coords_raw]

    for slab in coords_bits:
        new_coord = []
        for i in slab:
            new_coord.append(int(re.sub(r'[^-\d]', '', i)))
        coords.append(new_coord)

    PIXEL_COUNT = len(coords)  # this should be 500 | set up the pixels (AKA 'LEDs')

    pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, auto_write=False)


def light_spin():
    heights = []  # I get a list of the heights which is not overly useful here other than to set the max and min altitudes
    for i in coords:
        heights.append(i[2])

    min_alt = min(heights)
    max_alt = max(heights)

    # VARIOUS SETTINGS
    dinc = 1  # how much the rotation points moves each time
    buffer = 200  # a buffer so it does not hit to extreme top or bottom of the tree
    slow = 0  # pause between cycles (normally zero as it is already quite slow)
    angle = 0  # starting angle (in radians)
    inc = 0.1  # how much the angle changes per cycle
    colourA = [0, 50, 50]  # purple | the two colours in GRB order
    colourB = [50, 50, 0]  # yellow | if you are turning a lot of them on at once, keep their brightness down please depending on how good the power supply is

    # INITIALISE SOME VALUES
    swap01 = 0
    swap02 = 0
    direction = -1  # direct it move in
    c = 100  # the starting point on the vertical axis
    run = 1  # yes, I just run which run is true

    while run == 1:

        time.sleep(slow)

        LED = 0
        while LED < len(coords):
            if math.tan(angle) * coords[LED][1] <= coords[LED][2] + c:
                pixels[LED] = colourA
            else:
                pixels[LED] = colourB
            LED += 1

        # use the show() option as rarely as possible as it takes ages
        # do not use show() each time you change a LED but rather wait until you have changed them all
        pixels.show()

        # now we get ready for the next cycle

        angle += inc
        if angle > 2 * math.pi:
            angle -= 2 * math.pi
            swap01 = 0
            swap02 = 0

        # this is all to keep track of which colour is 'on top'

        if angle >= 0.5 * math.pi:
            if swap01 == 0:
                colour_hold = [i for i in colourA]
                colourA = [i for i in colourB]
                colourB = [i for i in colour_hold]
                swap01 = 1

        if angle >= 1.5 * math.pi:
            if swap02 == 0:
                colour_hold = [i for i in colourA]
                colourA = [i for i in colourB]
                colourB = [i for i in colour_hold]
                swap02 = 1

        c += direction * dinc  # and we move the rotation point

        if c <= min_alt + buffer:
            direction = 1
        if c >= max_alt - buffer:
            direction = -1

    return 'DONE'

def refresh():
    temp1 = colour_a.get()
    colour_a_old.set(temp1)

    temp2 = colour_b.get()
    colour_b_old.set(temp2)

    temp = direction.get()
    direction_old.set(temp)

    temp = Δ_point.get()
    Δ_point_old.set(temp)

    temp = Δ_angle.get()
    Δ_angle_old.set(temp)

    temp = angle.get()
    Δ_angle_old.set(temp)

    temp7 = speed.get()
    speed_old.set(temp7)

# =========================================================================
# a
# =========================================================================

root = Tk()
root.title("tree+gui")

# =========================================================================
#
# =========================================================================
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# =========================================================================
# With Tkinter we need to to update values on the screen we need to use
# a StingVar() we assign these here and then use these with the textvariable
# in "Entry" widgets
# =========================================================================
colour_a = StringVar()
colour_a_old = StringVar()
txtcolour_a = ttk.Entry(mainframe, textvariable=colour_a)
txtcolour_a.grid(column=2, row=2, columnspan=1, sticky=(W, E))
ttk.Label(mainframe, text="colour a").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, textvariable=colour_a_old).grid(column=3, row=2, columnspan=3, sticky=E)

colour_b = StringVar()
colour_b_old = StringVar()
txtcolour_b = ttk.Entry(mainframe, textvariable=colour_b)
txtcolour_b.grid(column=2, row=3, columnspan=1, sticky=(W, E))
ttk.Label(mainframe, text="colour b").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, textvariable=colour_b_old).grid(column=3, row=3, columnspan=3, sticky=E)

direction = StringVar()
direction_old = StringVar()
txtdirection = ttk.Entry(mainframe, textvariable=direction)
txtdirection.grid(column=2, row=4, columnspan=1, sticky=(W, E))
ttk.Label(mainframe, text="direction").grid(column=1, row=4, sticky=E)
ttk.Label(mainframe, textvariable=direction_old).grid(column=3, row=4, columnspan=3, sticky=E)

Δ_point = StringVar()
Δ_point_old = StringVar()
txtΔ_point = ttk.Entry(mainframe, textvariable=Δ_point)
txtΔ_point.grid(column=2, row=5, columnspan=1, sticky=(W, E))
ttk.Label(mainframe, text="Δ_point").grid(column=1, row=5, sticky=E)
ttk.Label(mainframe, textvariable=Δ_point_old).grid(column=3, row=5, columnspan=3, sticky=E)

angle = StringVar()
angle_old = StringVar()
txtangle = ttk.Entry(mainframe, textvariable=angle)
txtangle.grid(column=2, row=6, columnspan=1, sticky=(W, E))
ttk.Label(mainframe, text="angle").grid(column=1, row=6, sticky=E)
ttk.Label(mainframe, textvariable=angle_old).grid(column=3, row=6, columnspan=3, sticky=E)

Δ_angle = StringVar()
Δ_angle_old = StringVar()
txtΔ_angle = ttk.Entry(mainframe, textvariable=angle)
txtΔ_angle.grid(column=2, row=7, columnspan=1, sticky=(W, E))
ttk.Label(mainframe, text="Δ_angle").grid(column=1, row=7, sticky=E)
ttk.Label(mainframe, textvariable=Δ_angle_old).grid(column=3, row=7, columnspan=3, sticky=E)

speed = StringVar()
speed_old = StringVar()
txtspeed = ttk.Entry(mainframe, textvariable=angle)
txtspeed.grid(column=2, row=8, columnspan=1, sticky=(W, E))
ttk.Label(mainframe, text="speed").grid(column=1, row=8, sticky=E)
ttk.Label(mainframe, textvariable=speed_old).grid(column=3, row=8, columnspan=3, sticky=E)

ttk.Button(mainframe, text="refresh", command=refresh).grid(column=3, row=10, sticky=E)



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
