# ======================================================================================================================
# made by Bevan Matsacos
# basic write serial
# 3/6/21
# ======================================================================================================================

import serial  # pip install pyserial
from time import sleep, perf_counter

ser = serial.Serial(
    port='COM2',  # set to com on windows or tty on py
    baudrate=9600,  # is the bit rate of the bored the default is 9600
    parity=serial.PARITY_NONE,  # no idea
    stopbits=serial.STOPBITS_ONE,  # no idea
    bytesize=serial.EIGHTBITS,  # 8 bit
    timeout=1)  # also no idea

val = 0  # sets val to 0 on start
print("connected to: " + ser.portstr)

while True:
    val = "hello\n" .encode('utf-8')
    ser.write(val)  # reads serial line
    sleep(0)

ser.close()
