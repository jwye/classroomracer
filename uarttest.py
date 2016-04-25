#http://stackoverflow.com/questions/33898323/uart-communication-with-hex-code
#http://pyserial.readthedocs.org/en/latest/shortintro.html
#http://www.2cto.com/kf/201208/145066.html
#BOARD RT is 9bits not sure the protocal
# a. 0xAA b. 0x55 c.0x00


import serial
import time
import binascii

ser = serial.Serial()
ser.port= '/dev/tty.usbserial'
ser.baudrate = 26640
ser.timeout= 1
ser.parity='O'

ser.open()

print(ser.isOpen())
try:
    for i in range(50000):
        #arr1 = bytearray([0xAA,0x00,0x12,0x03,0x12,0x03])
        #arr1 = bytearray([0xAA,0xAA,0xFC,0x03,0xFC,0x03])
        #arr1 = bytearray([0xAA,0x80,0xFC,0x03,0xFC,0x03])
        arr1=bytearray([0xAA])
        #ser.parity="PARITY_NONE"
        #ser.parity='N'
        ser.write(arr1)

        #ser.parity='E'
        #ser.write(arr1)

        #ser.parity='O'
        #ser.write(arr1)

        #ser.close()
        #ser.parity='S'
        #ser.open()
        #ser.write(arr1)

        #ser.close()
        #ser.parity='M'
        #ser.open()
        #ser.write(arr1)
        #arr2=0x00
        #ser.write(arr2)

        #arr3=0x55
        #ser.write(arr3)
except(KeyboardInterrupt, SystemExit):
    ser.close()

while 1:
    try:

        #arr1 = bytearray([0xAA,0x00,0x10,0x10])
        arr1 = bytearray([0x55,0x80,0xFC,0x03,0xFC,0x03])
        ser.write(arr1)




    except(KeyboardInterrupt, SystemExit):
        ser.close()
