#!/usr/bin/python3
from lxml import etree

NSM = {"gpx": "http://www.topografix.com/GPX/1/0"}
NSGS = {"groundspeak": "http://www.groundspeak.com/cache/1/0/1"}
tree = etree.parse("CCreek.gpx")
root = tree.getroot()
# for elem in tree.findall("//wpt/type", root.nsmap):
map2={'gpx': 'http://www.topografix.com/GPX/1/0','groundspeak': 'http://www.groundspeak.com/cache/1/0/1'}
#>>> root.xpath('//a:HistoryRecords', namespaces=nsmap)
for elem in root.findall("groundspeak:type", NSGS):
    print(elem)

