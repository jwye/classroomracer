#using gpio to simulate st32 9 bits usart
#hoverboart protocal

import time
import RPi.GPIO as GPIO


def HIGHBIT(port,time):
    GPIO.output(port, GPIO.HIGH)
    time.sleep(time) # start

def LOWBIT(port,time):
    GPIO.output(port, GPIO.LOW)
    time.sleep(time) # start

def HighPandding(port,time,n):
    GPIO.output(port, GPIO.HIGH)
    time.sleep(n*time) # start

def SENDBYTE(byte,time):
    for b in byte:
        if b == '0':
            LOWBIT(11,time)
        elif b == '1':
            HIGHBIT(11,time)


Baudrate = 26640
#ONE Bit is 38us
K=0.5
Bittime=K*1/Baudrate
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
            HighPandding(11,Bittime,810)

            BYTE='010101010'
            SENDBYTE(BYTE,Bittime)
            HighPandding(11,Bittime,50)

            BYTE='100000000'
            SENDBYTE(BYTE,Bittime)
            HighPandding(11,Bittime,50)

except(KeyboardInterrupt):
    GPIO.cleanup()
