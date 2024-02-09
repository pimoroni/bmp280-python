import sys

import mock
import pytest


def test_setup_not_present():
    sys.modules['smbus2'] = mock.MagicMock()
    from bmp280 import BMP280
    bmp280 = BMP280()
    with pytest.raises(RuntimeError):
        bmp280.setup()


def test_setup_mock_present():
    from tools import SMBusFakeDevice
    smbus = mock.Mock()
    smbus.SMBus = SMBusFakeDevice
    sys.modules['smbus2'] = smbus
    from bmp280 import BMP280
    bmp280 = BMP280()
    bmp280.setup()


def test_setup_forced_mode():
    from tools import SMBusFakeDevice
    smbus = mock.Mock()
    smbus.SMBus = SMBusFakeDevice
    sys.modules['smbus2'] = smbus
    from bmp280 import BMP280
    bmp280 = BMP280()
    bmp280.setup(mode="forced")
