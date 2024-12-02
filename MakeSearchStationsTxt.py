####
'Finds wind data from nearest station in ground network within the SW and surrounding states'
'Filters out ground records with wind parameters that were taken from another station'
####

import os

cwd = os.getcwd()
parDIR = os.path.join(cwd, 'parfiles-2015')
searchFILE = os.path.join(cwd, 'search_stations.txt')

states = ['az', 'ca', 'co', 'id', 'nm', 'nv', 'ok', 'or', 'tx', 'ut', 'wy']

parfiles = os.listdir(parDIR)
parfiles = [f for f in parfiles if f[:2] in states]

with open(searchFILE, 'w') as f_out:

  f_out.write('stationID,x,y\n')

  for parf in parfiles:
    
    with open(os.path.join(parDIR, parf)) as f:
      lines = f.readlines()
  
    row = lines[1].split('=')
    y = row[1].split()[0]
    x = row[2].split()[0]

    hdr = lines[0]
    name = hdr.split()[0]
    
    if name in lines[86][:25]:
      f_out.write(parf[:-4] + ',' + str(x) + ',' + str(y) + '\n')        


