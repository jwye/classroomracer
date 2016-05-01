#http://stackoverflow.com/questions/33898323/uart-communication-with-hex-code
#http://pyserial.readthedocs.org/en/latest/shortintro.html
#http://www.2cto.com/kf/201208/145066.html
#BOARD RT is 9bits not sure the protocal
# a. 0xAA b. 0x55 c.0x00


import serial
import time
import binascii


ser = serial.Serial()
#ser.port= '/dev/tty.usbserial'
ser.port= '/dev/ttyUSB0'
ser.baudrate = 26640
ser.timeout= 1
ser.parity=serial.PARITY_NONE

ser.open()

print(ser.isOpen())
try:
    for i in range(2000):
        arr1 = bytearray([0x55,0x00,0x13,0x02,0x13,0x02])
        #arr1 = bytearray([0xAA,0xAA,0xFC,0x03,0xFC,0x03])
        #arr1 = bytearray([0xAA,0x80,0xFC,0x03,0xFC,0x03])
        ser.write(arr1)


except(KeyboardInterrupt, SystemExit):
    ser.close()

print(ser.isOpen())

while True:
    try:

        #arr1 = bytearray([0xAA,0x00,0x10,0x10])
        arr1 = bytearray([0x55,0x00,0x13,0x02,0x13,0x02])
        #arr1 = bytearray([0b101010100,0b000000001])
        ser.write(arr1)




    except(KeyboardInterrupt, SystemExit):
        ser.close()
