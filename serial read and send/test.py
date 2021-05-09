from tkinter import *
from tkinter import ttk
import serial
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# =========================================================================
# serial gui code by Bevan Matsacos
# start date 2/5/2021
# last edit 8/5/2021
#
# purpose is to simplify the use of the serial to inital state code i made
# prior that would read the serial output form a iot device cut and send
# the data to the site to be looked at
#
# to do
#
# try remove the need for log10.txt
# neaten and comment the code
#
# =========================================================================

wait = 100


def run_main(main):  # the run_main function just calls the main function every 100ms
    main()
    root.after(wait, run_main, main)


def main():
    if z.get() == "1":
        url = "https://groker.init.st/api/events?accessKey=" + str(access_key.get()) + "&bucketKey=" + str(
            bucket_key.get())  # full url getting general url add variable access_key variable and bucket_key variable

        ser = serial.Serial(
            port=str(port.get()), baudrate=9600,
            parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS, timeout=1)

        val = 0  # sets val to 0 on start
        print("connected to: " + ser.portstr)

        while True:
            val = ser.readline()  # reads serial line
            print(type(val))
            if len(val) >= 1:  # bug if the val is less than 1 it wont send is needed to cut b'' form the results

                name_cutoff_s = str("ab")
                name_cutoff_e = (len(str(name_cutoff_s)) + len(str(name_length.get()))) - len(str(val))

                data_cutoff_s = len(str(name_length.get())) + len(str(name_cutoff_s))
                data_cutoff_e = (len(str(name_cutoff_s)) + len(str(name_length.get())) + len(
                    str(data_length.get()))) - len(str(val))

                post_name = (str(val)[2:int(str(name_cutoff_e))])
                variable = (str(val)[int(str(data_cutoff_s)):int(str(data_cutoff_e))])

                post_url = "{}&{}={}".format(url, post_name, variable)  # formatting the url

                print(post_url)  # print to console

                if x.get() == "1":
                    requests.post(post_url)
                else:
                    pass
                ser.close()


# def run_read(read):  # the run_read function just calls the read function every 100ms
#    read()
#    root.after(wait, run_read, read)


# def read():
#    f = open("log10.txt", "r")  # opens log10.txt in read mode
#    log_list.set(f.read())  # sets log_list to the contents of log10.txt


def startstoptab1():  # toggle the main code running. loop always runs just not active
    if z.get() == "1":
        z.set(0)
        start_tab1.set("no")
    else:
        z.set(1)
        start_tab1.set("yes")


def onlinetab1():  # toggle online or offline
    if x.get() == "1":
        x.set(0)
        online_tab1.set("no")
    else:
        x.set(1)
        online_tab1.set("yes")


def save_tab1():
    f = open("log.txt", "r")  # opens log.txt in read
    g = open("exported.txt", "w")  # opens exported.txt in write
    g.write(f.read())  # copy's the contents of log.txt to exported.txt
    print("saved")
    f.close()
    g.close()


def clear_tab1():
    f = open("log.txt", "w")
    f.write("")
    f.close()


def save_tab2():
    access_key.set(tab2_access_key.get())  # sets the user input to the running
    bucket_key.set(tab2_bucket_key.get())
    port.set(tab2_port.get())
    name_length.set(tab2_name_length.get())
    data_length.set(tab2_data_length.get())


def run_last_ten(last_ten):  # the run_last_ten function just calls the read function every 100ms
    last_ten()
    root.after(wait, run_last_ten, last_ten)


def last_ten(file, number_of_lines):
    log_list.set("")
    f = open(file, "r")
    lines = []
    num_lines = sum(1 for line in open('log.txt'))
    for position, line in enumerate(f):
        for i in range(num_lines - number_of_lines, num_lines):
            if position == i:
                print(line, end='')
                log_list.set(lines)
                lines.append(line)
    return lines


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == "./log.txt":
            last_ten('log.txt', 10)  # file and amount of lines to read


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='./', recursive=False)
observer.start()

# =========================================================================

