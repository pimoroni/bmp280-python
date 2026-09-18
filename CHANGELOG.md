2.0.0
-----

* Enhancement: Repackage to the uv/hatchling method, with PyPI trusted publishing
* Enhancement: Version is derived from the git tag, __version__ from package metadata
* Fix: forced mode could wait forever for a measurement that never completes
* Fix: first reading in normal mode was taken before the first conversion finished
* Fix: get_altitude took three measurements instead of one
* Python 3.9 or later, 3.7 and 3.8 support dropped

1.0.0
-----

* Repackage to hatch/pyproject.toml

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
