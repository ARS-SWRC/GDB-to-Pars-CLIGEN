# GDB-to-Pars-CLIGEN
Creates CLIGEN par files from ESRI geodatabases containing parameter maps.

## Description
This Python-based package queries ESRI formatted geodatabases (GDBs) that contain CLIGEN parameter map sets representing climate change. The GDBs are supplied as part of the SWPar4.5 dataset with coverage of Nevada, Utah, Arizona and New Mexico in the southwestern U.S. at ~800m resolution.

## Requirements
- Python 3.9 minimum
- GDAL/osgeo library 3.10 minimum
- Pandas library
- Pyinstaller command-line tool (if creating exe)

## Directory Setup
```bash
-Current Working Dir
   |--list.txt
   |--search_stations.txt
   |--pars
       |--*.par
   |--wind-strings
       |--*.txt
   |--CCSM4.gdb
   |--CanESM2.gdb
   |--MIROC5.gdb
   |--classes
       |--formatting.py
       |--__init__.py
   |--parfiles-2015
       |--*.par
   |--CL_Tool_Standalone.py (if running as Python script only)
   |--CL_Tool.py (if compiling exe)
   |--CL_Tool.exe (if using executable, move from dist folder to here)
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