root = Tk()
root.title("serial gui")
tabControl = ttk.Notebook(root)
tabControl.pack(expand=1, fill="both")

# =========================================================================

online_tab1 = StringVar()
start_tab1 = StringVar()
x = StringVar()
z = StringVar()
bucket_key = StringVar()
access_key = StringVar()
port = StringVar()
name_length = StringVar()
data_length = StringVar()
log_list = StringVar()

# =========================================================================

run_main(main)
# run_read(read)

# =========================================================================

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='data')

ttk.Button(tab1, text="on/offline", command=onlinetab1).grid(column=1, row=1, padx=2, pady=2, sticky=(W, E))
ttk.Label(tab1, textvariable=online_tab1).grid(column=2, row=1, padx=2, pady=2, columnspan=1, sticky=(W, E))

ttk.Button(tab1, text="start/stop", command=startstoptab1).grid(column=1, row=2, padx=2, pady=2, sticky=(W, E))
ttk.Label(tab1, textvariable=start_tab1).grid(column=2, row=2, padx=2, pady=2, columnspan=1, sticky=(W, E))

ttk.Button(tab1, text="save", command=save_tab1).grid(column=1, row=3, padx=2, pady=2, sticky=(W, E))

ttk.Button(tab1, text="clear", command=clear_tab1).grid(column=1, row=4, padx=2, pady=2, sticky=(W, E))

ttk.Label(tab1, textvariable=log_list).grid(column=1, row=5, padx=2, pady=2, columnspan=3, sticky=(W, E))

# =========================================================================

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='setup')

tab2_access_key = StringVar()
txt_tab2_access_key = ttk.Entry(tab2, textvariable=tab2_access_key)
txt_tab2_access_key.grid(column=2, row=1, padx=2, pady=2, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="access key").grid(column=1, padx=2, pady=2, row=1, sticky=(W, E))

tab2_bucket_key = StringVar()
txt_tab2_bucket_key = ttk.Entry(tab2, textvariable=tab2_bucket_key)
txt_tab2_bucket_key.grid(column=2, row=2, padx=2, pady=2, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="bucket key").grid(column=1, row=2, padx=2, pady=2, sticky=(W, E))

tab2_port = StringVar()
txt_tab2_port = ttk.Entry(tab2, textvariable=tab2_port)
txt_tab2_port.grid(column=2, row=3, padx=2, pady=2, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="port").grid(column=1, row=3, padx=2, pady=2, sticky=(W, E))

tab2_name_length = StringVar()
txt_tab2_name_length = ttk.Entry(tab2, textvariable=tab2_name_length)
txt_tab2_name_length.grid(column=2, row=4, padx=2, pady=2, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="name length").grid(column=1, row=4, padx=2, pady=2, sticky=(W, E))

tab2_data_length = StringVar()
txt_tab2_data_length = ttk.Entry(tab2, textvariable=tab2_data_length)
txt_tab2_data_length.grid(column=2, row=5, padx=2, pady=2, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="data length").grid(column=1, row=5, sticky=(W, E))

ttk.Button(tab2, text="save", command=save_tab2).grid(column=2, row=6, padx=2, pady=2, sticky=(W, E))

ttk.Label(tab2, textvariable=start_tab1).grid(column=2, row=7, padx=2, pady=2, columnspan=1, sticky=(W, E))
ttk.Label(tab2, textvariable=start_tab1).grid(column=2, row=8, padx=2, pady=2, columnspan=1, sticky=(W, E))
ttk.Label(tab2, textvariable=start_tab1).grid(column=2, row=9, padx=2, pady=2, columnspan=1, sticky=(W, E))
ttk.Label(tab2, textvariable=start_tab1).grid(column=2, row=10, padx=2, pady=2, columnspan=1, sticky=(W, E))
ttk.Label(tab2, textvariable=start_tab1).grid(column=2, row=11, padx=2, pady=2, columnspan=1, sticky=(W, E))
ttk.Label(tab2, textvariable=start_tab1).grid(column=2, row=12, columnspan=1, sticky=(W, E))

root.mainloop()