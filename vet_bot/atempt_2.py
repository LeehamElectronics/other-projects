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


# threading control start stops kinda scuffed so you gotta start them with an if that's controlled by a button or
# forever loop to lazy to find a better solution atm

# timing code  # use this if you want to see how long it takes your code to do something
# start_time = perf_counter()  # starts timer
# end_time = perf_counter()  # ends timer
# print({end_time - start_time})  # figures out how long it tool


# Edward edited your function so it expects an event ("<Button-1>")
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
    t1.start()
    sleep(delay_space)


def thread_a():  # first thread function
    print("a waiting")  # tells the threading is running
    sleep(delay_start)  # delays the start so that it no die
    a = 0  # creates variable to count
    while thread_start.get() == str(1):  # infinite loop
        sleep(delay_run)  # timing delay
        log = "loop a" + " " + str(a)  # adds strings to the a num
        log_list_a.set(log)  # set log_list_a to log
        a = a + 1  # adds one to a each loop


def Forward(event):
    # print("forward")
    i = int(y_pos.get())
    i = i + 1
    y_pos.set(i)
    ser = serial.Serial(port='COM2',  # set to com on windows or tty on py
                        baudrate=9600,  # is the bit rate of the bored the default is 9600
                        parity=serial.PARITY_NONE,  # no idea
                        stopbits=serial.STOPBITS_ONE,  # no idea
                        bytesize=serial.EIGHTBITS,  # 8 bit
                        timeout=1)  # also no idea

    #print("connected to: " + ser.portstr)

    val = "+y\n".encode('utf-8')
    ser.write(val)  # reads serial line
    print(val)
    sleep(0)


def Left(event):
    # print("forward")
    i = int(x_pos.get())
    i = i - 1
    x_pos.set(i)
    ser = serial.Serial(port='COM2',  # set to com on windows or tty on py
                        baudrate=9600,  # is the bit rate of the bored the default is 9600
                        parity=serial.PARITY_NONE,  # no idea
                        stopbits=serial.STOPBITS_ONE,  # no idea
                        bytesize=serial.EIGHTBITS,  # 8 bit
                        timeout=1)  # also no idea

    # print("connected to: " + ser.portstr)

    val = "-x\n".encode('utf-8')
    ser.write(val)  # reads serial line
    print(val)
    sleep(0)


def Right(event):
    # print("forward")
    i = int(x_pos.get())
    i = i + 1
    x_pos.set(i)
    ser = serial.Serial(port='COM2',  # set to com on windows or tty on py
                        baudrate=9600,  # is the bit rate of the bored the default is 9600
                        parity=serial.PARITY_NONE,  # no idea
                        stopbits=serial.STOPBITS_ONE,  # no idea
                        bytesize=serial.EIGHTBITS,  # 8 bit
                        timeout=1)  # also no idea

    # print("connected to: " + ser.portstr)

    val = "+x\n".encode('utf-8')
    ser.write(val)  # reads serial line
    print(val)
    sleep(0)


def Back(event):
    #print("back")
    i = int(y_pos.get())
    i = i - 1
    y_pos.set(i)
    ser = serial.Serial(port='COM2',  # set to com on windows or tty on py
                        baudrate=9600,  # is the bit rate of the bored the default is 9600
                        parity=serial.PARITY_NONE,  # no idea
                        stopbits=serial.STOPBITS_ONE,  # no idea
                        bytesize=serial.EIGHTBITS,  # 8 bit
                        timeout=1)  # also no idea

    #print("connected to: " + ser.portstr)

    val = "-y\n".encode('utf-8')
    ser.write(val)  # reads serial line
    print(val)
    sleep(0)

    # print(scale.get())
    # if str(scale.get()) == str("1"):
    #     print('test1')
    #     if str(x_pos) < "0":
    #         x_pos.set(0)
    #     else:
    #         i = int(x_pos.get())
    #         i = i - 1
    #         print(i)
    #         if int(x_pos.get()) >= 0:  # greater than or equal
    #             ser = serial.Serial(
    #                 port='COM2',  # set to com on windows or tty on py
    #                 baudrate=9600,  # is the bit rate of the bored the default is 9600
    #                 parity=serial.PARITY_NONE,  # no idea
    #                 stopbits=serial.STOPBITS_ONE,  # no idea
    #                 bytesize=serial.EIGHTBITS,  # 8 bit
    #                 timeout=1)  # also no idea
    #
    #             print("connected to: " + ser.portstr)
    #
    #             val = "-x\n".encode('utf-8')
    #             ser.write(val)  # reads serial line
    #             print(val)
    #             sleep(0)
    #
    #             x_pos.set(i)
    #         else:
    #             x_pos.set(0)
    #
    # if scale.get() == 10:
    #     pass
    # if scale.get() == 100:
    #     pass
    # else:
    #     print('cum')


def Up(event):
    # print("forward")
    i = int(z_pos.get())
    i = i + 1
    z_pos.set(i)
    ser = serial.Serial(port='COM2',  # set to com on windows or tty on py
                        baudrate=9600,  # is the bit rate of the bored the default is 9600
                        parity=serial.PARITY_NONE,  # no idea
                        stopbits=serial.STOPBITS_ONE,  # no idea
                        bytesize=serial.EIGHTBITS,  # 8 bit
                        timeout=1)  # also no idea

    # print("connected to: " + ser.portstr)

    val = "+z\n".encode('utf-8')
    ser.write(val)  # reads serial line
    print(val)
    sleep(0)


def Scale(event):
    pass


def Down(event):
    # print("forward")
    i = int(z_pos.get())
    i = i - 1
    z_pos.set(i)
    ser = serial.Serial(port='COM2',  # set to com on windows or tty on py
                        baudrate=9600,  # is the bit rate of the bored the default is 9600
                        parity=serial.PARITY_NONE,  # no idea
                        stopbits=serial.STOPBITS_ONE,  # no idea
                        bytesize=serial.EIGHTBITS,  # 8 bit
                        timeout=1)  # also no idea

    # print("connected to: " + ser.portstr)

    val = "-z\n".encode('utf-8')
    ser.write(val)  # reads serial line
    print(val)
    sleep(0)


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
thread_start = StringVar()

on_off = StringVar()
x_pos = StringVar()
x_pos.set(0)
y_pos = StringVar()
y_pos.set(0)
z_pos = StringVar()
z_pos.set(0)
scale = StringVar()
scale.set(1)


toggle_button = ttk.Button(mainframe, text="Start")
toggle_button.grid(column=1, row=1, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", start_threading)

# Edward edited this bit
toggle_button = ttk.Button(mainframe, text="Forward")
toggle_button.grid(column=2, row=1, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", Forward)

toggle_button = ttk.Button(mainframe, text="Stop")
toggle_button.grid(column=3, row=1, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", start_threading)

toggle_button = ttk.Button(mainframe, text="Left")
toggle_button.grid(column=1, row=2, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", Left)

toggle_button = ttk.Button(mainframe, text="Right")
toggle_button.grid(column=3, row=2, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", Right)

toggle_button = ttk.Button(mainframe, text="Back")
toggle_button.grid(column=2, row=3, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", Back)


toggle_button = ttk.Button(mainframe, text="Up")
toggle_button.grid(column=4, row=1, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", Up)

toggle_button = ttk.Button(mainframe, text="Scale")
toggle_button.grid(column=4, row=2, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", start_threading)

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
