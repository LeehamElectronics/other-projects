# =========================================================================
# Created by bevan matsacos
# start date 28/4/21
# this is unfinished code for controling the tree leds
# =========================================================================
from tkinter import *
from tkinter import ttk
import time
import board
# import neopixel
import re
import math
import random
import numpy
import scipy
import sys

# =========================================================================
# function
# =========================================================================
cords = []


# =========================================================================
# tab2
# =========================================================================
def startstoptab2():  # the pass is just to stop it erroing out while theres no code there
    pass


def cleartab2():  # the tab2 at the end isnt reqired i just do that as my way of nameing
    pass


def refreshtab2():  # this is a save or update comand it sets whats been typed in the boxes to the running ones to stop breaking by mistake
    temp = colour_a.get()
    colour_a_old.set(temp)
    temp = colour_b.get()
    colour_b_old.set(temp)
    temp = direction.get()
    direction_old.set(temp)
    temp = Δ_point.get()
    Δ_point_old.set(temp)
    temp = Δ_angle.get()
    Δ_angle_old.set(temp)
    temp = angle.get()
    angle_old.set(temp)
    temp = speed.get()
    speed_old.set(temp)


# ======================================================================================================================
# tab 3:snake
# ======================================================================================================================
def startstoptab3():
    pass


def cleartab3():
    pass


def refreshtab3():
    pass


# ======================================================================================================================
# tab 4:temp1
# ======================================================================================================================
def startstoptab4():
    pass


def cleartab4():
    pass


def refreshtab4():
    pass


# ======================================================================================================================
# tab 5:temp2
# ======================================================================================================================
def startstoptab5():
    pass


def cleartab5():
    pass


def refreshtab5():
    pass


# ======================================================================================================================
# tab 6:debug
# ======================================================================================================================
def read_cords_tab6():
    pass


def set_tab6():
    pass


def start_stop_tab6():
    pass


def forward_tab6():
    pass


def back_tab6():
    pass


set_tab6
# ======================================================================================================================

root = Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)  # adds tabs to the tkinter
tabControl.pack(expand=1, fill="both")  # i dont know what this does i just know its needed

# ======================================================================================================================
# tab 1:title
# ======================================================================================================================
tab1 = ttk.Frame(tabControl)  # creates the tab 1
tabControl.add(tab1, text='title')  # gives tab 1 a tittle

ttk.Label(tab1, text="temp").grid(column=1, row=1, sticky=E)  # insted of "ttk.Label(mainframe" on the non tabed one we just put the tab number in its place

# ======================================================================================================================
# tab 2:spin
# ======================================================================================================================
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='spin')

colour_a = StringVar()
colour_a_old = StringVar()
txtcolour_a = ttk.Entry(tab2, textvariable=colour_a)
txtcolour_a.grid(column=2, row=2, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="colour a").grid(column=1, row=2, sticky=E)
ttk.Label(tab2, textvariable=colour_a_old).grid(column=3, row=2, columnspan=1, sticky=E)

colour_b = StringVar()
colour_b_old = StringVar()
txtcolour_b = ttk.Entry(tab2, textvariable=colour_b)
txtcolour_b.grid(column=2, row=3, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="colour b").grid(column=1, row=3, sticky=E)
ttk.Label(tab2, textvariable=colour_b_old).grid(column=3, row=3, columnspan=1, sticky=E)

direction = StringVar()
direction_old = StringVar()
txtdirection = ttk.Entry(tab2, textvariable=direction)
txtdirection.grid(column=2, row=4, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="direction").grid(column=1, row=4, sticky=E)
ttk.Label(tab2, textvariable=direction_old).grid(column=3, row=4, columnspan=1, sticky=E)

Δ_point = StringVar()
Δ_point_old = StringVar()
txtΔ_point = ttk.Entry(tab2, textvariable=Δ_point)
txtΔ_point.grid(column=2, row=5, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="Δ_point").grid(column=1, row=5, sticky=E)
ttk.Label(tab2, textvariable=Δ_point_old).grid(column=3, row=5, columnspan=1, sticky=E)

angle = StringVar()
angle_old = StringVar()
txtangle = ttk.Entry(tab2, textvariable=angle)
txtangle.grid(column=2, row=6, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="angle").grid(column=1, row=6, sticky=E)
ttk.Label(tab2, textvariable=angle_old).grid(column=3, row=6, columnspan=1, sticky=E)

Δ_angle = StringVar()
Δ_angle_old = StringVar()
txtΔ_angle = ttk.Entry(tab2, textvariable=Δ_angle)
txtΔ_angle.grid(column=2, row=7, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="Δ_angle").grid(column=1, row=7, sticky=E)
ttk.Label(tab2, textvariable=Δ_angle_old).grid(column=3, row=7, columnspan=1, sticky=E)

