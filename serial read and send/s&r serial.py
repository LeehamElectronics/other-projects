# ======================================================================================================================
# made by Bevan Matsacos
#
# ======================================================================================================================

import serial  # pip install pyserial
import requests  # pip install requests

access_key = "ist_WNCOhg0VQNzA4AQT9NqLLQ-UXPTwe5pF"  # initial state access key
bucket_key = "697WU5WM5EYX"  # initial state bucket key
url = "https://groker.init.st/api/events?accessKey=" + access_key + "&bucketKey=" + bucket_key  # full url getting general url add variable access key and bucket key

ser = serial.Serial(
    port='COM3',  # set to com on windows or tty on py
    baudrate=9600,  # is the bit rate of the bored the default is 9600
    parity=serial.PARITY_NONE,  # no idea
    stopbits=serial.STOPBITS_ONE,  # no idea
    bytesize=serial.EIGHTBITS,  # 8 bit
    timeout=1)  # also no idea

val = 0  # sets val to 0 on start
print("connected to: " + ser.portstr)

while True:
    val = ser.readline()  # reads serial line
    print(type(val))
    if len(val) >= 1:  # bug if the val is less than 1 it wont send is needed to cut b'' form the results
        post_name = (str(val)[2:-31])  # -31=4 char for the if you have a longer name make it bigger also
        variable = (str(val)[12:-15])  # 12=4 char for name if you have a longer name make it bigger also gets the val from serial read removes 12 char from the start and 15 from the end. is the variable value that's sent to initial state
        post_url = "{}&{}={}".format(url, post_name,variable)  # formatting the url - compiles the url, post name and variable into one line , & is for string = for int

        print(post_url)  # print to console
        requests.post(post_url)  # request is the name of a repository and post is the command to post it to the website
ser.close()

# ======================================================================================================================
#
# ======================================================================================================================
