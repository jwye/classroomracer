#using gpio to simulate st32 9 bits usart
#hoverboart protocal

import time
import RPi.GPIO as GPIO

GPIO.cleanup()

def HIGHBIT(port,bt):
    GPIO.output(port, GPIO.HIGH)
    time.sleep(bt) # start

def LOWBIT(port,bt):
    GPIO.output(port, GPIO.LOW)
    time.sleep(bt) # start

def HighPandding(port,bt,n):
    GPIO.output(port, GPIO.HIGH)
    time.sleep(n*bt) # start

def SENDBYTE(byte,bt):
    LOWBIT(11,bt)
    for b in byte:
        if b == '0':
            LOWBIT(11,bt)
        elif b == '1':
            HIGHBIT(11,bt)
    HighPandding(11,bt,1)


Baudrate = 26640
#ONE Bit is 38us
K=0.03
Bittime=K*1/Baudrate
#MDBmode:address indicated MSB=1
MDB=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.HIGH)
print('GPIO 11 is set to HIGH')
time.sleep(1)
try:
    print('GO')
    while 1:
            HighPandding(11,Bittime,81)

            BYTE='010101010'
            SENDBYTE(BYTE,Bittime)


            BYTE='100000000'
            SENDBYTE(BYTE,Bittime)
            HighPandding(11,Bittime,18)

except(KeyboardInterrupt):
    GPIO.cleanup()
