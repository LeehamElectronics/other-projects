from tkinter import *
from tkinter import ttk
from threading import *
from time import sleep, perf_counter

# ===================================================================
# bevan matsacos
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
#thread_start = 1

# timing code
# start_time = perf_counter()
# end_time = perf_counter()
# print({end_time - start_time})


def test():
    v = 0
    while v == 0:
        print(1)
        sleep(2)

#Edward edited your fuction so it expects an event ("<Button-1>")
def start_threading(event):  # toggle threading on or off
    if str(thread_start.get()) == "1":
        thread_start.set(0)
        on_off.set("no")
    else:
        thread_start.set(1)
        on_off.set("yes")
    threading()


def thread_a():
    print("a waiting")
    sleep(delay_start)
    a = 0
    while thread_start.get() == str(1):
        sleep(delay_run)
        log = "loop a" + " " + str(a)
        log_list_a.set(log)
        a = a + 1


def thread_b():
    print("b waiting")
    sleep(delay_start)
    b = 0
    while thread_start.get() == str(1):
        sleep(delay_run)
        log = "loop b" + " " + str(b)
        log_list_b.set(log)
        b = b + 1


def threading():
    t1 = Thread(target=thread_a)
    t2 = Thread(target=thread_b)
    t1.start()
    sleep(delay_space)
    t2.start()


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
#Edward edited this bit
toggle_button = ttk.Button(mainframe, text="on/off")
toggle_button.grid(column=1, row=1, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>",start_threading)

ttk.Label(mainframe, textvariable=on_off).grid(column=2, row=1, padx=2, pady=2, columnspan=1, sticky=(W, E))


log_list_a = StringVar()
ttk.Label(mainframe, textvariable=log_list_a).grid(column=1, row=2, sticky=(W, E))

log_list_b = StringVar()
ttk.Label(mainframe, textvariable=log_list_b).grid(column=2, row=2, sticky=(W, E))


root.mainloop()