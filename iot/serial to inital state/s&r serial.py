import serial
import requests

access_key = "ist_WNCOhg0VQNzA4AQT9NqLLQ-UXPTwe5pF"  # initialstate access key
bucket_key = "697WU5WM5EYX"  # initialstate bucket key
url = "https://groker.init.st/api/events?accessKey=" + access_key + "&bucketKey=" + bucket_key  # full url getting
# general url add varible access key and bucket key

ser = serial.Serial(
    port='COM3',  # set to com on windows or tty on py
    baudrate=9600,  # is the bit rate of the bored the default is 9600
    parity=serial.PARITY_NONE,  # no idea
    stopbits=serial.STOPBITS_ONE,  # no idea
    bytesize=serial.EIGHTBITS,  # 8 bit
    timeout=1)  # also no idea

val = 0  # sets val to 0 on start

while True:
    val = ser.readline()  # reads serial line
    if len(val) > 1:  # bug if the val is less than 1 it wont send is needed to cut b'' form the results
        post_name = "temp"  # the variable name that shows up on initial state
        variable = (str(val)[2:-1])  # the number to post and [2:-1] removes b' ' from the result
        post_url = "{}&{}={}".format(url, post_name, variable)  # formatting the url - compiles the url, post name and
        # variable into one line , & is for string = for int

        # printing the url and sending post request
        print(post_url)  # print to console
        requests.post(post_url)  # request is the name of a repository and post is the commmand to post it to the
        # website
ser.close()













