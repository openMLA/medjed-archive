## Medjed mainboard

Notes about the mainboard/stage controller for the medjed MLA system.

The current PCB aims to drive the `TMC2209` in the linear axes by combining a `TMC424` (encoder) and `TMC429` (motioncontroller). The datasheet for the `TMC424` is really quite poor however, and the product seems a bit of an afterthought by Trinamic.

The board will probably be redesigned around the `TMC4361A` (one for each axis).  

### Power considerations

The snapmaker linear axes use 24V supply. The snapmaker power supply comes with plenty of overhead in terms of power (as it need to be able to run a 3D printer heated bed) so that is not a concern. 

We also need 5V and 3.3V supply on the board.

5V:

* Teensy 4.1: 100mA
* [3X] RLC2IC encoders: <30mA (no termination resistors) or <130mA with 120ohm termination.
* [3X] AM26LS32A: max 70mA, typ 50mA

3.3V:

* TMC424: 1.5mA
* TMC429: 10mA (running in 3.3V CMOS mode)
* (for future revision: IMXRT60: 53mA)

1.5V:

* TMC424: 10.5mA

### Other

The documentation for `TMC424` does not list a MISO connection to the `TMC429`. It may not be necessary as the information encoded in the Datagrams is precisely the part handled by the `TMC424` (i.e.). Still it might be useful for reading back the state of registers which I don't believe is possible through the `TMC424`. For now I have handled it with a solder jumper.