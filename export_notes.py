#!/usr/bin/python3
from sys import argv
import csv
 
def export_notes(filename, savepath):
    titles = []
    textx = []
 
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            titles.append(row[0])
            textx.append(row[1])
 
    # return titles, textx
    x = len(titles)
    for x in range(x):
        """
        function should get passed the path now
        """
        #path = '/home/rfile/megrev/'
        filext = '.txt'
        titles[x] = titles[x].replace("/", "-")
        newfilename = savepath + titles[x] + filext
        revnote =  open(newfilename,'w')
        revnote.write(textx[x])
        revnote.close
 

export_notes(argv[1] , argv[2])
