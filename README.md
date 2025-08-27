# GDB-to-Pars-CLIGEN
Creates CLIGEN par files from ESRI geodatabases containing parameter maps. The geodatabases are available at:

SWPar4.5 https://doi.org/10.25422/azu.data.28507262

SWPar8.5 https://doi.org/10.25422/azu.data.28719917

## Description
This Python-based package queries ESRI formatted geodatabases (GDBs) that contain CLIGEN parameter map sets based on gridded climate projections. The GDBs are supplied as part of the SWPar4.5 dataset with coverage of Nevada, Utah, Arizona and New Mexico in the southwestern U.S. at ~800m resolution. To make the data accessible, this tool has two purposes: (**1**) the primary purpose is to create formatted parameter files that are required CLIGEN input; (**2**) secondarily, parameter maps in geotiff format may be created for cases where ESRI GDB is not the preferred format or if only a subset of maps is desired. The directory structure matters for the parent folder and the maps folder when either the stand alone scripts or EXEs are run. The directory structure should be the same as detailed below, and viewing the maps folder shows the necessary structure for this sub-folder when creating geotiff maps.

While this tool kit is useful for doing batch queries, a website for querying single locations can be accessed at: https://apps.tucson.ars.ag.gov/cligenpar

## Requirements
- Python 3.9 minimum
- GDAL/osgeo library 3.10 minimum
- Pandas library
- Pyinstaller command-line tool (if creating exe)

## Directory Setup
```bash
-Current Working Dir CL_Tool.py
   |--list.txt
   |--search_stations.txt
   |--pars
       |--*.par
   |--wind-strings
       |--*.txt
   |--CCSM4.gdb (at least one GDB needed)
   |--CanESM2.gdb (at least one GDB needed)
   |--MIROC5.gdb (at least one GDB needed)
   |--classes
       |--formatting.py
       |--__init__.py
   |--parfiles-2015
       |--*.par
   |--CL_Tool_Standalone.py (if running as Python script only)
   |--CL_Tool.py (run with PyInstaller when compiling exe)
   |--CL_Tool.exe (after compiling exe, move exe from dist folder to here)
   |--build (created by PyInstaller when compiling exe, not needed after compiling)
   |--dist (created by PyInstaller when compiling exe, not needed after compiling)
```
## User Inputs
The user manually modifies `list.txt` with a list of lat/lon points to write *.par files to the `pars` folder for. The `list.txt` file has placeholder entries as examples, with resulting placeholder files inside `pars` and `wind-strings`. The SWPar4.5 dataset includes all required parameters except for wind parameter sets. In order to produce complete *.par files, an option is to put custom *.txt files inside `wind-strings` that contain formatted wind parameter text blocks, which may be taken from ground stations in `parfiles-2015`. It is then necessary to put the names of these *.txt files in `list.txt`. An easier option is using `Search` as the wind option in `list.txt`, which automatically uses wind parameter sets from the nearest station in `parfiles-2015`.

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
## Running
The PyInstaller command used to create the EXEs has the windowless option enabled. This means that the created EXEs run in the background. The EXEs were ran successfully if the outputs specified in list.txt appear in either the pars folder or the maps_out folder, depending on which EXE was used. If the expected outputs don't appear, check for errors in the formatting in list.txt and that the directory structure is correct.
