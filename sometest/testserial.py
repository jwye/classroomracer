import serial

ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=3)
#ser.open()

try:
    while 1:
        response = ser.readline()
        print(response)
except(KeyboardInterrupt):
    ser.close()
