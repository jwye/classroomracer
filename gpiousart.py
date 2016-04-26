#using gpio to simulate st32 9 bits usart
#hoverboart protocal

import time
import RPi.GPIO as GPIO


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

def OX55():
    BYTE='101010100'  #0b001010101  #0x55
    SENDBYTE(BYTE,Bittime)

    BYTE='000000001' #b100000000  #0x00
    SENDBYTE(BYTE,Bittime)

    BYTE='000100000'#b000001000  #0x10
    SENDBYTE(BYTE,Bittime)

    BYTE='001100000' #b000001100  #0x0c
    SENDBYTE(BYTE,Bittime)

    BYTE='000100000'#b000001000  #0x10
    SENDBYTE(BYTE,Bittime)

    BYTE='001100000' #b000001100  #0x0c
    SENDBYTE(BYTE,Bittime)
    HighPandding(11,Bittime,27)

def OXAA():
    BYTE='010101010' #010101010  #0xAA
    SENDBYTE(BYTE,Bittime)

    BYTE='000000001' #b100000000  #0x00
    SENDBYTE(BYTE,Bittime)

    BYTE='000100000'#b000001000  #0x10
    SENDBYTE(BYTE,Bittime)

    BYTE='001100000' #b000001100  #0x0c
    SENDBYTE(BYTE,Bittime)

    BYTE='000100000'#b000001000  #0x10
    SENDBYTE(BYTE,Bittime)

    BYTE='001100000' #b000001100  #0x0c
    SENDBYTE(BYTE,Bittime)


    HighPandding(11,Bittime,27)


Baudrate = 26640
#ONE Bit is 38us
K=0.03
Bittime=K/Baudrate
Bittime=0.1/1000000
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
        OX55()

except(KeyboardInterrupt):
    GPIO.cleanup()
