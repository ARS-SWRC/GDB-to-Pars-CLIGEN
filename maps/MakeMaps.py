
####
'GDAL requires Python 3.9 minimum'
'Exe or py script needs to be run from "maps" folder'
'Modify list.txt with query info with columns: var_name, year_window, gcm_name'
'VALID VARIABLE NAME STRINGS: DEM, accm, mean, mx5p, pwd, pww, ratio, sdev, skew, srad, srsd, tdew, timepk, tmax, tmin, tnsd, txsd'
'VALID YEAR WINDOW STRINGS: 1974_2013, 2000_2029, 2010_2039, 2020_2049, 2030_2059, 2040_2069, 2050_2079, 2060_2089, 2070_2099'
'VALID GCM NAME STRINGS: CCSM4, CanESM2, MIROC5'
'Note that for DEM, ratio, and timepk, only the 1974_2013 window is valid.'
'Command line to create exe using pyinstaller: pyinstaller --onefile --window MakeMaps.py'
'This command creates build and dist folders inside cwd. Copy Exe from dist to top of directory before running exe'
####

import sys
import os
import pandas as pd
from osgeo import ogr
from osgeo import gdal

application_path = os.path.dirname(sys.executable)
cwd = application_path
mapDIR = os.path.join(cwd)
listFILE = os.path.join(cwd, 'list.txt')

def readlist(listFILE):
  with open(listFILE) as f:
    next(f)
    lines = f.readlines()
  maps = []
  for line in lines:
    row = line.strip('\n').split(',')
    var = str(row[0])
    yrs = str(row[1])
    gcm = str(row[2])
    maps.append([var, yrs, gcm])
  return maps

def makegeotiff(var, yr, gdb):
  gdbDIR = os.path.join(os.path.split(cwd)[:-1][0], '{}.gdb'.format(gdb))
  driver = gdal.GetDriverByName('GTiff')
  if var != 'DEM':
    raster_name = var + '_' + yr
  else:
    raster_name = var
  output = os.path.join(mapDIR, 'maps_out', raster_name + '.tif')
  dataset = gdal.Open(f'OpenFileGDB:{gdbDIR}:{raster_name}')
  transform = dataset.GetGeoTransform()
  srs = dataset.GetSpatialRef()
  dataset.SetGeoTransform(transform)
  dataset.SetSpatialRef(srs)
  dataset.SetProjection(srs.ExportToWkt())
  options = ['COMPRESS=LZW']
  raster_tif = driver.CreateCopy(output, dataset, 0, options=options)
  dataset.FlushCache()
  raster_tif.FlushCache()
  dataset = None
  raster_tif = None
  return None

if __name__ == '__main__':
  maps = readlist(listFILE)
  for m in maps:
    makegeotiff(m[0], m[1], m[2])
