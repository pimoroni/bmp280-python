#!/usr/bin/env python

from bmp280 import BMP280

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

print("""dump-calibration.py - Dumps calibration data.

Press Ctrl+C to exit!

""")

# Initialise the BMP280
bmp280 = BMP280(i2c_dev=SMBus(1))
bmp280.setup()

for key in dir(bmp280.calibration):
    if key.startswith('dig_'):
        value = getattr(bmp280.calibration, key)
        print('{} = {}'.format(key, value))
