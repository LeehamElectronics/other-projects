# ======================================================================================================================
# made by Bevan Matsacos
# basic read serial
# 3/6/21
# ======================================================================================================================

import serial  # pip install pyserial
import time

ser = serial.Serial(
    port='COM1',  # set to com on windows or tty on py
    baudrate=9600,  # is the bit rate of the bored the default is 9600
    parity=serial.PARITY_NONE,  # no idea
    stopbits=serial.STOPBITS_ONE,  # no idea
    bytesize=serial.EIGHTBITS,  # 8 bit
    timeout=1)  # also no idea

val = 0  # sets val to 0 on start
print("connected to: " + ser.portstr)

while True:
    val = ser.readline()  # reads serial line
    print(str(val))

ser.close()

# ======================================================================================================================
#
# ======================================================================================================================
