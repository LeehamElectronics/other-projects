# =========================================================================
# Created by bevan matsacos
#
# =========================================================================
from tkinter import *
from tkinter import ttk
from threading import *
from time import sleep, perf_counter



# delay_start = 1  # default 1
# print(delay_start)
# delay_run = .01  # default .01
# print(delay_run)
# delay_space = delay_run / 2  # delay_run / 2
# print(delay_space)

def start_threading(event):  # toggle threading on or off
    delay_start.set(float(val_var_0.get()))
    delay_run.set(float(val_var_1.get()))
    delay_space.set(float(delay_run.get()) / 2)  # delay_run / 2

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
    sleep(float(delay_space.get()))
    t2.start()


def thread_a():  # first thread function
    sleep(float(delay_start.get()))  # delays the start so that it no die
    a = 0  # creates variable to count
    while thread_start.get() == str(1):  # infinite loop
        sleep(float(delay_run.get()))  # timing delay
        log = "loop a" + " " + str(a)  # adds strings to the a num
        log_list_a.set(log)  # set log_list_a to log
        a = a + 1  # adds one to a each loop


def thread_b():
    sleep(float(delay_start.get()))
    b = 0
    while thread_start.get() == str(1):
        sleep(float(delay_run.get()))
        log = "loop b" + " " + str(b)
        log_list_b.set(log)
        b = b + 1


# ======================================================================================================================
# tab 10:var/debug
# ======================================================================================================================

def read_tab_10(event):
    file = open("Python.txt")
    read_lines = file.readlines()

    import_var_0 = (read_lines[0])
    val_var_0.set(import_var_0[len(str(name_var_0.get())) + 1
                               :len(str(import_var_0)) - 2])  # - 2 from end

    import_var_1 = (read_lines[1])
    val_var_1.set(import_var_1[len(str(name_var_1.get())) + 1
                               :len(str(import_var_1)) - 2])
    file.close()


def save_tab_10(event):
    export_var_0 = str(name_var_0.get()) + val_var_0.get()
    export_var_1 = str(name_var_1.get()) + val_var_1.get()
    print(export_var_0)
    print(export_var_1)

    file = open("Python.txt", "w")  # opens python.txt in write mode
    file.write(repr(export_var_0) + "\n" +
               repr(export_var_1) + "\n")  # export var + new line writen to file
    file.close()


# ======================================================================================================================

root = Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)  # adds tabs to the tkinter
tabControl.pack(expand=1, fill="both")  # i dont know what this does i just know its needed

# ======================================================================================================================
# tab 1:main
# ======================================================================================================================
tab1 = ttk.Frame(tabControl)  # creates the tab 1
tabControl.add(tab1, text='main')  # gives tab 1 a tittle

thread_start = StringVar()
delay_start = StringVar()
delay_run = StringVar()
delay_space = StringVar()

on_off = StringVar()
# Edward edited this bit
toggle_button = ttk.Button(tab1, text="on/off")
toggle_button.grid(column=1, row=1, padx=2, pady=2, sticky=(W, E))
toggle_button.bind("<Button-1>", start_threading)

ttk.Label(tab1, textvariable=on_off).grid(column=2, row=1, padx=2, pady=2, columnspan=1, sticky=(W, E))

log_list_a = StringVar()
ttk.Label(tab1, textvariable=log_list_a).grid(column=1, row=2, sticky=(W, E))

log_list_b = StringVar()
ttk.Label(tab1, textvariable=log_list_b).grid(column=2, row=2, sticky=(W, E))

# ======================================================================================================================
# tab 10:var/debug
# ======================================================================================================================
tab10 = ttk.Frame(tabControl)
tabControl.add(tab10, text='debug')

import_var_0 = StringVar()
name_var_0 = StringVar()
val_var_0 = StringVar()
name_var_0.set("Start delay     = ")
txtTitle = ttk.Entry(tab10, textvariable=val_var_0)
txtTitle.grid(column=2, row=1, columnspan=4, sticky=(W, E))
ttk.Label(tab10, text=name_var_0.get()).grid(column=1, row=1, sticky=E)

import_var_1 = StringVar()
name_var_1 = StringVar()
val_var_1 = StringVar()
name_var_1.set("Runing delay = ")
txtTitle = ttk.Entry(tab10, textvariable=val_var_1)
txtTitle.grid(column=2, row=2, columnspan=4, sticky=(W, E))
ttk.Label(tab10, text=name_var_1.get()).grid(column=1, row=2, sticky=E)

toggle_button1 = ttk.Button(tab10, text="read")
toggle_button1.grid(column=1, row=8, padx=2, pady=2, sticky=(W, E))
toggle_button1.bind("<Button-1>", read_tab_10)

toggle_button1 = ttk.Button(tab10, text="save")
toggle_button1.grid(column=2, row=8, padx=2, pady=2, sticky=(W, E))
toggle_button1.bind("<Button-1>", save_tab_10)

root.mainloop()
