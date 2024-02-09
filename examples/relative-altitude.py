#!/usr/bin/env python

import time

from smbus2 import SMBus

from bmp280 import BMP280

print("""relative-altitude.py - Calculates relative altitude from pressure.

Press Ctrl+C to exit!

""")

# Initialise the BMP280
bus = SMBus(1)
bmp280 = BMP280(i2c_dev=bus)

baseline_values = []
baseline_size = 100

print(f"Collecting baseline values for {baseline_size:d} seconds. Do not move the sensor!\n")

for i in range(baseline_size):
    pressure = bmp280.get_pressure()
    baseline_values.append(pressure)
    time.sleep(1)

baseline = sum(baseline_values[:-25]) / len(baseline_values[:-25])

while True:
    altitude = bmp280.get_altitude(qnh=baseline)
    print(f"Relative altitude: {altitude:05.2f} metres")
    time.sleep(1)
