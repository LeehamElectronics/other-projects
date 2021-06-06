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

test_mode = 1

if test_mode == 0:
    ser = serial.Serial(port='COM2',  # set to com on windows or tty on py
                        baudrate=9600,  # is the bit rate of the bored the default is 9600
                        parity=serial.PARITY_NONE,  # no idea
                        stopbits=serial.STOPBITS_ONE,  # no idea
                        bytesize=serial.EIGHTBITS,  # 8 bit
                        timeout=1)  # also no idea
else:
    ser = 0



def test(event):
    pass


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
            if int(y_pos.get()) > 0:
                i = int(y_pos.get()) + 1
                if i >= 0:
                    y_pos.set(i)
                    val = "+t\n".encode('utf-8')
                    # ser.write(val)  # reads serial line
                    print(val)
                    sleep(.05)




def Back(event):
    if int(on_off.get()) == 1:
        for v in range(int(scale.get())):
            if int(y_pos.get()) > 0:
                i = int(y_pos.get()) - 1
                if i >= 0:
                    y_pos.set(i)
                    val = "-y\n".encode('utf-8')
                    # ser.write(val)  # reads serial line
                    print(val)
                    sleep(.05)



def Up(event):
    if int(on_off.get()) == 1:
        for v in range(int(scale.get())):
            if int(z_pos.get()) < 500:
                i = int(z_pos.get()) + 1
                if i <= 500:
                    z_pos.set(i)
                    val = "+z\n".encode('utf-8')
                    # ser.write(val)  # reads serial line
                    print(val)
                    sleep(.05)



def Down(event):
    if int(on_off.get()) == 1:
        for v in range(int(scale.get())):
            if int(z_pos.get()) > 0:
                i = int(z_pos.get()) - 1
                if i >= 0:
                    z_pos.set(i)
                    val = "-z\n".encode('utf-8')
                    # ser.write(val)  # reads serial line
                    print(val)
                    sleep(.05)





def scale_set(event):
    if int(scale.get()) == 100:
        scale.set(1)
    if int(scale.get()) == 50:
        scale.set(100)
    if int(scale.get()) == 10:
        scale.set(50)
    if int(scale.get()) == 5:
        scale.set(10)
    if int(scale.get()) == 1:
        scale.set(5)
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

toggle_button = ttk.Button(mainframe, text="Set")
toggle_button.grid(column=1, row=1, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", test)

# Edward edited this bit
toggle_button = ttk.Button(mainframe, text="Forward")
toggle_button.grid(column=2, row=1, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", Forward)

toggle_button = ttk.Button(mainframe, text="Stop")
toggle_button.grid(column=3, row=1, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", test)

toggle_button = ttk.Button(mainframe, text="Back")
toggle_button.grid(column=2, row=3, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", Back)

toggle_button = ttk.Button(mainframe, text="Up")
toggle_button.grid(column=4, row=1, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", Up)

toggle_button = ttk.Button(mainframe, text="Scale")
toggle_button.grid(column=4, row=2, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", scale_set)

toggle_button = ttk.Button(mainframe, text="Down")
toggle_button.grid(column=4, row=3, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", Down)

# ====================================================================
ttk.Label(mainframe, text="x=").grid(column=5, padx=2, pady=2, row=1, sticky=(W, E))
ttk.Label(mainframe, textvariable=x_pos).grid(column=6, row=1, padx=2, pady=2, columnspan=1, sticky=(W, E))

ttk.Label(mainframe, text="y=").grid(column=5, padx=2, pady=2, row=2, sticky=(W, E))
ttk.Label(mainframe, textvariable=y_pos).grid(column=6, row=2, padx=2, pady=2, columnspan=1, sticky=(W, E))

ttk.Label(mainframe, text="z=").grid(column=5, padx=2, pady=2, row=3, sticky=(W, E))
ttk.Label(mainframe, textvariable=z_pos).grid(column=6, row=3, padx=2, pady=2, columnspan=1, sticky=(W, E))

ttk.Label(mainframe, text="scale=").grid(column=5, padx=2, pady=2, row=4, sticky=(W, E))
ttk.Label(mainframe, textvariable=scale).grid(column=7, row=4, padx=2, pady=2, columnspan=1, sticky=(W, E))

# ====================================================================

ttk.Label(mainframe, textvariable=on_off).grid(column=3, row=5, padx=2, pady=2, columnspan=1, sticky=(W, E))

log_list_a = StringVar()
ttk.Label(mainframe, textvariable=log_list_a).grid(column=1, row=5, sticky=(W, E))

log_list_b = StringVar()
ttk.Label(mainframe, textvariable=log_list_b).grid(column=2, row=5, sticky=(W, E))

root.mainloop()
