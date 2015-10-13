#!/usr/bin/python

import serial

ser = serial.Serial('/dev/pts/3')

while True:
    data = ser.read()
    print(data)
