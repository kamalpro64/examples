# This script can be used to connect to GPIB, RS232, USB, Ethernet
import pyvisa

rm = pyvisa.ResourceManager()
rm.list_resources()
addr = 'GPIB0::XX::INSTR'
inst = rm.open_resource(addr)
print(inst.query('*IDN?')
