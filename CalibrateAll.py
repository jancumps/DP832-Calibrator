from Psu import *
from Dmm import *
from Calibrate import *


# Settings

psuResource = 'USB0::0x1AB1::0x0E11::DP8B152800364::INSTR'
dmmResource = 'USB0::0x05E6::0x6500::04386016::INSTR'


# Code

psu = Psu(psuResource)
print('Connected to PSU at \'{:s}\''.format(psuResource))

dmm = Dmm(dmmResource)
print('Connected to DMM at \'{:s}\''.format(dmmResource))

psu.reset()

for mode in ['V', 'I']:
    for channel in numpy.arange(1, 4):
        calibrate(psu, dmm, channel, mode)
