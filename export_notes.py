#!/usr/bin/python3
from sys import argv
import os
import pandas as pd
from slugify import slugify


def export_notes(filename, savepath):
    filext='.txt'
    if os.path.exists(savepath) == False :
        os.mkdir(savepath)
    gq = open(filename, 'r') 
    reader = pd.read_csv(gq)
    for index, row in reader.iterrows():
            
            
            fullfilename = slugify(row['Title'], separator=' ') + filext
            # fullfilename = (row['Title']) + filext
            newfilename=os.path.join(savepath, fullfilename)
            revnote = open(newfilename, 'w')
            #revnote.write(row['Text'].replace('\\n','\n'))
            revnote.write(row['Text'])
            revnote.close    
        

export_notes(argv[1] , argv[2])

"""
gmdb2 did not seem to do the trick on export. 

Had to do a double import export

ended up exporting sql and then importing into sqlite db and exporting again

note the delimiter line for the DictReader as the export from sqlite was single quote double quote

```
mdb-export -I sqlite GeoQuick.dat GeoQuick_Tb > geoquick.sql
```
going to get rid of most of the spurious data before I commit...

3-10-18

rfile at home
==========
3-11-18
switch to pandas 
works with out double import export
mdb-export GeoQuick.dat GeoQuick_Tb > gqmdb.csv
"""
