#using gpio to simulate st32 9 bits usart
#hoverboart protocal

import time
import RPi.GPIO as GPIO

Baudrate = 26640
#ONE Bit is 38us
Bittime=10/10000000
BitsinByte = 9
#MDBmode:address indicated MSB=1
MDB=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.HIGH)
print('GPIO 11 is set to HIGH')
time.sleep(5)
try:
    print('GO')
    while 1:
            time.sleep(30*Bittime)

            # 0xAA 0xAA  0b 1 10101010
            GPIO.output(11, GPIO.LOW)
            time.sleep(Bittime) # start
            # 1010
            GPIO.output(11, GPIO.LOW)
            time.sleep(Bittime) # lsb

            GPIO.output(11, GPIO.HIGH)
            time.sleep(Bittime) # 2

            GPIO.output(11, GPIO.LOW)
            time.sleep(Bittime) # 3

            GPIO.output(11, GPIO.HIGH)
            time.sleep(Bittime) # 4
            # 1010
            GPIO.output(11, GPIO.LOW)
            time.sleep(Bittime) # lsb

            GPIO.output(11, GPIO.HIGH)
            time.sleep(Bittime)

            GPIO.output(11, GPIO.LOW)
            time.sleep(Bittime) # lsb

            GPIO.output(11, GPIO.HIGH)
            time.sleep(Bittime)

            # MSB=0
            GPIO.output(11, GPIO.LOW)
            time.sleep(Bittime)
            # finish 0xAA  0b 1 10101010

            #pandding
            GPIO.output(11, GPIO.HIGH)
            time.sleep(6*Bittime)
            #


            # 0b00000000
            GPIO.output(11, GPIO.LOW)
            time.sleep(8*Bittime)
            # MSB=1
            GPIO.output(11, GPIO.HIGH)
            time.sleep(Bittime)
            # first 9 bits








except(KeyboardInterrupt):
    GPIO.cleanup()
