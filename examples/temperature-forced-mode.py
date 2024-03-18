import time

from smbus2 import SMBus

from bmp280 import BMP280

bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

# Set up in "forced" mode
# In this mode `get_temperature` and `get_pressure` will trigger
# a new reading and wait for the result.
# The chip will return to sleep mode when finished.
bmp280.setup(mode="forced")

while True:
    temperature = bmp280.get_temperature()
    print("{temperature:05.2f}*C")
    time.sleep(1)
