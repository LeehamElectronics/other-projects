from tkinter import *
from tkinter import ttk
from threading import *
from time import sleep, perf_counter
import serial  # pip install pyserial

# ===================================================================
# bevan matsacos
# date 08/06/21
#
#
# ===================================================================

# threading delays this is just what i use to keep the code stable def could be less
delay_start = 1  # default 1
# print(delay_start)
delay_run = .005  # default .01
# print(delay_run)
delay_space = delay_run / 2  # delay_run / 2
# print(delay_space)

# timing code  # use this if you want to see how long it takes your code to do something
# start_time = perf_counter()  # starts timer
# end_time = perf_counter()  # ends timer
# print({end_time - start_time})  # figures out how long it tool

ser = serial.Serial(port='COM4', baudrate=9600, timeout=.1)  # if you want to test the output without device use HHD
# virtual serial port tools and run ser_read.py along side this one it'll read whats being forwarded to the other port

# =========================================================================


def start_threading(event):  # toggle threading on or off
    if str(thread_start.get()) == "1":  # if thread_start = 1 set it to 0
        thread_start.set(0)
        on_off.set("no")  # set label to no
    else:  # if its  0 then set it to 1
        thread_start.set(1)
        on_off.set("yes")  # set label to yes
    threading()  # runs threading


def threading():
    t1 = Thread(target=thread_a)
    t2 = Thread(target=thread_b)
    t3 = Thread(target=thread_c)
    t4 = Thread(target=thread_d)
    t1.start()
    sleep(delay_space)
    t2.start()
    sleep(delay_space)
    t3.start()
    sleep(delay_space)
    t4.start()
    sleep(delay_space)


def a_button(event):
    if int(a_run.get()) == 0:
        a_run.set(int(scale.get()))
    # print(a_run.get())


def thread_a():  # first thread function
    sleep(delay_start)
    range_end = 100000
    range_start = -100000
    while thread_start.get() == str(1):
        for v in range(int(a_run.get())):
            if int(range_start) <= int(y_pos.get()) <= int(range_end):
                # print(y_pos.get())
                # print("a test")
                sleep(delay_space)
                i = int(y_pos.get()) + 1
                y_pos.set(i)
                x = "1"
                ser.write(bytes(x, 'utf-8'))
                sleep(.01)
        a_run.set(0)


def b_button(event):
    if int(b_run.get()) == 0:
        b_run.set(int(scale.get()))
    # print(b_run.get())


def thread_b():
    sleep(delay_start)
    range_end = 100000
    range_start = -100000
    while thread_start.get() == str(1):
        for v in range(int(b_run.get())):
            if int(range_start) <= int(y_pos.get()) <= int(range_end):
                # print(y_pos.get())
                # print("b test")
                sleep(delay_space)
                i = int(y_pos.get()) - 1
                y_pos.set(i)
                x = "2"
                ser.write(bytes(x, 'utf-8'))
                sleep(.01)
        b_run.set(0)


def c_button(event):
    if int(c_run.get()) == 0:
        c_run.set(int(scale.get()))
    # print(c_run.get())


def thread_c():
    sleep(delay_start)
    range_end = 100000
    range_start = -100000
    while thread_start.get() == str(1):
        for v in range(int(c_run.get())):
            if int(range_start) <= int(z_pos.get()) <= int(range_end):
                # print(z_pos.get())
                # print("c test")
                sleep(delay_space)
                i = int(z_pos.get()) + 1
                z_pos.set(i)
                x = "3"
                ser.write(bytes(x, 'utf-8'))
        c_run.set(0)


def d_button(event):
    if int(d_run.get()) == 0:
        d_run.set(int(scale.get()))
    # print(d_run.get())


def thread_d():
    sleep(delay_start)
    range_end = 100000
    range_start = -100000
    while thread_start.get() == str(1):
        for v in range(int(d_run.get())):
            if int(range_start) <= int(z_pos.get()) <= int(range_end):
                # print(z_pos.get())
                # print("d test")
                sleep(delay_space)
                i = int(z_pos.get()) - 1
                z_pos.set(i)
                x = "4"
                ser.write(bytes(x, 'utf-8'))
        d_run.set(0)


def set(event):
    z_pos.set(0)
    y_pos.set(0)


def scale_set(event):
    if int(scale.get()) == 100:
        scale.set(5)
        return
    if int(scale.get()) == 50:
        scale.set(100)
        return
    if int(scale.get()) == 10:
        scale.set(50)
        return
    if int(scale.get()) == 5:
        scale.set(10)
        return
    # print(scale.get())


# =========================================================================

root = Tk()
root.title("Serial_control")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# =========================================================================
y_pos = StringVar()
y_pos.set(0)
z_pos = StringVar()
z_pos.set(0)
a_run = StringVar()
a_run.set(0)
b_run = StringVar()
b_run.set(0)
c_run = StringVar()
c_run.set(0)
d_run = StringVar()
d_run.set(0)
scale = StringVar()
scale.set(5)

thread_start = StringVar()

on_off = StringVar()

# =========================================================================

toggle_button = ttk.Button(mainframe, text="forward")  #
toggle_button.grid(column=1, row=1, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", a_button)

toggle_button = ttk.Button(mainframe, text="backward")
toggle_button.grid(column=1, row=2, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", b_button)

toggle_button = ttk.Button(mainframe, text="up")
toggle_button.grid(column=2, row=1, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", c_button)

toggle_button = ttk.Button(mainframe, text="down")
toggle_button.grid(column=2, row=2, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", d_button)

toggle_button = ttk.Button(mainframe, text="on/off")  #
toggle_button.grid(column=3, row=1, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", start_threading)

toggle_button = ttk.Button(mainframe, text="set")  #
toggle_button.grid(column=3, row=2, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", set)

toggle_button = ttk.Button(mainframe, text="scale")  #
toggle_button.grid(column=3, row=3, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", scale_set)

# =========================================================================

ttk.Label(mainframe, text="y=").grid(column=4, padx=2, pady=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=y_pos).grid(column=5, row=1, padx=2, pady=2, columnspan=1, sticky=(W, E))

ttk.Label(mainframe, text="z=").grid(column=4, padx=2, pady=2, row=2, sticky=(W, E))
ttk.Label(mainframe, textvariable=z_pos).grid(column=5, row=2, padx=2, pady=2, columnspan=1, sticky=(W, E))

ttk.Label(mainframe, text="scale=").grid(column=4, padx=2, pady=2, row=3, sticky=(W, E))
ttk.Label(mainframe, textvariable=scale).grid(column=5, row=3, padx=2, pady=2, columnspan=1, sticky=(W, E))

root.mainloop()
