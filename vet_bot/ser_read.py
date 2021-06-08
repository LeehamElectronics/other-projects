# ======================================================================================================================
# made by Bevan Matsacos
# basic read serial
# 3/6/21
# ======================================================================================================================

import serial  # pip install pyserial
import time

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
    val = ser.readline()  # reads serial line
    print(str(val))

ser.close()

#if str(range_start) <= str(y_pos.get()) <= str(range_end):
#
# def thread_b():
#     print("test")
#     sleep(delay_start)
#     i = 0
#     range_start = -9999
#     range_end = 9999
#     print(y_pos.get())
#     while thread_start.get() == str(1):
#         #print("test 3")
#         #sleep(2)
#         if int(y_pos.get()) >= int(range_start):
#             print("test 2")
#             sleep(1)
#             if int(y_pos.get()) <= int(range_end):
#                 print("test 1")
#                 sleep(1)
#                 if int(range_start) <= int(y_pos.get()) <= int(range_end):
#                     print("test 0")
#                     print(y_pos.get())
#                     sleep(1)
#                     sleep(delay_run)
#                     i = int(y_pos.get()) + 1
#                     y_pos.set(i)
#                     x = "1"
#                     ser.write(bytes(x, 'utf-8'))
#                     sleep(1)

# ======================================================================================================================
#
# ======================================================================================================================
