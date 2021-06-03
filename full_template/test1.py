from tkinter import *
from tkinter import ttk
from threading import *
from time import sleep, perf_counter

# ===================================================================
# bevan matsacos
# date 01/06/21
#
#
# threading control start stops kinda scuffed so you gotta start them with an if that's controlled by a button or
# forever loop to lazy to find a better solution atm
# ===================================================================

# threading delays
delay_start = 1  # default 1
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
    t2 = Thread(target=thread_b)
    t1.start()
    sleep(delay_space)
    t2.start()


def thread_a():  # first thread function
    print("a waiting")  # tells the threading is running
    sleep(delay_start)  # delays the start so that it no die
    a = 0  # creates variable to count
    while thread_start.get() == str(1):  # infinite loop
        sleep(delay_run)  # timing delay
        log = "loop a" + " " + str(a)  # adds strings to the a num
        log_list_a.set(log)  # set log_list_a to log
        a = a + 1  # adds one to a each loop


def thread_b():
    print("b waiting")
    sleep(delay_start)
    b = 0
    while thread_start.get() == str(1):
        sleep(delay_run)
        log = "loop b" + " " + str(b)
        log_list_b.set(log)
        b = b + 1


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
# Edward edited this bit
toggle_button = ttk.Button(mainframe, text="on/off")
toggle_button.grid(column=1, row=1, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", start_threading)

ttk.Label(mainframe, textvariable=on_off).grid(column=2, row=1, padx=2, pady=2, columnspan=1, sticky=(W, E))

log_list_a = StringVar()
ttk.Label(mainframe, textvariable=log_list_a).grid(column=1, row=2, sticky=(W, E))

log_list_b = StringVar()
ttk.Label(mainframe, textvariable=log_list_b).grid(column=2, row=2, sticky=(W, E))

root.mainloop()
