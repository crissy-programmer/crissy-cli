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
import time

SERIAL_PORT = "--port"
HEX_FILE = "HEX_FILE"

if __name__ == "__main__":
    arguments = docopt(__doc__, version="0.0.1")

    hexfile = IntelHex(arguments[HEX_FILE]).todict()

    print("Porta serial: %s", arguments[SERIAL_PORT])
    
    print("Pronto, enviar os pacotes agora!");
    for addr, code in hexfile.items():
        print("%x : %x" %(addr, code))
