import sys
import os
import pandas as pd
from osgeo import ogr
from osgeo import gdal

cwd = os.getcwd()
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
  