speed = StringVar()
speed_old = StringVar()
txtspeed = ttk.Entry(tab2, textvariable=speed)
txtspeed.grid(column=2, row=8, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="speed").grid(column=1, row=8, sticky=E)
ttk.Label(tab2, textvariable=speed_old).grid(column=3, row=8, columnspan=1, sticky=E)

ttk.Button(tab2, text="start/stop", command=startstoptab2).grid(column=1, row=10, sticky=E)
ttk.Button(tab2, text="clear", command=cleartab2).grid(column=2, row=10, sticky=E)
ttk.Button(tab2, text="refresh", command=refreshtab2).grid(column=3, row=10, sticky=E)

# ======================================================================================================================
# tab 3:snake
# ======================================================================================================================
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='snake')

ttk.Label(tab3, text="temp1").grid(column=1, row=1, sticky=E)

ttk.Button(tab3, text="start/stop", command=startstoptab3).grid(column=1, row=10, sticky=E)
ttk.Button(tab3, text="clear", command=cleartab3).grid(column=2, row=10, sticky=E)
ttk.Button(tab3, text="refresh", command=refreshtab3).grid(column=3, row=10, sticky=E)

# ======================================================================================================================
# tab 4:temp1
# ======================================================================================================================
tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text='temp1')

ttk.Label(tab4, text="temp1").grid(column=1, row=1, sticky=E)

ttk.Button(tab4, text="start/stop", command=startstoptab4).grid(column=1, row=10, sticky=E)
ttk.Button(tab4, text="clear", command=cleartab4).grid(column=2, row=10, sticky=E)
ttk.Button(tab4, text="refresh", command=refreshtab4).grid(column=3, row=10, sticky=E)

# ======================================================================================================================
# tab 5:temp2
# ======================================================================================================================
tab5 = ttk.Frame(tabControl)
tabControl.add(tab5, text='temp2')

ttk.Label(tab5, text="temp2").grid(column=1, row=1, sticky=E)

ttk.Button(tab5, text="start/stop", command=startstoptab5).grid(column=1, row=10, sticky=E)
ttk.Button(tab5, text="clear", command=cleartab5).grid(column=2, row=10, sticky=E)
ttk.Button(tab5, text="refresh", command=refreshtab5).grid(column=3, row=10, sticky=E)

# ======================================================================================================================
# tab 6:debug
# ======================================================================================================================
tab6 = ttk.Frame(tabControl)
tabControl.add(tab6, text='debug')

ttk.Label(tab6, text="light setup").grid(column=1, row=1, sticky=E)

tab6_light_num = StringVar()
txttab6_light_num = ttk.Entry(tab6, textvariable=tab6_light_num)
txttab6_light_num.grid(column=2, row=2, columnspan=1, sticky=(W, E))
ttk.Label(tab6, text="light num").grid(column=1, row=2, sticky=E)

ttk.Button(tab6, text="set", command=set_tab6).grid(column=3, row=2, sticky=E)

ttk.Label(tab6, text="light position").grid(column=1, row=3, sticky=E)

tab6_x = StringVar()
txttab6_x = ttk.Entry(tab6, textvariable=tab6_x)
txttab6_x.grid(column=2, row=4, columnspan=1, sticky=(W, E))
ttk.Label(tab6, text="x").grid(column=1, row=4, sticky=E)

tab6_y = StringVar()
txttab6_y = ttk.Entry(tab6, textvariable=tab6_y)
txttab6_y.grid(column=2, row=5, columnspan=1, sticky=(W, E))
ttk.Label(tab6, text="y").grid(column=1, row=5, sticky=E)

tab6_z = StringVar()
txttab6_z = ttk.Entry(tab6, textvariable=tab6_z)
txttab6_z.grid(column=2, row=6, columnspan=1, sticky=(W, E))
ttk.Label(tab6, text="z").grid(column=1, row=6, sticky=E)

tab6_grb = StringVar()  # one variable cut up in the format of 0, 0, 0 will be cut by the function
txttab6_grb = ttk.Entry(tab6, textvariable=tab6_grb)
txttab6_grb.grid(column=2, row=7, columnspan=1, sticky=(W, E))
ttk.Label(tab6, text="grb").grid(column=1, row=7, sticky=E)

ttk.Button(tab6, text="start/stop", command=start_stop_tab6).grid(column=1, row=8, sticky=E)
ttk.Button(tab6, text="back", command=back_tab6).grid(column=2, row=8, sticky=E)
ttk.Button(tab6, text="forward", command=forward_tab6).grid(column=3, row=8, sticky=E)

root.mainloop()

