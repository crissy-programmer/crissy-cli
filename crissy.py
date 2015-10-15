#!/usr/bin/env python

"""
Crissy Programmer, An AT89S52 command-line programmer.

Usage: 
    crissy.py [options] <hex_file>
    crissy.py -h | --help
    crissy.py --version

Options:
    -h, --help                  Show this help message.
    --version                   Show programmer version.
    -p <port>, --port <port>    The serial port of the programmer hardware [default: /dev/ttyACM0].
    -b <baudrate>               The baudrate [default: 9600].
"""

from intelhex import IntelHex
from docopt import docopt
import mcu
import time

SERIAL_PORT = "--port"
HEX_FILE = "<hex_file>"
BAUDRATE = "-b"

if __name__ == "__main__":
    arguments = docopt(__doc__, version="0.0.1")
    print(arguments)

    hexfile = IntelHex(arguments[HEX_FILE]).todict()

    port_name = arguments[SERIAL_PORT]
    baudrate = arguments[BAUDRATE]
    print("Porta serial: %s, baudrate: %s", port_name, baudrate)
    mcu.open(port_name, int(baudrate))

    print("Habilitar programacao...")
    mcu.prog_enable()
    ack = mcu.ser.readline()
    print("--> %s" % ack)

    print("Apagar o chip...")
    mcu.erase_chip()
    ack = mcu.ser.readline()
    time.sleep(0.5)
    print("--> %s" % ack)

    print("Lendo o arquivo .hex, e carregando no micro.");
    for addr, code in hexfile.items():
        print("%x : %x" %(addr, code))
        mcu.write_progmem(addr, code)

        ack = mcu.ser.readline()
        print("--> %s" % ack)

    print("Finalizar a gravacao...")
    mcu.finalize()
    ack = mcu.ser.readline()
    print("--> %s" % ack)

    mcu.close()
