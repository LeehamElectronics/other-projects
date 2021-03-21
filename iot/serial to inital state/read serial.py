import serial

ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

print("connected to: " + ser.portstr)
count=2
val = 0
data = 0
while True:
    val = ser.readline()
    if len(val) > 1:
        print(str(val)[2:-1])
ser.close()
