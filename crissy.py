#!/usr/bin/env python

import serial
from intelhex import IntelHex

STX = 0x01
ETX = 0x03

port = serial.Serial('/dev/ttyACM0', 9600)

def sendPacket(packet):
    chk = 0
    for byte in packet:
        chk = chk ^ byte

    data = [STX]
    data.append(packet.count)
    data.extend(packet)
    data.append(chk)
    data.append(ETX)


if __name__ == "__main__":
    hexfile = IntelHex('teste.hex').todict()
    for addr, code in hexfile.items():
        print("%x : %x" %(addr, code))
        sendPacket([addr, code])
