#using gpio to simulate st32 9 bits usart
#hoverboart protocal

import time
import RPi.GPIO as GPIO

Baudrate = 26640
#ONE Bit is 38us
Bittime=40/1000000
BitsinByte = 9
#MDBmode:address indicated MSB=1
MDB=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

try:
    while 1:

        GPIO.output(11, GPIO.HIGH)
        #time.sleep(Bittime)
        GPIO.output(11, GPIO.LOW)
        #time.sleep(Bittime)
        
except(KeyboardInterrupt):
    GPIO.cleanup()
