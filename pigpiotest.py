#ref. http://raspberrypi.stackexchange.com/questions/27488/pigpio-library-example-for-bit-banging-a-uart

import sys
import time
import pigpio

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

TEXT=0

pi.wave_add_serial(TX, baud, TEXT,bb_bits=bits)
wid=pi.wave_create()
wave_send_using_mode(wid,WAVE_MODE_REPEAT_SYNC)
print("baud={} bits={}".format(baud, bits))

wait=input('wait to close')

pi.wave_delete(wid)
pi.stop()
