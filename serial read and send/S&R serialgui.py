from tkinter import *
from tkinter import ttk
import serial  # pip install pyserial
import requests  # pip install requests


# =========================================================================
#
# =========================================================================


def startstoptab1():
    url = "https://groker.init.st/api/events?accessKey=" + str(access_key.get()) + "&bucketKey=" + str(
        bucket_key.get())  # full url getting general url add variable access_key variable and bucket_key variable

    ser = serial.Serial(
        port=str(port.get()), baudrate=9600, parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

    val = 0  # sets val to 0 on start
    print("connected to: " + ser.portstr)
    #  print(x.get())

    if x.get() == "1":
        x.set(0)
        while True:
            val = ser.readline()  # reads serial line
            print(type(val))
            if len(val) >= 1:  # bug if the val is less than 1 it wont send is needed to cut b'' form the results

                name_cutoff_s = 2
                name_cutoff_e = len(str(name_length.get())) - len(str(val))
                data_cutoff_s = len(str(val)) - (len(str(val)) - len(str(name_length.get())))
                data_cutoff_e = (len(str(name_length.get())) + len(str(data_length.get()))) - len(str(val))

                post_name = (str(val)[int(name_cutoff_s):int(name_cutoff_e)])  # -31=4 char for the if you have a longer name make it bigger also
                variable = (str(val)[int(data_cutoff_s):int(data_cutoff_e)])  # removes 12 char from the start and 15 from the end
                post_url = "{}&{}={}".format(url, post_name, variable)  # formatting the url - compiles the url, post name and variable into one line , & is for string = for int

                print(post_url)  # print to console
                print("no send")
        ser.close()


    else:
        x.set(1)
        while True:
            val = ser.readline()  # reads serial line
            print(type(val))
            if len(val) >= 1:  # bug if the val is less than 1 it wont send is needed to cut b'' form the results

                name_cutoff_s = 2
                name_cutoff_e = len(str(name_length.get())) - len(str(val))
                data_cutoff_s = len(str(val)) - (len(str(val)) - len(str(name_length.get())))
                data_cutoff_e = (len(str(name_length.get())) + len(str(data_length.get()))) - len(str(val))

                post_name = (str(val)[int(name_cutoff_s):int(
                    name_cutoff_e)])  # -31=4 char for the if you have a longer name make it bigger also
                variable = (
                str(val)[int(data_cutoff_s):int(data_cutoff_e)])  # removes 12 char from the start and 15 from the end
                post_url = "{}&{}={}".format(url, post_name,
                                             variable)  # formatting the url - compiles the url, post name and variable into one line , & is for string = for int

                print(post_url)  # print to console
                requests.post(post_url)  # request is the name of a repository and post is the command to post it to the website
                ser.close()


def tab1_save():
    name_cutoff_s = "ab"
    val = "abkillme1234"
    data_cutoff_e = (len(str(name_cutoff_s)) + len(str(name_length.get())) + len(str(data_length.get()))) - len(str(val))
    print("yes")
    print(data_cutoff_e)
    #  3 = 12 - (2+4+3)
    


def save_tab2():
    #val = "43wantdie123"
    access_key.set(tab2_access_key.get())
    bucket_key.set(tab2_bucket_key.get())
    name_length.set(tab2_name_length.get())
    data_length.set(tab2_data_length.get())

    #name_cutoff_s = len(str("ab"))
    #print(name_cutoff_s)
    #name_cutoff_e = len(str(name_length.get())) - len(str(val))
    # print(name_cutoff)
    #data_cutoff_s = len(str(val)) - (len(str(val)) - len(str(name_length.get())))

    #data_cutoff_e = (len(str(name_cutoff_s)) + len(str(name_length.get())) + len(str(data_length.get()))) - len(str(val))

    #post_name = (str(val)[int(str(name_cutoff_s)):int(name_cutoff_e)])

    #variable = (str(val)[int(data_cutoff_s):int(data_cutoff_e)])


    #print("name cutoff s")
    #print(name_cutoff_s)
    #print("name cutoff e")
    #print(name_cutoff_e)
    #print("data cutoff s")
    #print(data_cutoff_s)
    #print("data_cutoff_e")
    #print(data_cutoff_e)
    #print("post name")
    #print(post_name)
    #print("post var")
    #print(variable)

    name_cutoff_s = "ab"
    val = "abkillme1234"
    data_cutoff_e = (len(str(name_cutoff_s)) + len(str(name_length.get())) + len(str(data_length.get()))) - len(
        str(val))
    print("data c e")
    print(data_cutoff_e)
    #  3 = 12 - (2+4+3)

    name_cutoff_e = (len(str(name_cutoff_s)) + len(str(name_length.get()))) - len(str(val))
    print("name c e")
    print(name_cutoff_e)
    # 12 - 2+4


    data_cutoff_s = len(str(name_length.get())) + len(str(name_cutoff_s))
    print("data c s")
    print(data_cutoff_s)

    post_name = (str(val)[int(str(name_cutoff_s)):int(str(name_cutoff_e))])
    print("post name")
    print(post_name)

    variable = (str(val)[int(data_cutoff_s):int(str(data_cutoff_e))])
    print("post var")
    print(variable)



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

# =========================================================================
# With Tkinter we need to to update values on the screen we need to use
# a StingVar() we assign these here and then use these with the textvariable
# in "Entry" widgets
# =========================================================================
x = StringVar()
bucket_key = StringVar()
access_key = StringVar()
port = StringVar()
name_length = StringVar()
data_length = StringVar()
# =========================================================================
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='data')

tab1_start_stop = StringVar()
ttk.Button(tab1, text="start/stop", command=startstoptab1).grid(column=1, row=1, sticky=E)

tab1_save = StringVar()
ttk.Button(tab1, text="save", command=tab1_save).grid(column=1, row=2, sticky=E)

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

root.mainloop()
