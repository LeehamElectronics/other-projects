from tkinter import *
from tkinter import ttk
import serial  # pip install pyserial
import requests  # pip install requests
import os

logs = []


# =========================================================================
#
# =========================================================================
def run():
    if z.get() == "1":
        url = "https://groker.init.st/api/events?accessKey=" + str(access_key.get()) + "&bucketKey=" + str(
            bucket_key.get())  # full url getting general url add variable access_key variable and bucket_key variable

        ser = serial.Serial(
            port=str(port.get()), baudrate=9600, parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

        val = 0  # sets val to 0 on start
        print("connected to: " + ser.portstr)
        #  print(x.get())

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

                post_url = "{}&{}={}".format(url, post_name,
                                             variable)  # formatting the url - compiles the url, post name and variable into one line , & is for string = for int

                print(post_url)  # print to console

                if x.get() == "1":
                    requests.post(
                        post_url)  # request is the name of a repository and post is the command to post it to the website
                else:
                    pass
                ser.close()



def read():
    number_of_lines = len(open('log.txt').readlines())
    print(number_of_lines)



def startstoptab1():
    print(x.get())
    if z.get() == "1":
        z.set(0)
        start_tab1.set("no")
    else:
        z.set(1)
        start_tab1.set("yes")


def onlinetab1():
    if x.get() == "1":
        x.set(0)
        online_tab1.set("no")
    else:
        x.set(1)
        online_tab1.set("yes")


def save_tab1():
    print("test")


def save_tab2():
    access_key.set(tab2_access_key.get())
    bucket_key.set(tab2_bucket_key.get())
    name_length.set(tab2_name_length.get())
    data_length.set(tab2_data_length.get())

    url = "https://groker.init.st/api/events?accessKey=" + str(access_key.get()) + "&bucketKey=" + str(
        bucket_key.get())  # full url getting general url add variable access_key variable and bucket_key variable

    val = "123456789012"

    name_cutoff_s = str("ab")
    name_cutoff_e = (len(str(name_cutoff_s)) + len(str(name_length.get()))) - len(str(val))

    data_cutoff_s = len(str(name_length.get())) + len(str(name_cutoff_s))
    data_cutoff_e = (len(str(name_cutoff_s)) + len(str(name_length.get())) + len(str(data_length.get()))) - len(
        str(val))

    post_name = (str(val)[2:int(str(name_cutoff_e))])
    variable = (str(val)[int(str(data_cutoff_s)):int(str(data_cutoff_e))])

    post_url = "{}&{}={}".format(url, post_name,
                                 variable)  # formatting the url - compiles the url, post name and variable into one line , & is for string = for int

    print(post_url)  # print to console


# =========================================================================
#
# =========================================================================

root = Tk()
root.title("serial gui")
tabControl = ttk.Notebook(root)
tabControl.pack(expand=1, fill="both")

# =========================================================================
#
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
# =========================================================================
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='data')

ttk.Button(tab1, text="online/offline", command=onlinetab1).grid(column=1, row=1, sticky=E)
ttk.Label(tab1, textvariable=online_tab1).grid(column=2, row=1, columnspan=1, sticky=W)

ttk.Button(tab1, text="start/stop", command=startstoptab1).grid(column=1, row=2, sticky=E)
ttk.Label(tab1, textvariable=start_tab1).grid(column=2, row=2, columnspan=1, sticky=W)

ttk.Button(tab1, text="save", command=save_tab1).grid(column=1, row=12, sticky=E)

# =========================================================================

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='setup')

tab2_access_key = StringVar()
txttab2_access_key = ttk.Entry(tab2, textvariable=tab2_access_key)
txttab2_access_key.grid(column=2, row=1, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="access key").grid(column=1, row=1, sticky=E)

tab2_bucket_key = StringVar()
txttab2_bucket_key = ttk.Entry(tab2, textvariable=tab2_bucket_key)
txttab2_bucket_key.grid(column=2, row=2, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="bucket key").grid(column=1, row=2, sticky=E)

tab2_port = StringVar()
txttab2_port = ttk.Entry(tab2, textvariable=tab2_port)
txttab2_port.grid(column=2, row=3, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="port").grid(column=1, row=3, sticky=E)

tab2_send_test = StringVar()
txttab2_send_test = ttk.Entry(tab2, textvariable=tab2_send_test)
txttab2_send_test.grid(column=2, row=4, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="send test").grid(column=1, row=4, sticky=E)

tab2_name_length = StringVar()
txttab2_name_length = ttk.Entry(tab2, textvariable=tab2_name_length)
txttab2_name_length.grid(column=2, row=5, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="name length").grid(column=1, row=5, sticky=E)

tab2_data_length = StringVar()
txttab2_data_length = ttk.Entry(tab2, textvariable=tab2_data_length)
txttab2_data_length.grid(column=2, row=6, columnspan=1, sticky=(W, E))
ttk.Label(tab2, text="data length").grid(column=1, row=6, sticky=E)

ttk.Button(tab2, text="save", command=save_tab2).grid(column=2, row=8, sticky=E)

run()

read()

root.mainloop()
