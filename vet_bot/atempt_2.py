from tkinter import *
from tkinter import ttk
from threading import *
from time import sleep, perf_counter
import serial  # pip install pyserial

# ===================================================================
# bevan matsacos
# date 01/06/21
#
#
# threading control start stops kinda scuffed so you gotta start them with an if that's controlled by a button or
# forever loop to lazy to find a better solution atm
# ===================================================================

# threading delays
delay_start = 0.5  # default 1
print(delay_start)
delay_run = .01  # default .01
print(delay_run)
delay_space = delay_run / 2  # delay_run / 2
print(delay_space)

ser = serial.Serial(port='COM10', baudrate=9600, timeout=.1)


def run_read(read):  # the run_last_ten function just calls the read function every 100ms
    read()
    root.after(100, run_read, read)


def read():
    val = ser.readline()  # reads serial line
    val = (str(val)[2:-1])
    if len(val) < 3:
        return
    else:
        print(str(val))


def stop(event):
    on_off.set(0)


def set(event):
    stop()
    y_pos.set(0)
    z_pos.set(0)
    on_off.set(1)


def Forward(event):
    if int(on_off.get()) == 1:
        for v in range(int(scale.get())):
            if int(y_pos.get()) < 500:
                i = int(y_pos.get()) + 1
                if i <= 500:
                    y_pos.set(i)
                    x = "1"
                    ser.write(bytes(x, 'utf-8'))  # reads serial line
                    sleep(.05)


def Back(event):
    if int(on_off.get()) == 1:
        for v in range(int(scale.get())):
            if int(y_pos.get()) > 0:
                i = int(y_pos.get()) - 1
                if i >= 0:
                    y_pos.set(i)
                    x = "2"
                    ser.write(bytes(x, 'utf-8'))  # reads serial line
                    sleep(.05)


def Up(event):
    if int(on_off.get()) == 1:
        for v in range(int(scale.get())):
            if int(z_pos.get()) < 500:
                i = int(z_pos.get()) + 1
                if i <= 500:
                    z_pos.set(i)
                    x = "3"
                    ser.write(bytes(x, 'utf-8'))  # reads serial line
                    sleep(.05)


def Down(event):
    if int(on_off.get()) == 1:
        for v in range(int(scale.get())):
            if int(z_pos.get()) > 0:
                i = int(z_pos.get()) - 1
                if i >= 0:
                    z_pos.set(i)
                    x = "4"
                    ser.write(bytes(x, 'utf-8'))
                    sleep(.05)


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
    print(scale.get())


# =========================================================================
#
# =========================================================================
root = Tk()
root.title("Serial")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# =========================================================================
#
# =========================================================================
on_off = StringVar()
on_off.set(1)
x_pos = StringVar()
x_pos.set(0)
y_pos = StringVar()
y_pos.set(50)
z_pos = StringVar()
z_pos.set(50)
scale = StringVar()
scale.set(5)

# ====================================================================

toggle_button = ttk.Button(mainframe, text="Set")  #
toggle_button.grid(column=3, row=1, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", set)

# Edward edited this bit
toggle_button = ttk.Button(mainframe, text="Forward")  #
toggle_button.grid(column=2, row=1, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", Forward)

toggle_button = ttk.Button(mainframe, text="Stop")  #
toggle_button.grid(column=3, row=2, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", stop)

toggle_button = ttk.Button(mainframe, text="Back")  #
toggle_button.grid(column=2, row=2, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", Back)

toggle_button = ttk.Button(mainframe, text="Up")  #
toggle_button.grid(column=1, row=1, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", Up)

toggle_button = ttk.Button(mainframe, text="Scale")  #
toggle_button.grid(column=3, row=3, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", scale_set)

toggle_button = ttk.Button(mainframe, text="Down")  #
toggle_button.grid(column=1, row=2, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", Down)

# ====================================================================
ttk.Label(mainframe, text="y=").grid(column=4, padx=2, pady=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=y_pos).grid(column=5, row=1, padx=2, pady=2, columnspan=1, sticky=(W, E))

ttk.Label(mainframe, text="z=").grid(column=4, padx=2, pady=2, row=2, sticky=(W, E))
ttk.Label(mainframe, textvariable=z_pos).grid(column=5, row=2, padx=2, pady=2, columnspan=1, sticky=(W, E))

ttk.Label(mainframe, text="scale=").grid(column=4, padx=2, pady=2, row=3, sticky=(W, E))
ttk.Label(mainframe, textvariable=scale).grid(column=5, row=3, padx=2, pady=2, columnspan=1, sticky=(W, E))

# ====================================================================

run_read(read)

root.mainloop()
