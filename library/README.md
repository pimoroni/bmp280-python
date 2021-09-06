# BMP280 Temperature, Pressure, & Altitude Sensor

[![Build Status](https://travis-ci.com/pimoroni/bmp280-python.svg?branch=master)](https://travis-ci.com/pimoroni/bmp280-python)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/bmp280-python/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/bmp280-python?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/bmp280.svg)](https://pypi.python.org/pypi/bmp280)
[![Python Versions](https://img.shields.io/pypi/pyversions/bmp280.svg)](https://pypi.python.org/pypi/bmp280)

Suitable for measuring ambient temperature, barometric pressure, and altitude, the BMP280 is a basic weather sensor.

# Installing

Stable library from PyPi:

* Just run `sudo pip install bmp280`

Latest/development library from GitHub:

* `git clone https://github.com/pimoroni/bmp280-python`
* `cd bmp280-python`
* `sudo ./install.sh`


# Changelog
0.0.4
-----

* Add support for forced-mode on demand i2c
* Change altitude formula
* Allow manual temperature compensation for altitude
* Allow oversampling settings to be configured on `__init__`

0.0.3
-----

* Migrate to i2cdevice>=0.0.6 set/get API

0.0.2
-----

* Added `get_altitude` method
* Corrected pressure to hPa

0.0.1
-----

* Initial Release
