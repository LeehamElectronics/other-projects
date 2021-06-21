from time import sleep, perf_counter
import serial  # pip install pyserial


ser = serial.Serial(port='COM1', baudrate=9600, timeout=.1)

file = open("cisco.txt", 'r+')
line = file.readlines()
v = len(open('cisco.txt').readlines(  )) - 1

i = 0
q = 0
w = 30
while i < v:
    i = i + 1
    write = line[i]

    while q < w:
        q = q + 1
        read = ser.readline()

        if read != b'':
            print(read)
            print(q)

    while True:
        read = ser.readline()

        if read != b'':
            print(read)

        if read == b'':
            sleep(0.1)
            ser.write(bytes(write, 'utf-8'))
            print(write)
            break

while True:
    while q < w:
        q = q + 1
        read = ser.readline()
        if read != b'':
            print(read)
            print(q)

    ser.write = input()

