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
    LOWBIT(11,bt) #start
    for b in byte:
        if b == '0':
            LOWBIT(11,bt)
        elif b == '1':
            HIGHBIT(11,bt)
    HIGHBIT(11,bt) #finish


Baudrate = 26640
#ONE Bit is 38us
K=0.07
Bittime=K/Baudrate
#MDBmode:address indicated MSB=1
MDB=1

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.HIGH)
print('GPIO 11 is set to HIGH')
time.sleep(1)
try:
    print('GO')
    while 1:


            BYTE='100000000'  #0x00
            SENDBYTE(BYTE,Bittime)

            BYTE='000001000'  #0x10
            SENDBYTE(BYTE,Bittime)

            BYTE='000001100'  #0x0c
            SENDBYTE(BYTE,Bittime)

            BYTE='000001000'  #0x10
            SENDBYTE(BYTE,Bittime)

            BYTE='000001100'  #0x0c
            SENDBYTE(BYTE,Bittime)

            BYTE='010101010'  #0xAA
            SENDBYTE(BYTE,Bittime)

            HighPandding(11,Bittime,21)




except(KeyboardInterrupt):
    GPIO.cleanup()
