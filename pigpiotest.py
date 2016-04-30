#ref. http://raspberrypi.stackexchange.com/questions/27488/pigpio-library-example-for-bit-banging-a-uart

import sys
import time
import pigpio

open_pigpio()

def open_pigpio():
    command = "/usr/bin/sudo pigpiod now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)


RX=19
TX=26
baud=26640
bits=9

pi = pigpio.pi()
pi.set_mode(TX, pigpio.OUTPUT)
pigpio.exceptions = False
pi.bb_serial_read_close(RX)
pigpio.exceptions = True
pi.wave_clear()

msg = [0]*6
msg[0]=b'100000000'#256#b100000000'
msg[1]=b'001001001'#73#b'001001001'
msg[2]=b'001001011'#75#b'001001011'
msg[3]=msg[1]
msg[4]=msg[2]
msg[5]=b'110101010'#426#b'110101010'

TEXT=msg[:]
TEXT=TEXT[:]
DATA=b'0x155'

pi.wave_add_serial(TX, baud, DATA,bb_bits=bits)
wid=pi.wave_create()
wave_send_using_mode(wid,WAVE_MODE_REPEAT_SYNC)
print("baud={} bits={} data={}".format(baud, bits, TEXT))

wait=input('wait to close')

pi.wave_delete(wid)
pi.stop()
