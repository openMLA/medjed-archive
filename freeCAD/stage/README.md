# XY stage

The XY stage has the following limits:

---

With Base 4-inch stage

X: 158mm (Z-axis prevents movement)

Y: 168mm 

---

With no stage (just the snapmaker carriage)

X: 168mm 

Y: 168mm 

## Sample chuck

The sample chuck PCB would ideally sit at such height that the UV sensor active area is exactly the sample height. For a typical Si sample: 0.5mm. Doing so, however, would mean the PCB and components stick out above the chuck's surface level. I think this is not ideal as it limits the sample size but also increases risk of collision.

The three ICs on the frontside have the following max heights:

* ICM42605: 0.97mm
* OPT3002: 0.65mm
* SHT45 (with PTFE filter): 0.79

Accounting for solder height and maybe poor seating I think recessing the PCB surface 1.5mm below the chuck should be adequate. 