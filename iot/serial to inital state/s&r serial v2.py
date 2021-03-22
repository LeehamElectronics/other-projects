import serial
import requests

access_key = "ist_WNCOhg0VQNzA4AQT9NqLLQ-UXPTwe5pF"
bucket_key = "697WU5WM5EYX"
url = "https://groker.init.st/api/events?accessKey=" + access_key + "&bucketKey=" + bucket_key

ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

val = 0

while True:
    val = ser.readline()
    if len(val) >= 1:
        post_name = (str(val)[2:-31])
        variable = (str(val)[10:-15])
        post_url = "{}&{}={}".format(url, post_name, variable)

        print(post_url)
        requests.post(post_url)
ser.close()

