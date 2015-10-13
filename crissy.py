#!/usr/bin/env python

"""
Crissy Programmer, An AT89S52 command-line programmer.

Usage: 
    crissy.py -p SERIAL_PORT HEX_FILE
    crissy.py -h | --help
    crissy.py --version

Options:
    -h, --help                  Show this help message.
    --version                   Show programmer version.
    -p SERIAL, --port SERIAL    The serial port of the programmer hardware [default: /dev/ttyACM0]    
"""

from intelhex import IntelHex
from docopt import docopt
import mcu

SERIAL_PORT = "--port"
HEX_FILE = "HEX_FILE"

if __name__ == "__main__":
    arguments = docopt(__doc__, version="0.0.1")

    hexfile = IntelHex(arguments[HEX_FILE]).todict()

    port_name = arguments[SERIAL_PORT]
    print("Porta serial: %s", port_name)
    mcu.open(port_name)

    print("Habilitar programacao...")
    mcu.prog_enable()

    print("Apagar o chip...")
    mcu.erase_chip()
    
    print("Lendo o arquivo .hex, e carregando no micro.");
    for addr, code in hexfile.items():
        print("%x : %x" %(addr, code))
        mcu.write_progmem(addr, code)

    print("Finalizar a gravacao...")
    mcu.finalize()
    mcu.close()
