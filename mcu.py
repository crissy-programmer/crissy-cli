#!/usr/bin/env python

import serial
import time

ser = serial.Serial()

def split(data):
    low = data & 0x00ff
    high = (data & 0xff00) >> 8

    return high, low

def open(port):
    ser.port = port
    ser.open()
    time.sleep(3)

def prog_enable():
    ser.write([ord("s")])

def erase_chip():
    ser.write([ord("e")])

def finalize():
    ser.write([ord("f")])

def write_progmem(addr, data):
    high,low = split(addr)

    # envia o endereco
    addr_data = bytearray( [ord('a'), low, ord('A'), high] ) 
    ser.write(addr_data)

    # envia o dado
    ser.write( bytearray( [ ord('w'), data ] ) )

def close():
    ser.close()
