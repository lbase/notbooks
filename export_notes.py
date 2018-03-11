#!/usr/bin/python3
from sys import argv
import os
import csv
from slugify import slugify

def export_notes(filename, savepath):
    filext='.txt'
    if os.path.exists(savepath) == False :
        os.mkdir(savepath)
    with open(filename, newline = '') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='"')
        for row in reader:
            if row['Title'] is None :
                row['Title'] = 'title text'
            if row['Text'] is None :
               row['Text'] = 'no text'
            fullfilename = slugify(row['Title'], separator=' ') + filext
            newfilename=os.path.join(savepath, fullfilename)
            revnote = open(newfilename, 'w')
            revnote.write(row['Text'].replace('\\n','\n'))
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

"""
