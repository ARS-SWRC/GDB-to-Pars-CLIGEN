# MakeMaps.py
Creates CLIGEN parameter maps in geotiff format.

## Description
Creates parameter maps in geotiff format for cases where ESRI GDB is not the preferred format or if only a subset of maps is desired.

## Requirements
- Python 3.9 minimum
- GDAL/osgeo library 3.10 minimum
- Pandas library
- Pyinstaller command-line tool (if creating exe)

## Directory Setup
```bash
--Current Working Dir CL_Tool.py
    |--maps
       |--list.txt
       |--maps_out
           |--*.tif
       |--MakeMaps_Standalone.py (if running as Python script only)
       |--MakeMaps.py (run with PyInstaller when compiling exe)
       |--MakeMaps.exe (if compiling exe, move exe from dist folder to here)
       |--build (created by PyInstaller when compiling exe, not needed after compiling)
       |--dist (created by PyInstaller when compiling exe, not needed after compiling)
```
## User Inputs
The main options are specified in `list.txt` and should be modified by the user. This file contains a list of lat/lon points to write *.par files to the `maps_out` folder. `list.txt` has placeholder entries as examples. It is then necessary to put the names of these *.txt files in `list.txt`. An easier option is using `Search` as the wind option in `list.txt`, which automatically uses wind parameter sets from the nearest station in `parfiles-2015`.

Valid GCM strings:
```sh
CCSM4, CanESM2, MIROC5
```

Valid variable names:
```sh
 DEM, accm, mean, mx5p, pwd, pww, ratio, sdev, skew, srad, srsd, tdew, timepk, tmax, tmin, tnsd, txsd
```

Valid year window strings:
```sh
1974_2013, 2000_2029, 2010_2039, 2020_2049, 2030_2059, 2040_2069, 2050_2079, 2060_2089, 2070_2099
```

*For DEM, ratio, and timepk, only the 1974_2013 window is valid.
