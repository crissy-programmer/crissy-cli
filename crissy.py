#!/usr/bin/env python
"""
Crissy Programmer, An AT89S52 command-line programmer.

Usage: 
    crissy.py [options] HEX_FILE
    crissy.py -h | --help
    crissy.py --version

Options:
    -h, --help                  Show this help message.
    --version                   Show programmer version.
    -p SERIAL, --port SERIAL    The serial port of the programmer hardware [default: /dev/ttyACM0]    
"""

import serial
from intelhex import IntelHex
from docopt import docopt

STX = 0x01
ETX = 0x03
SERIAL_PORT = "SERIAL"
HEX_FILE = "HEX_FILE"


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
    arguments = docopt(__doc__, version="0.0.1")

    #port = serial.Serial('/dev/ttyACM0', 9600)

    hexfile = IntelHex('teste.hex').todict()
    for addr, code in hexfile.items():
        print("%x : %x" %(addr, code))
        #sendPacket([addr, code])
