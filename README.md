# GDB-to-Pars-CLIGEN
Creates CLIGEN par files from ESRI geodatabases containing parameter maps.

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
   |--CL_Tool.exe (if using executable, move from dist folder to here)
   |--build (created by pyinstaller when compiling exe)
   |--dist (created by pyinstaller when compiling exe)
```
## User Inputs
The main options are specified in `list.txt` and should be modified by the user. This file contains a list of lat/lon points to create *.par files for, which will be written to the `pars` folder. The version of `list.txt` in this repository has placeholder entries as examples. 

Valid year window strings:
```sh
1974_2013, 2000_2029, 2010_2039, 2020_2049, 2030_2059, 2040_2069, 2050_2079, 2060_2089, 2070_2099
```


