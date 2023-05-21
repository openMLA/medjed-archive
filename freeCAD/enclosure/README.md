## Medjed Enclosure

The FreeCAD file in this directory can be used to export `.dxf` files that define cut lines for acrylic panels.  In addition, there are printed parts that can be printed on a standard filament 3D printer. PLA is probably adequate, but if you plan on treating it particularly aggressively you may want to print the structural pieces out of PETG.

Use the **legacy** exporter for dxf, as the new one has some issue at time of writing (2023).

There are 5 panels total

* Front panel (this one is kept as a solid piece, to lower costs; some separation needed when you receive it)
* Back panel
* Side panel 1
* Side panel 2 (identical to panel 1)
* Top panel

### Material choice

I suggest you have the enclosure cut out of orange acrylic. Ideally, choose an acrylic material of which you know the absorption at the relevant wavelengths (centered at 405nm, but consider 390-420). It would be good to have the enclosure made out of material with high absorption in this range (99.9%+). Since the focus of the objective (and hence the UV) is always far away from the user (provided they are not inside the enclosure) very high OD is not needed I suspect (please check safety considerations by yourself).

Something like 

* Plexiglas `ORANGE 2C04`
* Green Cast 

*Note that neither of the above have published transmission spectra (that I could find), and may still transmit a significant amount of UV light.*