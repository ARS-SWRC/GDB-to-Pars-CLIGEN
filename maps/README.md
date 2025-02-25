# GDB-to-Maps-CLIGEN
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
--CL_Tool
    |--maps
       |--MakeMaps_Standalone.py (if running as Python script only)
       |--MakeMaps.py (if compiling exe)
       |--MakeMaps.exe (if compiling exe, move exe from dist folder to here)
       |--build (created by pyinstaller when compiling exe, not needed after compiling)
       |--dist (created by pyinstaller when compiling exe, not needed after compiling)
```
## User Inputs
The main options are specified in `list.txt` and should be modified by the user. This file contains a list of lat/lon points to write *.par files to the `pars` folder. `list.txt` has placeholder entries as examples, with resulting placeholder files inside `pars` and `wind-strings`. The SWPar4.5 dataset includes all required parameters except for wind parameter sets. In order to produce complete *.par files, an option is to put custom *.txt files inside `wind-strings` that contain formatted wind parameter text blocks, which may be taken from ground stations in `parfiles-2015`. It is then necessary to put the names of these *.txt files in `list.txt`. An easier option is using `Search` as the wind option in `list.txt`, which automatically uses wind parameter sets from the nearest station in `parfiles-2015`.

Valid GCM strings:
```sh
CCSM4, CanESM2, MIROC5
```

Valid year window strings:
```sh
1974_2013, 2000_2029, 2010_2039, 2020_2049, 2030_2059, 2040_2069, 2050_2079, 2060_2089, 2070_2099
```

Valid wind options:
```sh
Search, <some_custom_wind_string_name>
```

