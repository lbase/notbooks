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


