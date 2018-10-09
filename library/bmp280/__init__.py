"""BMP280 Driver."""
from i2cdevice import Device, Register, BitField, _int_to_bytes
from i2cdevice.adapter import LookupAdapter, Adapter
import struct

CHIP_ID = 0x58


class S16Adapter(Adapter):
    """Convert unsigned 16bit integer to signed."""

    def _decode(self, value):
        return struct.unpack('>h', _int_to_bytes(value, 2))[0]


_bmp280 = Device(0x76, bit_width=8, registers=(
    Register('CHIP_ID', 0xD0, fields=(
        BitField('id', 0xFF),
    )),
    Register('RESET', 0xE0, fields=(
        BitField('reset', 0xFF),
    )),
    Register('STATUS', 0xF3, fields=(
        BitField('measuring', 0b00001000),  # 1 when conversion is running
        BitField('im_update', 0b00000001),  # 1 when NVM data is being copied
    )),
    Register('CTRL_MEAS', 0xF4, fields=(
        BitField('osrs_t', 0b11100000,   # Temperature oversampling
                 adapter=LookupAdapter({
                     1: 0b001,
                     2: 0b010,
                     4: 0b011,
                     8: 0b100,
                     16: 0b101
                 })),
        BitField('osrs_p', 0b00011100,   # Pressure oversampling
                 adapter=LookupAdapter({
                     1: 0b001,
                     2: 0b010,
                     4: 0b011,
                     8: 0b100,
                     16: 0b101})),
        BitField('mode', 0b00000011,     # Power mode
                 adapter=LookupAdapter({
                     'sleep': 0b00,
                     'forced': 0b10,
                     'normal': 0b11})),
    )),
    Register('CONFIG', 0xF5, fields=(
        BitField('t_sb', 0b11100000,     # Temp standby duration in normal mode
                 adapter=LookupAdapter({
                     0.5: 0b000,
                     62.5: 0b001,
                     125: 0b010,
                     250: 0b011,
                     500: 0b100,
                     1000: 0b101,
                     2000: 0b110,
                     4000: 0b111})),
        BitField('filter', 0b00011100),                   # Controls the time constant of the IIR filter
        BitField('spi3w_en', 0b0000001, read_only=True),  # Enable 3-wire SPI interface when set to 1. IE: Don't set this bit!
    )),
    Register('DATA', 0xF7, fields=(
        BitField('temperature', 0x000000FFFFF0),
        BitField('pressure', 0xFFFFF0000000),
    ), bit_width=48),
    Register('CALIBRATION', 0x88, fields=(
        BitField('dig_t1', 0xFFFF << 16 * 11),                         # 0x88 0x89
        BitField('dig_t2', 0xFFFF << 16 * 10, adapter=S16Adapter()),   # 0x8A 0x8B
        BitField('dig_t3', 0xFFFF << 16 * 9, adapter=S16Adapter()),    # 0x8C 0x8D
        BitField('dig_p1', 0xFFFF << 16 * 8),                          # 0x8E 0x8F
        BitField('dig_p2', 0xFFFF << 16 * 7, adapter=S16Adapter()),    # 0x90 0x91
        BitField('dig_p3', 0xFFFF << 16 * 6, adapter=S16Adapter()),    # 0x92 0x93
        BitField('dig_p4', 0xFFFF << 16 * 5, adapter=S16Adapter()),    # 0x94 0x95
        BitField('dig_p5', 0xFFFF << 16 * 4, adapter=S16Adapter()),    # 0x96 0x97
        BitField('dig_p6', 0xFFFF << 16 * 3, adapter=S16Adapter()),    # 0x98 0x99
        BitField('dig_p7', 0xFFFF << 16 * 2, adapter=S16Adapter()),    # 0x9A 0x9B
        BitField('dig_p8', 0xFFFF << 16 * 1, adapter=S16Adapter()),    # 0x9C 0x9D
        BitField('dig_p9', 0xFFFF << 16 * 0, adapter=S16Adapter()),    # 0x9E 0x9F
    ), bit_width=192)
))
